#!/usr/bin/env python3
"""Offline configuration checks, or explicit stdio initialize/tools-list probe.

Never calls a research/library tool. --connect launches third-party code and may
install packages. This is a diagnostic, not a sandbox or a client policy check.
"""
import argparse
import json
import os
from pathlib import Path
import queue
import re
import subprocess
import threading
import time

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / 'integrations/literature/servers.json'


def validate_catalog(catalog):
    errors = []
    for name, server in catalog['servers'].items():
        if not re.fullmatch(r'[0-9a-f]{40}', server['source_commit']):
            errors.append(f'{name}: missing source revision')
        if not server['allowed_tools'] or len(set(server['allowed_tools'])) != len(server['allowed_tools']):
            errors.append(f'{name}: invalid tool allowlist')
        if server['command'] == 'npx':
            expected = ['-y', f'@cyanheads/{name}-mcp-server@{server["version"]}']
        else:
            expected = ['--from', f'git+{server["repository"]}.git@{server["source_commit"]}', 'zotero-mcp', 'serve', '--transport', 'stdio']
        if server['args'] != expected:
            errors.append(f'{name}: executable reference differs from pin')
        fragment = json.loads((ROOT / f'integrations/literature/{name}.client.example.json').read_text())
        if fragment != {'mcpServers': {f'galileo_{name}': {k: server[k] for k in ('command', 'args', 'env')}}}:
            errors.append(f'{name}: client fragment differs from catalog')
    return errors


def probe(command, allowed_tools, timeout=60, env=None):
    """Return advertised tool count and missing allowlisted names; no tool calls."""
    process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                               stderr=subprocess.DEVNULL, text=True, env=env)
    messages = queue.Queue()

    def read():
        try:
            for line in process.stdout:
                try:
                    messages.put(json.loads(line))
                except json.JSONDecodeError:
                    messages.put({'probe_error': 'Non-JSON output on MCP stdout'})
        finally:
            messages.put({'probe_error': 'MCP process closed stdout'})

    reader = threading.Thread(target=read, daemon=True)
    reader.start()
    deadline = time.monotonic() + timeout

    def send(message):
        process.stdin.write(json.dumps({'jsonrpc': '2.0', **message}) + '\n')
        process.stdin.flush()

    def request(identifier, method, params):
        send({'id': identifier, 'method': method, 'params': params})
        while True:
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                raise TimeoutError('MCP probe timed out')
            try:
                response = messages.get(timeout=remaining)
            except queue.Empty:
                raise TimeoutError('MCP probe timed out') from None
            if not isinstance(response, dict):
                raise RuntimeError('Invalid MCP message')
            if 'probe_error' in response:
                raise RuntimeError(response['probe_error'])
            # Reject unexpected server requests instead of granting capabilities.
            if 'method' in response and 'id' in response:
                send({'id': response['id'], 'error': {'code': -32601, 'message': 'Unsupported client request'}})
            if response.get('id') != identifier or 'method' in response:
                continue
            if 'error' in response or not isinstance(response.get('result'), dict):
                raise RuntimeError(f'MCP {method} failed (server payload withheld)')
            return response['result']

    try:
        result = request(1, 'initialize', {'protocolVersion': '2024-11-05',
                         'capabilities': {}, 'clientInfo': {'name': 'galileo-probe', 'version': '1.0'}})
        if result.get('protocolVersion') not in ('2024-11-05', '2025-03-26', '2025-06-18'):
            raise RuntimeError('Unsupported negotiated MCP version')
        send({'method': 'notifications/initialized'})
        names = set()
        cursor = None
        for page in range(20):
            result = request(2 + page, 'tools/list', {'cursor': cursor} if cursor else {})
            tools = result.get('tools')
            if not isinstance(tools, list) or any(not isinstance(t, dict) or not isinstance(t.get('name'), str) for t in tools):
                raise RuntimeError('Malformed tools/list response')
            names.update(t['name'] for t in tools)
            cursor = result.get('nextCursor')
            if not cursor:
                break
        else:
            raise RuntimeError('Tool-list pagination exceeded 20 pages')
        missing = sorted(set(allowed_tools) - names)
        return {'advertised_tool_count': len(names), 'missing_allowed_tools': missing,
                'tool_execution_tested': False, 'client_allowlist_enforcement_tested': False}
    finally:
        if process.poll() is None:
            process.terminate()
            try:
                process.wait(timeout=2)
            except subprocess.TimeoutExpired:
                process.kill()
                process.wait(timeout=2)
        reader.join(timeout=1)
        process.stdin.close()
        process.stdout.close()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--connect', choices=('pubmed', 'openalex', 'crossref', 'zotero'))
    parser.add_argument('--timeout', type=float, default=60)
    args = parser.parse_args()
    if not 0 < args.timeout <= 300:
        parser.error('--timeout must be between 0 and 300 seconds')
    catalog = json.loads(CATALOG.read_text())
    errors = validate_catalog(catalog)
    if errors:
        print('\n'.join(errors))
        return 1
    if not args.connect:
        print('Offline catalog and JSON fragments verified. No server launched; no network used.')
        return 0
    server = catalog['servers'][args.connect]
    if args.connect == 'zotero':
        config = Path.home() / '.config/zotero-mcp/config.json'
        if config.exists():
            print('Zotero probe refused: existing startup config can activate indexing/embeddings. Inspect it and use your client deliberately.')
            return 1
    # Avoid passing unrelated model/API keys to the subprocess. Runtime essentials
    # and explicitly listed server variables only; no values are printed.
    keep = ('PATH', 'HOME', 'USERPROFILE', 'SYSTEMROOT', 'TEMP', 'TMP', 'TMPDIR', 'SSL_CERT_FILE', 'SSL_CERT_DIR')
    env = {k: os.environ[k] for k in (*keep, *server['optional_env_vars']) if k in os.environ}
    env.update(server['env'])
    print(f'Launching pinned {args.connect} server for initialize + tools/list only; packages may download.')
    try:
        result = probe([server['command'], *server['args']], server['allowed_tools'], args.timeout, env)
    except (OSError, RuntimeError, TimeoutError):
        print('Connection probe failed. Check runtime, server configuration and upstream diagnostics locally; payloads withheld.')
        return 1
    print(json.dumps(result, indent=2))
    return int(bool(result['missing_allowed_tools']))


if __name__ == '__main__':
    raise SystemExit(main())
