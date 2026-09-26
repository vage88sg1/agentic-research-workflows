#!/usr/bin/env python3
"""Offline, non-overwriting installation of a selected workflow/skill profile."""
import argparse
import hashlib
import json
import shutil
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def install(destination, dry_run=False, root=ROOT, profile='full'):
    destination = Path(destination).expanduser().resolve()
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
    if dry_run:
        return {'dry_run': True, 'profile': profile, 'destination': str(destination), 'skills': [s.name for s in sources]}
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
    except Exception:
        for target in reversed(created):
            shutil.rmtree(target)
        raise
    return {'dry_run': False, 'profile': profile, 'destination': str(destination), 'installed': [p.name for p in created]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dest', required=True, help='The skill directory supported by your host')
    parser.add_argument('--dry-run', action='store_true', help='Validate and show plan without writing')
    parser.add_argument('--profile', choices=('core', 'docx', 'latex', 'slides', 'full'), default='full')
    args = parser.parse_args()
    try:
        print(json.dumps(install(args.dest, args.dry_run, profile=args.profile), indent=2))
    except (OSError, ValueError) as error:
        parser.exit(1, f'Installation stopped: {error}\n')


if __name__ == '__main__':
    main()
