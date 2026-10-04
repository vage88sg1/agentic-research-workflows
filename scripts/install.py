#!/usr/bin/env python3
"""Offline, non-overwriting installation of a selected workflow/skill profile."""
import argparse
import hashlib
import importlib.util
import json
import shutil
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location('galileo_model_settings', ROOT / 'skills/galileo/scripts/model_settings.py')
model_settings = importlib.util.module_from_spec(_spec)
_previous_bytecode_policy = sys.dont_write_bytecode
try:
    # Importing a helper from a skill must not generate cache payloads that the
    # installer would then redistribute as part of that skill.
    sys.dont_write_bytecode = True
    _spec.loader.exec_module(model_settings)
finally:
    sys.dont_write_bytecode = _previous_bytecode_policy


def install(destination, dry_run=False, root=ROOT, profile='full', model_preferences=None):
    destination = Path(destination).expanduser().resolve()
    preferences = model_settings.validate(model_preferences) if model_preferences is not None else model_settings.defaults(model_settings.infer_harness(destination))
    provenance = json.loads((root / 'vendor/provenance.json').read_text())
    inventory = {p.relative_to(root / 'vendor').as_posix() for p in (root / 'vendor').rglob('*') if p.is_file() or p.is_symlink()}
    if inventory != set(provenance['files']) | {'provenance.json'}:
        raise ValueError('Vendor inventory differs from provenance; restore a clean vendor directory')
    for relative, expected in provenance['files'].items():
        path = root / 'vendor' / relative
        if path.is_symlink() or not path.is_file():
            raise ValueError(f'Missing or symlinked vendor file: {relative}')
        if hashlib.sha256(path.read_bytes()).hexdigest() != expected:
            raise ValueError(f'Vendor hash mismatch: {relative}')
    bundle = json.loads((root / 'bundle.json').read_text())
    if profile not in bundle['profiles']:
        raise ValueError(f'Unknown profile: {profile}')
    selected = bundle['profiles'][profile]
    sources = [root / ('skills' if name in bundle['original_skills'] else 'vendor') / name
               for name in selected]
    for source in sources:
        if source.is_symlink():
            raise ValueError(f'Symlinked skill directory: {source.name}')
        if not (source / 'SKILL.md').is_file():
            raise ValueError(f'Missing skill: {source.name}')
        if any(p.is_symlink() for p in source.rglob('*')):
            raise ValueError(f'Symlinked skill content: {source.name}')
        if (destination / source.name).exists() or (destination / source.name).is_symlink():
            raise FileExistsError(f'Refusing existing destination: {destination / source.name}')
    settings_path = destination / model_settings.FILENAME
    if settings_path.exists() or settings_path.is_symlink():
        raise FileExistsError(f'Refusing existing model settings: {settings_path}')
    if dry_run:
        return {'dry_run': True, 'profile': profile, 'destination': str(destination), 'skills': [s.name for s in sources],
                'model_settings': {'path': str(settings_path), 'preferences': preferences}}
    destination.mkdir(parents=True, exist_ok=True)
    created = []
    try:
        with tempfile.TemporaryDirectory(prefix='.research-install-', dir=destination) as staging:
            staging = Path(staging)
            for source in sources:
                target = staging / source.name
                shutil.copytree(source, target)
                source_info = provenance['skill_sources'].get(source.name, {})
                license_path = root / 'LICENSE' if source.parent.name == 'skills' else root / 'vendor' / source_info['license_file']
                shutil.copy2(license_path, target / 'BUNDLE_LICENSE.txt')
                (target / 'bundle-provenance.json').write_text(json.dumps({
                    'package': 'agentic-research-workflows',
                    'display_name': 'Galileo: Agentic Research Workflows',
                    'source_type': 'original' if source.parent.name == 'skills' else 'vendored',
                    'upstream_repository': source_info.get('repository'),
                    'upstream_commit': source_info.get('commit'),
                    'installed_files_sha256': {p.relative_to(target).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
                                               for p in sorted(target.rglob('*')) if p.is_file()},
                }, indent=2) + '\n')
            for source in sources:
                target = destination / source.name
                # copytree refuses collisions, including ones appearing after preflight.
                try:
                    shutil.copytree(staging / source.name, target)
                except FileExistsError:
                    raise
                except Exception:
                    if target.is_dir():
                        shutil.rmtree(target)
                    raise
                created.append(target)
            # Save only after every skill copy succeeds. Atomic exclusive creation
            # preserves a concurrent settings file and triggers skill rollback.
            settings_record = model_settings.save(destination, preferences)
    except Exception:
        for target in reversed(created):
            shutil.rmtree(target)
        raise
    return {'dry_run': False, 'profile': profile, 'destination': str(destination), 'installed': [p.name for p in created],
            'model_settings': settings_record, 'configuration_status': preferences['configuration_status']}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dest', required=True, help='The skill directory supported by your host')
    parser.add_argument('--dry-run', action='store_true', help='Validate and show plan without writing')
    parser.add_argument('--profile', choices=tuple(json.loads((ROOT / 'bundle.json').read_text())['profiles']), default='full')
    parser.add_argument('--non-interactive', action='store_true', help='Skip questions; import preferences or defer to first use')
    parser.add_argument('--model-settings', help='Import a validated model-preferences JSON')
    parser.add_argument('--available-models', help='Offline JSON inventory (harness and models) for guided setup')
    parser.add_argument('--configure-models', action='store_true', help='Configure an existing Galileo installation without copying skills')
    parser.add_argument('--replace-model-settings', action='store_true', help='Allow replacement of existing preferences with a backup; requires --configure-models')
    args = parser.parse_args()
    if args.model_settings and args.available_models:
        parser.error('--model-settings and --available-models are alternatives')
    if args.replace_model_settings and not args.configure_models:
        parser.error('--replace-model-settings requires --configure-models')
    try:
        destination = Path(args.dest).expanduser().resolve()
        inventory = model_settings.load_inventory(args.available_models) if args.available_models else None
        preferences = model_settings.load(args.model_settings) if args.model_settings else None
        if args.configure_models:
            if not (destination / 'galileo/SKILL.md').is_file():
                raise ValueError('--configure-models requires an existing Galileo installation')
            if (destination / model_settings.FILENAME).is_symlink():
                raise ValueError('Refusing symlinked model settings')
            if (destination / model_settings.FILENAME).exists() and not args.replace_model_settings and not args.dry_run:
                raise FileExistsError('Existing preferences are preserved; use --replace-model-settings to replace with backup')
        else:
            # Check collisions and vendor integrity before asking any questions.
            install(destination, dry_run=True, profile=args.profile, model_preferences=preferences)
        interactive = not args.non_interactive and sys.stdin.isatty() and sys.stderr.isatty()
        if not args.dry_run and preferences is None:
            if interactive:
                previous = destination / model_settings.FILENAME
                preferences = model_settings.wizard(model_settings.infer_harness(destination), inventory,
                                                     existing=model_settings.load(previous) if previous.exists() else None)
            elif args.configure_models or inventory is not None:
                raise ValueError('Guided model setup requires a terminal; use --model-settings for unattended configuration')
        if args.configure_models:
            if args.dry_run:
                result = {'dry_run': True, 'model_settings': {'path': str(destination / model_settings.FILENAME),
                          'preferences': preferences or (model_settings.load(destination / model_settings.FILENAME)
                                         if (destination / model_settings.FILENAME).exists()
                                         else model_settings.defaults(model_settings.infer_harness(destination)))}}
            else:
                result = model_settings.save(destination, preferences, replace=args.replace_model_settings)
        else:
            result = install(destination, args.dry_run, profile=args.profile, model_preferences=preferences)
        print(json.dumps(result, indent=2))
    except (OSError, ValueError, EOFError, KeyboardInterrupt) as error:
        parser.exit(1, f'Installation stopped: {error}\n')


if __name__ == '__main__':
    main()
