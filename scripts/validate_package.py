#!/usr/bin/env python3
"""Validate original entry points, local links and vendor provenance offline."""
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def validate():
    errors = []
    provenance = json.loads((ROOT / 'vendor/provenance.json').read_text())
    inventory = {p.relative_to(ROOT / 'vendor').as_posix() for p in (ROOT / 'vendor').rglob('*') if p.is_file() or p.is_symlink()}
    if inventory != set(provenance['files']) | {'provenance.json'}:
        errors.append('Vendor inventory differs from provenance')
    for relative, expected in provenance['files'].items():
        path = ROOT / 'vendor' / relative
        if path.is_symlink() or not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != expected:
            errors.append(f'Vendor hash mismatch: {relative}')
    for path in ROOT.rglob('*.md'):
        if 'vendor' in path.relative_to(ROOT).parts:
            continue  # Upstream links may intentionally refer to optional, unbundled skills.
        for link in re.findall(r'\]\(([^)]+)\)', path.read_text()):
            if '://' in link or link.startswith('#'):
                continue
            target = link.split('#')[0]
            if target and not (path.parent / target).exists():
                errors.append(f'Broken local link in {path.relative_to(ROOT)}: {link}')
    bundle = json.loads((ROOT / 'bundle.json').read_text())
    available = set(bundle['original_skills']) | set(provenance['skills'])
    for profile, names in bundle['profiles'].items():
        if len(names) != len(set(names)) or not set(names) <= available:
            errors.append(f'Invalid profile: {profile}')
    for name in bundle['original_skills']:
        path = ROOT / 'skills' / name / 'SKILL.md'
        text = path.read_text()
        if not text.startswith('---\n') or f'name: {name}\n' not in text:
            errors.append(f'Invalid skill frontmatter: {name}')
        if not re.search(r'^description: .+', text, re.M):
            errors.append(f'Missing description: {name}')
        ui = (path.parent / 'agents/openai.yaml').read_text()
        if '$' + name not in ui:
            errors.append(f'Missing skill reference in UI prompt: {name}')
    from check_literature_mcp import CATALOG, validate_catalog
    errors.extend(validate_catalog(json.loads(CATALOG.read_text())))
    return errors


if __name__ == '__main__':
    issues = validate()
    for issue in issues:
        print(issue)
    print('Package validation passed.' if not issues else 'Package validation failed.')
    raise SystemExit(bool(issues))
