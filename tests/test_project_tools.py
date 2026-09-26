import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'skills/research-project/scripts/research_tools.py'
spec = importlib.util.spec_from_file_location('project_tools', SCRIPT)
tools = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tools)


def example():
    return {'schema_version': 1,
            'sources': [{'id': 'source', 'access': 'metadata'}],
            'claims': [{'id': 'claim', 'text': 'Example claim', 'evidence': [
                {'source_id': 'source', 'relation': 'supports', 'verification': 'pending'}]}],
            'artifacts': [{'id': 'table', 'depends_on': ['claim']},
                          {'id': 'slides', 'depends_on': ['table']}]}


class ProjectToolsTests(unittest.TestCase):
    def test_metadata_and_pending_cannot_pass_as_content(self):
        report = tools.evidence_report(example())
        self.assertEqual({v['issue'] for v in report['issues']},
                         {'verification_pending', 'metadata_is_not_content_support'})
        self.assertFalse(report['semantic_support_verified_by_script'])

    def test_checked_evidence_requires_audit_fields(self):
        data = example()
        data['claims'][0]['evidence'][0]['verification'] = 'human_verified'
        with self.assertRaisesRegex(ValueError, 'locator, verifier and date'):
            tools.evidence_report(data)

    def test_graph_rejects_unknown_dependencies_cycles_and_duplicate_ids(self):
        data = example()
        data['artifacts'][0]['depends_on'] = ['missing']
        with self.assertRaisesRegex(ValueError, 'unknown dependency'):
            tools.index_map(data)
        data = example()
        data['sources'][0]['depends_on'] = ['slides']
        with self.assertRaisesRegex(ValueError, 'Cyclic'):
            tools.index_map(data)
        data = example()
        data['artifacts'][0]['id'] = 'source'
        with self.assertRaisesRegex(ValueError, 'Duplicate ID'):
            tools.index_map(data)

    def test_content_change_reaches_indirect_artifacts_without_mutating_map(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / 'input.txt'
            source.write_text('before')
            data = example()
            data['sources'][0].update(path='input.txt', sha256=tools.digest(source))
            before = json.dumps(data)
            self.assertEqual(tools.impact_report(data, root, [])['requires_recheck'], [])
            source.write_text('after')
            report = tools.impact_report(data, root, [])
            self.assertEqual(report['affected_artifacts'], ['slides', 'table'])
            self.assertEqual(report['reasons']['source'], 'content_hash_changed')
            self.assertEqual(json.dumps(data), before)
            source.unlink()
            self.assertEqual(tools.impact_report(data, root, [])['reasons']['source'], 'missing_or_unsafe_file')

    def test_explicit_remote_change_and_unregistered_id(self):
        self.assertEqual(tools.impact_report(example(), '.', ['source'])['requires_recheck'],
                         ['claim', 'slides', 'source', 'table'])
        with self.assertRaisesRegex(ValueError, 'Unknown changed'):
            tools.impact_report(example(), '.', ['unknown'])

    def test_local_path_escape_and_symlink_are_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            target = root / 'data.txt'
            target.write_text('example')
            (root / 'link.txt').symlink_to(target)
            for path in ('../data.txt', str(target), 'link.txt', 'C:\\private.txt'):
                with self.subTest(path=path), self.assertRaises(ValueError):
                    tools.local_file(root, path)

    def manifest(self, root):
        (root / 'analysis.py').write_text('raise RuntimeError("must never execute")\n')
        return {'schema_version': 1, 'files': [{'path': 'analysis.py', 'sharing': 'synthetic',
                'sha256': tools.digest(root / 'analysis.py')}], 'environment': {'python': '3.11'},
                'reproduction_commands': ['python analysis.py'], 'excluded_inputs': [], 'license_or_terms': 'MIT'}

    def test_bundle_copies_only_allowlist_without_executing(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = self.manifest(root)
            (root / 'private.txt').write_text('not selected')
            destination = root / 'bundle'
            result = tools.build_bundle(manifest, root, destination)
            self.assertFalse(result['analysis_executed'])
            self.assertEqual([p.name for p in (destination / 'payload').iterdir()], ['analysis.py'])
            saved = json.loads((destination / 'bundle-manifest.json').read_text())
            self.assertEqual(saved['execution_status'], 'NOT_EXECUTED_BY_PACKAGER')
            with self.assertRaisesRegex(ValueError, 'already exists'):
                tools.build_bundle(manifest, root, destination)
            self.assertTrue((destination / 'payload/analysis.py').is_file())

    def test_bundle_rejects_restricted_credentials_and_changed_inputs(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = self.manifest(root)
            manifest['files'][0]['sharing'] = 'restricted'
            with self.assertRaisesRegex(ValueError, 'public or synthetic'):
                tools.build_bundle(manifest, root, root / 'bundle')
            manifest['files'][0]['sharing'] = 'synthetic'
            (root / 'analysis.py').write_text('changed')
            with self.assertRaisesRegex(ValueError, 'hash mismatch'):
                tools.build_bundle(manifest, root, root / 'bundle')
            secret = root / '.env'
            secret.write_text('example')
            manifest['files'][0].update(path='.env', sha256=tools.digest(secret))
            with self.assertRaisesRegex(ValueError, 'credential path'):
                tools.build_bundle(manifest, root, root / 'bundle')
            self.assertFalse((root / 'bundle').exists())

    def test_failed_copy_leaves_no_bundle(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = self.manifest(root)
            with patch.object(tools.shutil, 'copyfile', side_effect=OSError('copy failed')):
                with self.assertRaises(OSError):
                    tools.build_bundle(manifest, root, root / 'bundle')
            self.assertFalse((root / 'bundle').exists())
            self.assertFalse(list(root.glob('.galileo-bundle-*')))

    def test_preflight_does_not_execute_discovered_programs(self):
        with patch.object(tools.shutil, 'which', return_value='/example/executable'):
            result = tools.preflight()
        self.assertFalse(result['executables_launched'])
        self.assertEqual(set(result['host_capabilities'].values()), {'not_verified'})

    def test_synthetic_bundle_reproduces_recorded_result(self):
        source = ROOT / 'examples/synthetic-project'
        manifest = tools.load_json(source / 'reproducibility-manifest.json')
        data = tools.load_json(source / 'research-map.json')
        self.assertEqual(tools.evidence_report(data)['issues'], [])
        self.assertEqual(tools.impact_report(data, source, [])['requires_recheck'], [])
        with tempfile.TemporaryDirectory() as directory:
            destination = Path(directory) / 'reproduction'
            tools.build_bundle(manifest, source, destination)
            payload = destination / 'payload'
            baseline = (payload / 'results.json').read_bytes()
            (payload / 'results.json').unlink()
            result = subprocess.run([sys.executable, 'analyze.py'], cwd=payload,
                                    capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual((payload / 'results.json').read_bytes(), baseline)
            self.assertEqual(json.loads(baseline), {'n': 4, 'mean': 7.0})

    def test_evidence_cli_exit_two_for_issues(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'map.json'
            path.write_text(json.dumps(example()))
            result = subprocess.run([sys.executable, str(SCRIPT), 'evidence', '--map', str(path)],
                                    capture_output=True, text=True)
            self.assertEqual(result.returncode, 2)
            self.assertTrue(json.loads(result.stdout)['issues'])
