import importlib.util
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('literature', ROOT / 'scripts/check_literature_mcp.py')
mcp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mcp)

FAKE = '''
import json,sys
for line in sys.stdin:
 m=json.loads(line)
 if 'id' not in m: continue
 if m['method']=='initialize': r={'protocolVersion':'2024-11-05','capabilities':{},'serverInfo':{'name':'fake','version':'1'}}
 elif m['params'].get('cursor'): r={'tools':[{'name':'read_second','inputSchema':{'type':'object'}}]}
 else: r={'tools':[{'name':'read_first','inputSchema':{'type':'object'}}], 'nextCursor':'page2'}
 print(json.dumps({'jsonrpc':'2.0','id':m['id'],'result':r}),flush=True)
'''


class LiteratureTests(unittest.TestCase):
    def test_offline_catalog(self):
        self.assertEqual(mcp.validate_catalog(json.loads(mcp.CATALOG.read_text())), [])

    def test_codex_matches_catalog_and_stays_disabled(self):
        import tomllib  # CI uses Python 3.11; runtime probe needs only Python 3.10.
        catalog = json.loads(mcp.CATALOG.read_text())
        configs = tomllib.loads((ROOT / 'integrations/literature/codex.example.toml').read_text())['mcp_servers']
        self.assertEqual(set(configs), {f'galileo_{n}' for n in catalog['servers']})
        for name, server in catalog['servers'].items():
            c = configs[f'galileo_{name}']
            self.assertFalse(c['enabled'])
            self.assertFalse(c['required'])
            self.assertEqual(c['enabled_tools'], server['allowed_tools'])
            self.assertEqual(c['env_vars'], server['optional_env_vars'])
            for key in ('command', 'args', 'env'):
                self.assertEqual(c[key], server[key])

    def test_handshake_pagination_and_missing_tools(self):
        result = mcp.probe([sys.executable, '-u', '-c', FAKE], ['read_first', 'absent'], timeout=2)
        self.assertEqual(result['advertised_tool_count'], 2)
        self.assertEqual(result['missing_allowed_tools'], ['absent'])
        self.assertFalse(result['tool_execution_tested'])

    def test_timeout(self):
        with self.assertRaises(TimeoutError):
            mcp.probe([sys.executable, '-c', 'import time; time.sleep(10)'], [], timeout=.1)

    def test_protocol_error(self):
        with self.assertRaises(RuntimeError):
            mcp.probe([sys.executable, '-u', '-c', 'print("invalid",flush=True)'], [], timeout=2)

    def test_server_error(self):
        fake = FAKE.replace("'result':r", "'error':{'code':-32603,'message':'private payload'}")
        with self.assertRaisesRegex(RuntimeError, 'payload withheld'):
            mcp.probe([sys.executable, '-u', '-c', fake], [], timeout=2)
