import importlib.util
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('installer', ROOT / 'scripts/install.py')
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)


class InstallationTests(unittest.TestCase):
    def test_installed_office_payload_is_runnable_and_license_is_retained(self):
        import json
        import subprocess
        import sys
        with tempfile.TemporaryDirectory() as folder:
            dest = Path(folder) / 'skills'
            installer.install(dest, profile='docx')
            skill = dest / 'documents'
            self.assertEqual((skill / 'BUNDLE_LICENSE.txt').read_bytes(),
                             (ROOT / 'vendor/documents/LICENSE.md').read_bytes())
            record = json.loads((skill / 'bundle-provenance.json').read_text())
            self.assertEqual(record['upstream_commit'],
                             '9b34a87ee729f109019ac604681e5796349ea1b2')
            proc = subprocess.run([sys.executable, 'scripts/validate-documents.py', '--json',
                                   'fixtures/sample.docx', 'fixtures/sample.xlsx',
                                   'fixtures/sample.pptx', 'fixtures/sample.pdf'],
                                  cwd=skill, capture_output=True, text=True, check=True)
            report = json.loads(proc.stdout)
            self.assertEqual([item['format'] for item in report['files']],
                             ['docx', 'xlsx', 'pptx', 'pdf'])
            self.assertTrue(all(item['status'] == 'pass' for item in report['files']))
            self.assertTrue(all(item['render']['status'] == 'not_requested'
                                for item in report['files']))

    def test_office_skill_collision_is_not_overwritten(self):
        with tempfile.TemporaryDirectory() as folder:
            dest = Path(folder) / 'skills'
            existing = dest / 'documents'
            existing.mkdir(parents=True)
            (existing / 'SKILL.md').write_text('host-owned document skill')
            with self.assertRaises(FileExistsError):
                installer.install(dest, profile='full')
            self.assertEqual((existing / 'SKILL.md').read_text(), 'host-owned document skill')
            self.assertEqual([p.name for p in dest.iterdir()], ['documents'])

    def test_dry_run_has_no_writes(self):
        with tempfile.TemporaryDirectory() as folder:
            dest = Path(folder) / 'not-created'
            result = installer.install(dest, dry_run=True)
            self.assertEqual(len(result['skills']), 20)
            self.assertFalse(dest.exists())

    def test_install_is_self_contained_and_retains_notices(self):
        with tempfile.TemporaryDirectory() as folder:
            result = installer.install(Path(folder) / 'skills')
            self.assertEqual(len(result['installed']), 20)
            dest = Path(result['destination'])
            for name in result['installed']:
                self.assertTrue((dest / name / 'SKILL.md').is_file())
                self.assertTrue((dest / name / 'BUNDLE_LICENSE.txt').is_file())
                self.assertTrue((dest / name / 'bundle-provenance.json').is_file())
            self.assertTrue((dest / 'galileo/references/routing.md').is_file())
            self.assertTrue((dest / 'galileo/references/run-state.md').is_file())
            for name in ('research-drafting', 'research-review'):
                self.assertTrue((dest / name / 'references/agent-contracts.md').is_file())

    def test_collision_preserves_existing_files_and_installs_nothing(self):
        with tempfile.TemporaryDirectory() as folder:
            dest = Path(folder) / 'skills'
            existing = dest / 'scientific-writing'
            existing.mkdir(parents=True)
            (existing / 'keep.txt').write_text('original')
            with self.assertRaises(FileExistsError):
                installer.install(dest)
            self.assertEqual((existing / 'keep.txt').read_text(), 'original')
            self.assertEqual([p.name for p in dest.iterdir()], ['scientific-writing'])

    def test_tampered_vendor_is_rejected_before_writes(self):
        import shutil
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder) / 'package'
            shutil.copytree(ROOT / 'vendor', root / 'vendor')
            (root / 'vendor/scientific-writing/SKILL.md').write_text('tampered')
            dest = Path(folder) / 'skills'
            with self.assertRaisesRegex(ValueError, 'hash mismatch'):
                installer.install(dest, root=root)
            self.assertFalse(dest.exists())

    def test_conditional_profiles_and_distinct_license_provenance(self):
        import json
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            docx = installer.install(root / 'docx', profile='docx')
            self.assertNotIn('academic-writing-latex', docx['installed'])
            self.assertNotIn('scientific-slides', docx['installed'])
            latex = installer.install(root / 'latex', profile='latex')
            self.assertIn('academic-writing-latex', latex['installed'])
            self.assertNotIn('scientific-slides', latex['installed'])
            skill = root / 'latex/academic-writing-latex'
            self.assertEqual((skill / 'LICENSE').read_bytes(), (skill / 'BUNDLE_LICENSE.txt').read_bytes())
            record = json.loads((skill / 'bundle-provenance.json').read_text())
            self.assertEqual(record['upstream_repository'], 'https://github.com/HS0n4/academic-writing-latex-skills')
            slides = installer.install(root / 'slides', profile='slides')
            self.assertIn('research-presentations', slides['installed'])
            self.assertIn('scientific-slides', slides['installed'])
            self.assertNotIn('academic-writing-latex', slides['installed'])

    def test_extra_vendor_file_is_rejected_before_writes(self):
        import shutil
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder) / 'package'
            shutil.copytree(ROOT / 'vendor', root / 'vendor')
            (root / 'vendor/scientific-writing/untracked.py').write_text('print("unexpected")')
            dest = Path(folder) / 'skills'
            with self.assertRaisesRegex(ValueError, 'inventory differs'):
                installer.install(dest, root=root)
            self.assertFalse(dest.exists())

    def test_installed_hashes_cover_payload_and_license(self):
        import hashlib
        import json
        with tempfile.TemporaryDirectory() as folder:
            result = installer.install(Path(folder) / 'skills', profile='core')
            for name in result['installed']:
                target = Path(result['destination']) / name
                record = json.loads((target / 'bundle-provenance.json').read_text())
                actual = {p.relative_to(target).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
                          for p in target.rglob('*') if p.is_file() and p.name != 'bundle-provenance.json'}
                self.assertEqual(record['installed_files_sha256'], actual)
                self.assertIn('BUNDLE_LICENSE.txt', actual)

    def test_extended_profiles_include_portable_project_tools(self):
        import subprocess
        import sys
        expected = {'publishing': ['research-thesis-to-article', 'research-submission'],
                    'defense': ['research-defense', 'research-presentations'],
                    'systematic': ['research-systematic-review']}
        with tempfile.TemporaryDirectory() as directory:
            for profile, names in expected.items():
                destination = Path(directory) / profile
                result = installer.install(destination, profile=profile)
                self.assertIn('galileo', result['installed'])
                for name in names:
                    self.assertIn(name, result['installed'])
                script = destination / 'research-project/scripts/research_tools.py'
                check = subprocess.run([sys.executable, str(script), 'preflight'], cwd=directory,
                                       capture_output=True, text=True)
                self.assertEqual(check.returncode, 0, check.stderr)
                self.assertIn('not_verified', check.stdout)

    def test_copy_failure_rolls_back_only_new_skills(self):
        from unittest.mock import patch
        original = installer.shutil.copytree
        with tempfile.TemporaryDirectory() as folder:
            dest = Path(folder) / 'skills'
            dest.mkdir()
            (dest / 'unrelated.txt').write_text('keep')

            def fail_one_copy(source, target, *args, **kwargs):
                if Path(target).resolve() == (dest / 'research-review').resolve():
                    Path(target).mkdir()
                    (Path(target) / 'partial.txt').write_text('partial')
                    raise OSError('simulated copy failure')
                return original(source, target, *args, **kwargs)

            with patch.object(installer.shutil, 'copytree', side_effect=fail_one_copy):
                with self.assertRaisesRegex(OSError, 'simulated copy failure'):
                    installer.install(dest)
            self.assertEqual([p.name for p in dest.iterdir()], ['unrelated.txt'])
            self.assertEqual((dest / 'unrelated.txt').read_text(), 'keep')


if __name__ == '__main__':
    unittest.main()
