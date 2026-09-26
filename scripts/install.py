#!/usr/bin/env python3
"""Offline, non-overwriting installation of the two workflows and seven skills."""
import argparse
import hashlib
import json
import shutil
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def install(destination, dry_run=False, root=ROOT):
    destination = Path(destination).expanduser().resolve()
    provenance = json.loads((root / 'vendor/provenance.json').read_text())
    for relative, expected in provenance['files'].items():
        path = root / 'vendor' / relative
        if path.is_symlink() or not path.is_file():
            raise ValueError(f'Missing or symlinked vendor file: {relative}')
        if hashlib.sha256(path.read_bytes()).hexdigest() != expected:
            raise ValueError(f'Vendor hash mismatch: {relative}')
    sources = [root / 'skills/research-drafting', root / 'skills/research-review']
    sources += [root / 'vendor' / name for name in provenance['skills']]
    for source in sources:
        if not (source / 'SKILL.md').is_file():
            raise ValueError(f'Missing skill: {source.name}')
        if any(p.is_symlink() for p in source.rglob('*')):
            raise ValueError(f'Symlinked skill content: {source.name}')
        if (destination / source.name).exists() or (destination / source.name).is_symlink():
            raise FileExistsError(f'Refusing existing destination: {destination / source.name}')
    if dry_run:
        return {'dry_run': True, 'destination': str(destination), 'skills': [s.name for s in sources]}
    destination.mkdir(parents=True, exist_ok=True)
    created = []
    try:
        with tempfile.TemporaryDirectory(prefix='.research-install-', dir=destination) as staging:
            staging = Path(staging)
            for source in sources:
                target = staging / source.name
                shutil.copytree(source, target)
                shutil.copy2(root / ('LICENSE' if source.parent.name == 'skills' else 'vendor/LICENSE.md'), target / 'BUNDLE_LICENSE.txt')
                (target / 'bundle-provenance.json').write_text(json.dumps({
                    'package': 'agentic-research-workflows',
                    'source_type': 'original' if source.parent.name == 'skills' else 'vendored',
                    'upstream_repository': provenance['repository'] if source.parent.name == 'vendor' else None,
                    'upstream_commit': provenance['commit'] if source.parent.name == 'vendor' else None,
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
    return {'dry_run': False, 'destination': str(destination), 'installed': [p.name for p in created]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dest', required=True, help='The skill directory supported by your host')
    parser.add_argument('--dry-run', action='store_true', help='Validate and show plan without writing')
    args = parser.parse_args()
    try:
        print(json.dumps(install(args.dest, args.dry_run), indent=2))
    except (OSError, ValueError) as error:
        parser.exit(1, f'Installation stopped: {error}\n')


if __name__ == '__main__':
    main()
