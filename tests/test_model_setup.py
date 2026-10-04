"""Offline setup behavior, cancellation, persistence and installed helper portability."""
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('model_setup_installer', ROOT / 'scripts/install.py')
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)
models = installer.model_settings


def configured():
    settings = models.defaults('codex')
    settings.update(configuration_status='configured', available_models=['small', 'general', 'strong'],
                    inventory_source='user_supplied', cost_profile='quality')
    settings['provider_model_mapping'] = dict(zip(models.ALIASES, settings['available_models']))
    settings['role_overrides'] = {'reviewer_methods': 'strong'}
    return settings


class ModelSetupTests(unittest.TestCase):
    def run_cli(self, *args, script=None):
        return subprocess.run([sys.executable, str(script or ROOT / 'scripts/install.py'), *map(str, args)],
                              capture_output=True, text=True, timeout=30,
                              env=dict(os.environ, PYTHONDONTWRITEBYTECODE='1'))

    def test_wizard_maps_aliases_cost_and_role_override(self):
        answers = iter(['now', 'codex', 'small,general,strong', '1', '2', '3', 'economy',
                        'yes', 'reviewer_methods', '2', '', 'yes'])
        settings = models.wizard(input_fn=lambda _: next(answers), output_fn=lambda _: None)
        self.assertEqual(settings['provider_model_mapping'], {'economical': 'small', 'balanced': 'general', 'frontier': 'strong'})
        self.assertEqual(settings['role_overrides'], {'reviewer_methods': 'general'})
        self.assertEqual(settings['cost_profile'], 'economy')
        self.assertEqual(settings['harness'], 'codex')
        self.assertEqual(settings['routing_status'], 'preferences_only')

    def test_wizard_same_model_for_every_alias_and_retry_invalid_selection(self):
        answers = iter(['now', 'other', 'one', 'unlisted', '1', '', '', 'balanced', 'no', 'yes'])
        settings = models.wizard(input_fn=lambda _: next(answers), output_fn=lambda _: None)
        self.assertEqual(set(settings['provider_model_mapping'].values()), {'one'})

    def test_defer_or_keep_current_model_requires_no_inventory(self):
        deferred = models.wizard('codex', input_fn=lambda _: 'later', output_fn=lambda _: None)
        self.assertEqual(deferred, models.defaults('codex'))
        answers = iter(['now', 'codex', '', 'balanced', 'yes'])
        current = models.wizard(input_fn=lambda _: next(answers), output_fn=lambda _: None)
        self.assertEqual(current['configuration_status'], 'configured')
        self.assertTrue(all(value is None for value in current['provider_model_mapping'].values()))

    def test_wizard_inventory_harness_mismatch_is_rejected(self):
        answers = iter(['now', 'codex'])
        with self.assertRaisesRegex(ValueError, 'different harness'):
            models.wizard(inventory={'harness': 'claude-code', 'models': ['one']},
                          input_fn=lambda _: next(answers), output_fn=lambda _: None)

    def test_reconfiguration_reuses_previous_choices_and_deferral_preserves_them(self):
        previous = configured()
        deferred = models.wizard(existing=previous, input_fn=lambda _: 'later', output_fn=lambda _: None)
        self.assertEqual(deferred, previous)
        answers = iter(['now', '', '', '', '', '', '', 'no', 'yes'])
        settings = models.wizard(existing=previous, input_fn=lambda _: next(answers), output_fn=lambda _: None)
        self.assertEqual(settings, previous)

    def test_advanced_reconfiguration_can_remove_one_override(self):
        previous = configured()
        answers = iter(['now', '', '', '', '', '', '', 'yes', '-reviewer_methods', '', 'yes'])
        settings = models.wizard(existing=previous, input_fn=lambda _: next(answers), output_fn=lambda _: None)
        self.assertEqual(settings['role_overrides'], {})
        self.assertEqual(settings['provider_model_mapping'], previous['provider_model_mapping'])

    def test_reconfiguration_reports_overrides_removed_with_inventory_change(self):
        output = []
        answers = iter(['now', '', 'small,general', '', '', '2', '', 'no', 'yes'])
        settings = models.wizard(existing=configured(), input_fn=lambda _: next(answers), output_fn=output.append)
        self.assertEqual(settings['role_overrides'], {})
        self.assertEqual(settings['provider_model_mapping']['frontier'], 'general')
        self.assertTrue(any('Overrides removed' in line for line in output))

    def test_configure_dry_run_previews_existing_settings_without_replace(self):
        with tempfile.TemporaryDirectory() as folder:
            destination = Path(folder) / 'skills'
            installer.install(destination, profile='core', model_preferences=configured())
            original = (destination / models.FILENAME).read_bytes()
            result = self.run_cli('--dest', destination, '--configure-models', '--dry-run')
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(json.loads(result.stdout)['model_settings']['preferences'], configured())
            self.assertEqual((destination / models.FILENAME).read_bytes(), original)

    def test_wizard_cancelled_summary_and_eof_install_nothing(self):
        with tempfile.TemporaryDirectory() as folder:
            destination = Path(folder) / 'skills'
            for answers in (['now', 'other', '', 'balanced', 'no'], []):
                with patch.object(sys, 'argv', ['install.py', '--dest', str(destination), '--profile', 'core']), \
                     patch.object(sys.stdin, 'isatty', return_value=True), \
                     patch.object(sys.stderr, 'isatty', return_value=True), \
                     patch('builtins.input', side_effect=answers if answers else EOFError), \
                     patch('builtins.print'):
                    with self.assertRaises(SystemExit) as stopped:
                        installer.main()
                self.assertEqual(stopped.exception.code, 1)
                self.assertFalse(destination.exists())

    def test_invalid_settings_fail_before_any_installation(self):
        mutations = [lambda s: s.update(cost_profile='cheap'),
                     lambda s: s.update(unavailable_model_policy='silent'),
                     lambda s: s.update(routing_status='applied'),
                     lambda s: s['provider_model_mapping'].update(frontier='not-listed'),
                     lambda s: s['role_overrides'].update(unknown='strong'),
                     lambda s: s.update(api_key='not-a-setting'),
                     lambda s: s.update(configuration_status='deferred'),
                     lambda s: s.update(available_models=['same', 'same']),
                     lambda s: s.update(available_models=['bad\nidentifier']),
                     lambda s: s.update(schema_version=True)]
        with tempfile.TemporaryDirectory() as folder:
            destination = Path(folder) / 'skills'
            for mutate in mutations:
                settings = configured()
                mutate(settings)
                with self.assertRaises(ValueError):
                    installer.install(destination, profile='core', model_preferences=settings)
                self.assertFalse(destination.exists())

    def test_dry_run_import_has_no_writes_and_does_not_prompt(self):
        with tempfile.TemporaryDirectory() as folder:
            destination = Path(folder) / 'skills'
            preset = Path(folder) / 'preferences.json'
            preset.write_text(json.dumps(configured()))
            result = self.run_cli('--dest', destination, '--dry-run', '--model-settings', preset)
            self.assertEqual(result.returncode, 0, result.stderr)
            preview = json.loads(result.stdout)
            self.assertEqual(preview['model_settings']['preferences'], configured())
            self.assertFalse(destination.exists())

    def test_unattended_default_is_deferred_and_helper_is_installed(self):
        with tempfile.TemporaryDirectory() as folder:
            destination = Path(folder) / '.claude/skills'
            result = self.run_cli('--dest', destination, '--profile', 'core', '--non-interactive')
            self.assertEqual(result.returncode, 0, result.stderr)
            settings = models.load(destination / models.FILENAME)
            self.assertEqual(settings, models.defaults('claude-code'))
            helper = destination / 'galileo/scripts/model_settings.py'
            self.assertTrue(helper.is_file())
            # Installed helper derives its destination without the source package.
            check = self.run_cli('--dry-run', script=helper)
            self.assertEqual(check.returncode, 0, check.stderr)
            self.assertEqual(json.loads(check.stdout)['settings']['harness'], 'claude-code')

    def test_default_python_invocation_does_not_generate_or_install_helper_caches(self):
        with tempfile.TemporaryDirectory() as folder:
            package = Path(folder) / 'package'
            package.mkdir()
            for directory in ('scripts', 'skills', 'vendor'):
                shutil.copytree(ROOT / directory, package / directory, ignore=shutil.ignore_patterns('__pycache__'))
            for filename in ('bundle.json', 'LICENSE'):
                shutil.copy2(ROOT / filename, package / filename)
            destination = Path(folder) / 'skills'
            environment = dict(os.environ)
            environment.pop('PYTHONDONTWRITEBYTECODE', None)
            result = subprocess.run([sys.executable, str(package / 'scripts/install.py'), '--dest', str(destination),
                                     '--profile', 'core', '--non-interactive'], env=environment,
                                    capture_output=True, text=True, timeout=30)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertFalse(list((package / 'skills').rglob('__pycache__')))
            self.assertFalse(list(destination.rglob('__pycache__')))

    def test_unattended_inventory_needs_preset_not_a_hanging_prompt(self):
        with tempfile.TemporaryDirectory() as folder:
            destination = Path(folder) / 'skills'
            inventory = Path(folder) / 'models.json'
            inventory.write_text(json.dumps({'harness': 'other', 'models': ['one']}))
            result = self.run_cli('--dest', destination, '--available-models', inventory)
            self.assertEqual(result.returncode, 1)
            self.assertIn('requires a terminal', result.stderr)
            self.assertFalse(destination.exists())

    def test_existing_settings_are_not_overwritten_or_skills_installed(self):
        with tempfile.TemporaryDirectory() as folder:
            destination = Path(folder) / 'skills'
            models.save(destination, configured())
            original = (destination / models.FILENAME).read_bytes()
            with self.assertRaises(FileExistsError):
                installer.install(destination, profile='core')
            self.assertEqual((destination / models.FILENAME).read_bytes(), original)
            self.assertEqual([p.name for p in destination.iterdir()], [models.FILENAME])

    def test_persistence_failure_rolls_back_skill_installation(self):
        with tempfile.TemporaryDirectory() as folder:
            destination = Path(folder) / 'skills'
            destination.mkdir()
            (destination / 'unrelated.txt').write_text('keep')
            with patch.object(models, 'save', side_effect=OSError('simulated write failure')):
                with self.assertRaisesRegex(OSError, 'simulated write failure'):
                    installer.install(destination, profile='core')
            self.assertEqual([p.name for p in destination.iterdir()], ['unrelated.txt'])

    def test_atomic_creation_preserves_concurrent_settings_collision(self):
        with tempfile.TemporaryDirectory() as folder:
            destination = Path(folder)
            original_link = models.os.link

            def race(source, target):
                Path(target).write_text('concurrent settings')
                return original_link(source, target)

            with patch.object(models.os, 'link', side_effect=race):
                with self.assertRaises(FileExistsError):
                    models.save(destination, configured())
            self.assertEqual((destination / models.FILENAME).read_text(), 'concurrent settings')
            self.assertEqual([p.name for p in destination.iterdir()], [models.FILENAME])

    @unittest.skipUnless(hasattr(os, 'symlink'), 'requires symlinks')
    def test_symlink_settings_are_rejected_even_with_explicit_replace(self):
        with tempfile.TemporaryDirectory() as folder:
            destination = Path(folder) / 'skills'
            destination.mkdir()
            outside = Path(folder) / 'outside.json'
            outside.write_text('keep')
            (destination / models.FILENAME).symlink_to(outside)
            with self.assertRaises(ValueError):
                models.save(destination, configured(), replace=True)
            self.assertEqual(outside.read_text(), 'keep')

    def test_reconfigure_requires_explicit_replace_and_preserves_payload(self):
        with tempfile.TemporaryDirectory() as folder:
            destination = Path(folder) / 'skills'
            installer.install(destination, profile='core')
            before = {p.relative_to(destination).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
                      for p in destination.rglob('*') if p.is_file() and p.name != models.FILENAME}
            previous = (destination / models.FILENAME).read_bytes()
            preset = Path(folder) / 'preferences.json'
            preset.write_text(json.dumps(configured()))
            failed = self.run_cli('--dest', destination, '--configure-models', '--model-settings', preset)
            self.assertEqual(failed.returncode, 1)
            self.assertEqual((destination / models.FILENAME).read_bytes(), previous)
            success = self.run_cli('--dest', destination, '--configure-models', '--replace-model-settings',
                                   '--non-interactive', '--model-settings', preset)
            self.assertEqual(success.returncode, 0, success.stderr)
            record = json.loads(success.stdout)
            backup = Path(record['backup'])
            self.assertEqual(backup.read_bytes(), previous)
            self.assertEqual(models.load(destination / models.FILENAME), configured())
            after = {p.relative_to(destination).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
                     for p in destination.rglob('*') if p.is_file() and p.name != models.FILENAME and p.resolve() != backup.resolve()}
            self.assertEqual(before, after)

    def test_installed_helper_imports_new_settings_without_source_checkout(self):
        with tempfile.TemporaryDirectory() as folder:
            destination = Path(folder) / 'skills'
            installer.install(destination, profile='core')
            preset = Path(folder) / 'preferences.json'
            preset.write_text(json.dumps(configured()))
            helper = destination / 'galileo/scripts/model_settings.py'
            result = self.run_cli('--settings-file', preset, '--replace', script=helper)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(models.load(destination / models.FILENAME), configured())

    def test_examples_and_null_role_override_are_valid(self):
        self.assertEqual(models.load(ROOT / 'examples/model-settings.json')['routing_status'], 'preferences_only')
        settings = configured()
        settings['role_overrides']['coordinator'] = None
        self.assertIs(models.validate(settings), settings)


if __name__ == '__main__':
    unittest.main()
