#!/usr/bin/env python3
"""Offline project diagnostics, evidence structure, change impact and explicit bundles.

Python 3.10+ standard library. Reports JSON to stdout. Only bundle writes files;
no command from a project document is executed and no service is contacted.
"""
import argparse
from collections import deque
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import shutil
import sys
import tempfile


def digest(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def local_file(root, relative):
    if not isinstance(relative, str) or '\\' in relative:
        raise ValueError('Paths must be relative POSIX strings')
    path = PurePosixPath(relative)
    if path.is_absolute() or '..' in path.parts or not path.parts or ':' in relative:
        raise ValueError(f'Invalid project-relative path: {relative}')
    root = Path(root).resolve()
    current = root
    for part in path.parts:
        current /= part
        if current.is_symlink():
            raise ValueError(f'Symlink not permitted: {relative}')
    if not current.is_file():
        raise ValueError(f'Missing project file: {relative}')
    return current


def load_json(path):
    with Path(path).open(encoding='utf-8') as stream:
        value = json.load(stream)
    if not isinstance(value, dict):
        raise ValueError('Expected a JSON object')
    return value


def preflight():
    names = ('python3', 'Rscript', 'pandoc', 'libreoffice', 'soffice', 'latexmk',
             'pdflatex', 'xelatex', 'lualatex', 'biber', 'node', 'npx', 'uvx', 'git')
    found = {name: shutil.which(name) is not None for name in names}
    return {'python_version': '.'.join(map(str, sys.version_info[:3])),
            'executables_on_path': found, 'executables_launched': False,
            'host_capabilities': {name: 'not_verified' for name in
                ('independent_agents', 'model_routing', 'browsing', 'mcp_search',
                 'native_document_renderer', 'native_slide_renderer', 'native_latex_compiler')},
            'candidate_routes': {
                'office_export': 'binary_found_not_tested' if found['libreoffice'] or found['soffice'] else 'check_host_renderer',
                'latex': 'binary_found_not_tested' if any(found[k] for k in ('latexmk', 'pdflatex', 'xelatex', 'lualatex')) else 'check_host_compiler'},
            'next_action': 'Confirm host capabilities and perform only the selected route smoke check. PATH discovery is not operational validation.'}


def index_map(data):
    if data.get('schema_version') != 1:
        raise ValueError('Unsupported map schema_version')
    nodes = {}
    for group in ('sources', 'claims', 'artifacts'):
        values = data.get(group)
        if not isinstance(values, list):
            raise ValueError(f'{group} must be a list')
        for row in values:
            if not isinstance(row, dict) or not isinstance(row.get('id'), str) or not row['id'].strip():
                raise ValueError(f'Invalid ID in {group}')
            if row['id'] in nodes:
                raise ValueError(f'Duplicate ID: {row["id"]}')
            nodes[row['id']] = (group, row)
    deps = {key: set() for key in nodes}
    for key, (group, row) in nodes.items():
        if 'path' in row and (not isinstance(row.get('sha256'), str) or not re.fullmatch(r'[a-f0-9]{64}', row['sha256'])):
            raise ValueError(f'{key}: file paths require a recorded SHA-256 baseline')
        if group == 'sources' and row.get('access') not in ('metadata', 'abstract', 'full_text', 'executed_result'):
            raise ValueError(f'{key}: invalid source access level')
        links = row.get('depends_on', [])
        if not isinstance(links, list) or any(not isinstance(link, str) for link in links):
            raise ValueError(f'{key}: depends_on must be a list of IDs')
        deps[key].update(links)
        if group == 'claims':
            if not isinstance(row.get('text'), str) or not row['text'].strip():
                raise ValueError(f'{key}: claim text is required')
            evidence = row.get('evidence', [])
            if not isinstance(evidence, list):
                raise ValueError(f'{key}: evidence must be a list')
            for link in evidence:
                if not isinstance(link, dict) or link.get('source_id') not in nodes or nodes[link['source_id']][0] != 'sources':
                    raise ValueError(f'{key}: unknown evidence source')
                if link.get('relation') not in ('supports', 'contradicts', 'context'):
                    raise ValueError(f'{key}: invalid evidence relation')
                if link.get('verification') not in ('pending', 'ai_checked', 'human_verified'):
                    raise ValueError(f'{key}: invalid verification status')
                if link['verification'] != 'pending' and (not link.get('locator') or not link.get('verified_by') or not link.get('checked_at')):
                    raise ValueError(f'{key}: checked evidence needs locator, verifier and date')
                deps[key].add(link['source_id'])
        if not deps[key] <= nodes.keys():
            raise ValueError(f'{key}: unknown dependency')
    # Topological validation: cyclic provenance cannot support change propagation.
    remaining = {key: set(value) for key, value in deps.items()}
    ready = deque(key for key, value in remaining.items() if not value)
    reverse = {key: set() for key in nodes}
    for key, values in deps.items():
        for dependency in values:
            reverse[dependency].add(key)
    visited = 0
    while ready:
        key = ready.popleft()
        visited += 1
        for child in reverse[key]:
            remaining[child].remove(key)
            if not remaining[child]:
                ready.append(child)
    if visited != len(nodes):
        raise ValueError('Cyclic dependency graph')
    return nodes, reverse


def evidence_report(data):
    nodes, _ = index_map(data)
    issues = []
    for claim in data['claims']:
        links = claim.get('evidence', [])
        support = [e for e in links if e['relation'] == 'supports']
        if not support:
            issues.append({'id': claim['id'], 'issue': 'no_supporting_evidence'})
        for link in links:
            access = nodes[link['source_id']][1]['access']
            if link['verification'] == 'pending':
                issues.append({'id': claim['id'], 'source_id': link['source_id'], 'issue': 'verification_pending'})
            if access == 'metadata':
                issues.append({'id': claim['id'], 'source_id': link['source_id'], 'issue': 'metadata_is_not_content_support'})
            elif access == 'abstract':
                issues.append({'id': claim['id'], 'source_id': link['source_id'], 'issue': 'abstract_only_check_claim_scope'})
            if link['relation'] == 'contradicts':
                issues.append({'id': claim['id'], 'source_id': link['source_id'], 'issue': 'contradictory_evidence_requires_assessment'})
    if not data['claims']:
        issues.append({'issue': 'no_claims_recorded'})
    return {'schema_valid': True, 'issues': issues, 'claim_count': len(data['claims']),
            'semantic_support_verified_by_script': False,
            'note': 'Recorded verifier assertions are not independently validated. A clear report is not scientific approval.'}


def impact_report(data, root, changed):
    nodes, reverse = index_map(data)
    seeds = set(changed)
    if not seeds <= nodes.keys():
        raise ValueError('Unknown changed ID')
    reasons = {key: 'explicit_change' for key in seeds}
    for key, (_, row) in nodes.items():
        if 'path' in row:
            try:
                actual = digest(local_file(root, row['path']))
            except ValueError:
                reasons[key] = 'missing_or_unsafe_file'
                seeds.add(key)
                continue
            if actual != row['sha256']:
                seeds.add(key)
                reasons[key] = 'content_hash_changed'
    affected = set(seeds)
    work = deque(sorted(seeds))
    while work:
        for child in reverse[work.popleft()]:
            if child not in affected:
                affected.add(child)
                work.append(child)
    return {'changed': sorted(seeds), 'reasons': reasons, 'requires_recheck': sorted(affected),
            'affected_artifacts': [key for key in sorted(affected) if nodes[key][0] == 'artifacts'],
            'state_modified': False, 'note': 'Only recorded dependencies can be tracked; update issue/state records before regenerating affected outputs.'}


def build_bundle(manifest, root, destination):
    if manifest.get('schema_version') != 1:
        raise ValueError('Unsupported bundle schema_version')
    rows = manifest.get('files')
    commands = manifest.get('reproduction_commands')
    if not isinstance(rows, list) or not rows:
        raise ValueError('Explicit nonempty file allowlist required')
    if not isinstance(commands, list) or any(not isinstance(c, str) for c in commands) or not commands:
        raise ValueError('Document reproduction commands; they will not be executed')
    if not isinstance(manifest.get('environment'), dict) or not manifest['environment']:
        raise ValueError('Record environment/dependency information')
    if not isinstance(manifest.get('excluded_inputs'), list):
        raise ValueError('Record excluded_inputs, including access instructions where needed')
    if not isinstance(manifest.get('license_or_terms'), str) or not manifest['license_or_terms'].strip():
        raise ValueError('Record distribution license or terms')
    planned = []
    seen = set()
    for row in rows:
        if not isinstance(row, dict) or row.get('sharing') not in ('public', 'synthetic'):
            raise ValueError('Bundle files must be explicitly classified public or synthetic')
        relative = row.get('path')
        source = local_file(root, relative)
        canonical = source.relative_to(Path(root).resolve()).as_posix()
        if canonical in seen:
            raise ValueError('Duplicate bundle path')
        seen.add(canonical)
        if any(part.lower() in ('.git', '.ssh', '.codex', '.agents') or part.lower().startswith('.env') for part in PurePosixPath(canonical).parts):
            raise ValueError('Configuration/credential path excluded from bundles')
        if not isinstance(row.get('sha256'), str) or row['sha256'] != digest(source):
            raise ValueError(f'Bundle baseline hash mismatch: {canonical}')
        planned.append((source, canonical, row))
    destination = Path(destination).expanduser().absolute()
    if destination.exists() or destination.is_symlink():
        raise ValueError('Bundle destination already exists')
    if not destination.parent.is_dir():
        raise ValueError('Create the destination parent directory explicitly first')
    # Staging plus exclusive final mkdir preserves unrelated outputs on collision.
    with tempfile.TemporaryDirectory(prefix='.galileo-bundle-', dir=destination.parent) as temporary:
        staging = Path(temporary)
        for source, relative, row in planned:
            target = staging / 'payload' / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, target)
            if digest(target) != row['sha256']:
                raise ValueError('Input changed during bundle copy')
        record = {**manifest, 'execution_status': 'NOT_EXECUTED_BY_PACKAGER',
                  'files': [{**row, 'path': relative} for _, relative, row in planned]}
        (staging / 'bundle-manifest.json').write_text(json.dumps(record, indent=2) + '\n', encoding='utf-8')
        (staging / 'REPRODUCE.md').write_text(
            '# Reproduction package\n\nRun from `payload/` only after inspecting the commands and dependencies.\n'
            'Packaging did not execute or verify the analysis. File classifications were supplied by the author; no automatic secret/consent audit was performed.\n\n'
            '## Environment\n\n```json\n' + json.dumps(manifest['environment'], indent=2) + '\n```\n\n'
            '## Commands (recorded, not executed)\n\n```text\n' + '\n'.join(commands) + '\n```\n\n'
            '## Excluded inputs and access\n\n```json\n' + json.dumps(manifest['excluded_inputs'], indent=2) + '\n```\n', encoding='utf-8')
        destination.mkdir()  # Exclusive claim; never delete an existing destination.
        try:
            shutil.copytree(staging, destination, dirs_exist_ok=True)
        except Exception:
            shutil.rmtree(destination)
            raise
    return {'destination': str(destination), 'file_count': len(planned), 'analysis_executed': False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    sub.add_parser('preflight')
    for name in ('evidence', 'impact'):
        child = sub.add_parser(name)
        child.add_argument('--map', required=True)
        if name == 'impact':
            child.add_argument('--root', required=True)
            child.add_argument('--changed', action='append', default=[])
    child = sub.add_parser('bundle')
    child.add_argument('--manifest', required=True)
    child.add_argument('--root', required=True)
    child.add_argument('--dest', required=True)
    args = parser.parse_args()
    try:
        if args.command == 'preflight':
            report = preflight()
        elif args.command == 'evidence':
            report = evidence_report(load_json(args.map))
        elif args.command == 'impact':
            report = impact_report(load_json(args.map), args.root, args.changed)
        else:
            report = build_bundle(load_json(args.manifest), args.root, args.dest)
        print(json.dumps(report, indent=2))
        return 2 if args.command == 'evidence' and report['issues'] else 0
    except (ValueError, OSError, KeyError, TypeError) as error:
        print(json.dumps({'error': str(error)}), file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
