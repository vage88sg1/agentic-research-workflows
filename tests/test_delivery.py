import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'skills/research-project/scripts/research_tools.py'
spec = importlib.util.spec_from_file_location('delivery_tools', SCRIPT)
tools = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tools)


def record(root):
    artifact = root / 'manuscript.md'
    artifact.write_text('Synthetic manuscript.\n')
    ref = {'path': 'manuscript.md', 'sha256': tools.digest(artifact)}
    return {'schema_version': 1, 'status': 'complete', 'outputs': [ref],
            'completed_checks': [{'id': 'review-v1', 'status': 'performed', 'result': 'pass',
                'artifacts': [dict(ref)], 'reviewer': 'synthetic evaluator',
                'context': 'independent', 'scope': 'Whole synthetic manuscript',
                'evidence': 'Synthetic fixture, not scientific review'}],
            'required_checks': ['review-v1'],
            'readiness': {kind: {'status': 'checked', 'rationale': 'Synthetic fixture only',
                'check_ids': ['review-v1']} for kind in ('content', 'bibliography', 'review', 'production')}}


class DeliveryTests(unittest.TestCase):
    def codes(self, data, root):
        return {v['issue'] for v in tools.delivery_report(data, root)['issues']}

    def test_matching_records_do_not_certify_science_or_mutate_state(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            data = record(root)
            before = copy.deepcopy(data)
            report = tools.delivery_report(data, root)
            self.assertTrue(report['record_consistent'])
            self.assertFalse(report['scientific_validity_verified_by_script'])
            self.assertFalse(report['reviewer_identity_authenticated'])
            self.assertFalse(report['state_modified'])
            self.assertEqual(data, before)

    def test_changed_output_invalidates_old_review_even_after_rebaseline(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            data = record(root)
            (root / 'manuscript.md').write_text('Changed synthetic claims.\n')
            self.assertIn('output_hash_mismatch', self.codes(data, root))
            data['outputs'][0]['sha256'] = tools.digest(root / 'manuscript.md')
            codes = self.codes(data, root)
            self.assertNotIn('output_hash_mismatch', codes)
            self.assertIn('check_revision_mismatch', codes)
            self.assertIn('output_without_current_check', codes)

    def test_operational_complete_and_pending_bibliography_are_not_ready(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            data = record(root)
            data['readiness']['bibliography'] = {'status': 'pending', 'rationale': 'Background sources missing'}
            self.assertIn('readiness_pending_or_blocked', self.codes(data, root))
            del data['readiness']
            self.assertIn('readiness_unrecorded', self.codes(data, root))

    def test_performed_is_not_pass_and_missing_required_review_is_reported(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            data = record(root)
            del data['completed_checks'][0]['result']
            self.assertIn('required_check_not_passed', self.codes(data, root))
            data['completed_checks'] = []
            self.assertIn('required_check_missing', self.codes(data, root))

    def test_required_independence_cannot_be_replaced_by_self_review(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            data = record(root)
            data['readiness']['review']['requires_independent'] = True
            data['completed_checks'][0]['context'] = 'self'
            self.assertIn('required_independent_review_pending', self.codes(data, root))
            data['readiness']['review']['status'] = 'not_required'
            self.assertIn('required_independent_review_pending', self.codes(data, root))

    def test_checked_readiness_requires_referenced_checks(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            data = record(root)
            data['readiness']['content']['check_ids'] = []
            self.assertIn('checked_readiness_without_checks', self.codes(data, root))

    def test_unchanged_superseded_history_is_not_current_evidence(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            data = record(root)
            old = copy.deepcopy(data['completed_checks'][0])
            old.update(id='historical-review', status='superseded')
            old['artifacts'][0]['sha256'] = '0' * 64
            data['completed_checks'].append(old)
            self.assertEqual(self.codes(data, root), set())
            data['required_checks'].append('historical-review')
            self.assertIn('required_check_not_passed', self.codes(data, root))

    def test_every_selected_output_needs_current_coverage(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            data = record(root)
            (root / 'notes.md').write_text('Synthetic notes.\n')
            data['outputs'].append({'path': 'notes.md', 'sha256': tools.digest(root / 'notes.md')})
            self.assertIn('output_without_current_check', self.codes(data, root))
            data['completed_checks'][0]['artifacts'].append(dict(data['outputs'][1]))
            self.assertEqual(self.codes(data, root), set())

    def test_missing_traversal_absolute_and_symlink_outputs_are_not_read(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            data = record(root)
            (root / 'link.md').symlink_to(root / 'manuscript.md')
            for path in ('missing.md', '../manuscript.md', str(root / 'manuscript.md'), 'link.md'):
                changed = copy.deepcopy(data)
                changed['outputs'][0]['path'] = path
                with self.subTest(path=path):
                    self.assertIn('missing_or_unsafe_output', self.codes(changed, root))

    def test_incomplete_audit_schema_and_duplicate_aliases_are_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            data = record(root)
            del data['completed_checks'][0]['scope']
            with self.assertRaisesRegex(ValueError, 'scope and evidence'):
                tools.delivery_report(data, root)
            data = record(root)
            data['outputs'].append({**data['outputs'][0], 'path': './manuscript.md'})
            with self.assertRaisesRegex(ValueError, 'Duplicate delivery output'):
                tools.delivery_report(data, root)

    def test_installed_delivery_cli_is_read_only_and_exit_two_for_stale_records(self):
        spec = importlib.util.spec_from_file_location('delivery_installer', ROOT / 'scripts/install.py')
        installer = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(installer)
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            data = record(root)
            snapshot = root / 'state.json'
            snapshot.write_text(json.dumps(data))
            before = snapshot.read_bytes()
            installer.install(root / 'skills', profile='core')
            installed = root / 'skills/research-project/scripts/research_tools.py'
            result = subprocess.run([sys.executable, str(installed), 'delivery', '--state', str(snapshot),
                                     '--root', str(root)], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue(json.loads(result.stdout)['record_consistent'])
            (root / 'manuscript.md').write_text('Changed.\n')
            result = subprocess.run([sys.executable, str(installed), 'delivery', '--state', str(snapshot),
                                     '--root', str(root)], capture_output=True, text=True)
            self.assertEqual(result.returncode, 2, result.stderr)
            self.assertEqual(snapshot.read_bytes(), before)
