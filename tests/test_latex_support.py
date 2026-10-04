"""Packaging and wrapper behavior with controlled tools; no real TeX build."""
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('latex_installer', ROOT / 'scripts/install.py')
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)


class LatexSupportTests(unittest.TestCase):
    def test_conditional_installation_retains_license_and_exact_payload(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            result = installer.install(root / 'latex', profile='latex')
            self.assertIn('academic-writing-latex', result['installed'])
            self.assertIn('latex-safe-build', result['installed'])
            skill = root / 'latex/latex-safe-build'
            self.assertEqual((skill / 'BUNDLE_LICENSE.txt').read_bytes(),
                             (ROOT / 'vendor/latex-safe-build/LICENSE').read_bytes())
            manifest = json.loads((skill / 'bundle-provenance.json').read_text())
            self.assertEqual(manifest['upstream_commit'],
                             'd6cd2314676c44a56e58c8f892082ef00a6a8371')
            for relative, expected in manifest['installed_files_sha256'].items():
                self.assertEqual(hashlib.sha256((skill / relative).read_bytes()).hexdigest(), expected)
            docx = installer.install(root / 'docx', profile='docx')
            self.assertNotIn('latex-safe-build', docx['installed'])

    def _controlled_build(self, failure=False):
        # Test the installed shell wrapper, not TeX or native feature resolution.
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            installer.install(root / 'skills', profile='latex')
            src = root / 'source with spaces'
            src.mkdir()
            (src / 'paper.tex').write_text('\\documentclass{article}\n\\begin{document}Test\\end{document}\n')
            (src / 'paper.aux').write_text('previous auxiliary state')
            (src / 'paper.pdf').write_bytes(b'previous output preserved on failure')
            (src / 'figure.pdf').write_bytes((ROOT / 'vendor/documents/fixtures/sample.pdf').read_bytes())
            before = {p.name: p.read_bytes() for p in src.iterdir()}
            tools_dir = root / 'controlled-tools'
            tools_dir.mkdir()
            # Fix process discovery for a deterministic isolated test.
            (tools_dir / 'pgrep').write_text('#!/bin/sh\nexit 1\n')
            (tools_dir / 'pgrep').chmod(0o755)
            log = ('! Undefined control sequence\n' if failure else
                   "LaTeX Warning: Reference `missing' undefined on input line 1.\n")
            fake = f'''#!{sys.executable}
from pathlib import Path
import sys
main=Path(sys.argv[-1])
assert main.is_file()
assert not main.with_suffix('.aux').exists()
assert Path('figure.pdf').exists()
main.with_suffix('.log').write_text({log!r})
main.with_suffix('.aux').write_text('mock auxiliary')
Path('mock-working-directory.txt').write_text(str(Path.cwd()))
if {failure!r}: raise SystemExit(1)
main.with_suffix('.pdf').write_bytes(Path({str(ROOT / 'vendor/documents/fixtures/sample.pdf')!r}).read_bytes())
'''
            (tools_dir / 'latexmk').write_text(fake)
            (tools_dir / 'latexmk').chmod(0o755)
            temp_root = root / 'scratch'
            temp_root.mkdir()
            env = dict(os.environ, PATH=str(tools_dir) + os.pathsep + os.environ.get('PATH', ''),
                       TMPDIR=str(temp_root), PYTHONDONTWRITEBYTECODE='1')
            script = root / 'skills/latex-safe-build/scripts/safe-build.sh'
            proc = subprocess.run(['sh', str(script), str(src), 'paper.tex', '-pdf'],
                                  env=env, capture_output=True, text=True, timeout=30)
            after = {p.name: p.read_bytes() for p in src.iterdir()}
            if failure:
                self.assertNotEqual(proc.returncode, 0)
                self.assertEqual(before, after)
                self.assertIn('BUILD FAILED', proc.stdout)
            else:
                self.assertEqual(proc.returncode, 0, proc.stderr)
                self.assertIn('undefined', proc.stdout)
                self.assertIn('BUILD OK', proc.stdout)
                self.assertEqual({k: v for k, v in before.items() if k != 'paper.pdf'},
                                 {k: v for k, v in after.items() if k != 'paper.pdf'})
                self.assertEqual(after['paper.pdf'], before['figure.pdf'])
                build_roots = list((temp_root / 'latex-safe-build').glob('*/mock-working-directory.txt'))
                self.assertEqual(len(build_roots), 1)
                self.assertNotEqual(build_roots[0].read_text(), str(src))

    @unittest.skipUnless(os.name == 'posix' and shutil.which('rsync'), 'requires POSIX and rsync')
    def test_isolated_wrapper_preserves_inputs_and_reports_unresolved_refs_even_on_zero_exit(self):
        self._controlled_build()

    @unittest.skipUnless(os.name == 'posix' and shutil.which('rsync'), 'requires POSIX and rsync')
    def test_failed_build_does_not_replace_existing_output_or_inputs(self):
        self._controlled_build(failure=True)


if __name__ == '__main__':
    unittest.main()
