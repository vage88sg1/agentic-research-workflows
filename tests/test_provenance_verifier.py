import hashlib
import importlib.util
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import urllib.error
import wave
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'skills/research-provenance/scripts/verify_provenance.py'
spec = importlib.util.spec_from_file_location('provenance_verifier', SCRIPT)
verifier = importlib.util.module_from_spec(spec)
spec.loader.exec_module(verifier)


def image_response(state='trusted', outcome='detected'):
    return {'object': 'content_provenance_check', 'created_at': 1778000000,
            'results': [{'type': 'c2pa', 'outcome': outcome, 'validation_state': state,
                         'issuer': 'Example provider', 'model': None, 'generated_at': None},
                        {'type': 'synthid', 'outcome': 'not_detected', 'model': None,
                         'generated_at': None}]}


class ProvenanceVerifierTests(unittest.TestCase):
    def test_negative_openai_signal_does_not_erase_non_openai_credentials(self):
        checks = verifier.normalize_openai(image_response('valid', 'not_detected'), ('c2pa', 'synthid'))
        self.assertEqual(checks[0]['status'], 'NOT FOUND IN THIS CHECK')
        self.assertEqual(checks[0]['credential_status'], 'SIGNAL PRESENT')
        checks = verifier.normalize_openai(image_response('invalid', 'not_detected'), ('c2pa', 'synthid'))
        self.assertEqual(checks[0]['credential_status'], 'INVALID')

    def test_incomplete_duplicate_and_contradictory_responses_are_not_negative(self):
        for mutate in (lambda v: v.update(results=[]),
                       lambda v: v['results'].append(v['results'][0]),
                       lambda v: v['results'][0].update(validation_state='invalid'),
                       lambda v: v.update(object='unknown'),
                       lambda v: v['results'][1].update(outcome='unknown')):
            payload = image_response()
            mutate(payload)
            with self.subTest(payload=payload), self.assertRaises(ValueError):
                verifier.normalize_openai(payload, ('c2pa', 'synthid'))

    def test_upload_and_credentials_require_explicit_selection(self):
        def forbidden(*args):
            raise AssertionError('Unexpected network call')
        with patch.dict(os.environ, {'OPENAI_API_KEY': 'synthetic-secret'}):
            for suffix, allowed, dry in (('.png', False, False), ('.png', True, True),
                                          ('.docx', True, False), ('.txt', True, False)):
                report = verifier.openai_check(b'example', suffix, allowed, dry, transport=forbidden)
                self.assertIn(report['status'], ('NOT TESTED', 'UNAVAILABLE'))
        with patch.dict(os.environ, {}, clear=True):
            self.assertEqual(verifier.openai_check(b'example', '.png', True,
                                                   transport=forbidden)['status'], 'UNAVAILABLE')

    def test_multipart_is_one_file_no_local_path_and_secrets_are_redacted(self):
        def transport(body, media_type, key, timeout):
            self.assertIn(b'name="file"', body)
            self.assertEqual(body.count(b'Content-Disposition:'), 1)
            self.assertIn(b'filename="asset.png"', body)
            self.assertIn(b'Content-Type: image/png', body)
            self.assertIn('boundary=', media_type)
            self.assertEqual(key, 'synthetic-secret')
            response = image_response()
            response['results'][0]['issuer'] = key
            return response
        with patch.dict(os.environ, {'OPENAI_API_KEY': 'synthetic-secret'}):
            report = verifier.openai_check(b'example', '.png', True, transport=transport)
        self.assertEqual(report['status'], 'COMPLETED')
        self.assertNotIn('synthetic-secret', json.dumps(report))

    def test_access_rate_limit_and_http_failures_are_not_absence(self):
        for code in (400, 401, 403, 404, 429, 500, 302):
            def transport(*args):
                raise urllib.error.HTTPError(verifier.ENDPOINT, code, 'secret error', None, None)
            with patch.dict(os.environ, {'OPENAI_API_KEY': 'synthetic-secret'}):
                report = verifier.openai_check(b'example', '.png', True, transport=transport)
            self.assertIn(report['status'], ('UNAVAILABLE', 'UNKNOWN'))
            self.assertEqual(report['http_status'], code)
            self.assertNotIn('secret error', json.dumps(report))
        handler = verifier.NoRedirect()
        self.assertIsNone(handler.redirect_request(None, None, 302, '', {}, 'https://example.com'))

    def test_transport_and_schema_failure_preserve_unknown_status(self):
        for failure in (urllib.error.URLError('sensitive message'), TimeoutError()):
            def transport(*args):
                raise failure
            with patch.dict(os.environ, {'OPENAI_API_KEY': 'synthetic-secret'}):
                self.assertEqual(verifier.openai_check(b'x', '.png', True,
                                                       transport=transport)['status'], 'UNKNOWN')
        with patch.dict(os.environ, {'OPENAI_API_KEY': 'synthetic-secret'}):
            self.assertEqual(verifier.openai_check(b'x', '.png', True,
                                                   transport=lambda *a: {})['status'], 'UNKNOWN')

    def test_supported_audio_is_not_a_c2pa_check(self):
        with patch.dict(os.environ, {'OPENAI_API_KEY': 'synthetic-secret'}):
            report = verifier.openai_check(b'example', '.mp3', True, transport=lambda *args: {
                'object': 'content_provenance_check', 'results': [{'type': 'synthid', 'outcome': 'detected'}]})
        self.assertEqual(len(report['checks']), 1)
        self.assertEqual(report['checks'][0]['scheme'], 'synthid')
        self.assertEqual(report['audio_duration_check'], 'server validation required for decoded audio duration')

    def test_wav_too_long_is_never_sent(self):
        data = io.BytesIO()
        with wave.open(data, 'wb') as audio:
            audio.setnchannels(1)
            audio.setsampwidth(1)
            audio.setframerate(100)
            audio.writeframes(b'\0' * 6100)
        report = verifier.openai_check(data.getvalue(), '.wav', True,
                                      transport=lambda *a: self.fail('Upload occurred'))
        self.assertEqual(report['status'], 'NOT TESTED')

    def fake_run(self, payload=None, diagnostic='', code=0):
        def run(command, **kwargs):
            if command[-1] == '--version':
                return subprocess.CompletedProcess(command, 0, 'c2patool synthetic\n', '')
            root = Path(kwargs['cwd'])
            self.assertEqual((root / 'asset.png').read_bytes(), b'original')
            self.assertEqual(kwargs['env'].get('C2PATOOL_SETTINGS'), None)
            self.assertFalse(any(arg in command for arg in ('-m', '--manifest', '-o', '--output')))
            settings = (root / 'offline.toml').read_text()
            self.assertIn('allowed_network_hosts = []', settings)
            self.assertIn('remote_manifest_fetch = false', settings)
            kwargs['stdout'].write(json.dumps(payload).encode() if payload is not None else b'')
            kwargs['stderr'].write(diagnostic.encode())
            return subprocess.CompletedProcess(command, code)
        return run

    def test_local_states_and_private_temp_copy_without_inherited_settings(self):
        for state, status in (('Valid', 'SIGNAL PRESENT'), ('Trusted', 'SIGNAL PRESENT'), ('Invalid', 'INVALID')):
            with patch.object(verifier.shutil, 'which', return_value='/trusted/c2patool'), \
                 patch.dict(os.environ, {'C2PATOOL_SETTINGS': '/outside/config'}), \
                 patch.object(verifier.subprocess, 'run', side_effect=self.fake_run({'validation_state': state})):
                report = verifier.c2pa_check(b'original', '.png')
            self.assertEqual(report['status'], status)
            self.assertEqual(report['tool_version'], 'c2patool synthetic')

    def test_no_manifest_differs_from_bad_output_and_missing_tool(self):
        for diagnostic, expected in (('Error: No claim found\n', 'NOT FOUND IN THIS CHECK'),
                                     ('Failed to read file', 'UNKNOWN')):
            with patch.object(verifier.shutil, 'which', return_value='/trusted/tool'), \
                 patch.object(verifier.subprocess, 'run', side_effect=self.fake_run(diagnostic=diagnostic, code=1)):
                self.assertEqual(verifier.c2pa_check(b'original', '.png')['status'], expected)
        with patch.object(verifier.shutil, 'which', return_value=None):
            self.assertEqual(verifier.c2pa_check(b'original', '.png')['status'], 'UNAVAILABLE')

    def test_local_timeout_and_nonzero_are_not_validity(self):
        with patch.object(verifier.shutil, 'which', return_value='/trusted/tool'), \
             patch.object(verifier.subprocess, 'run', side_effect=subprocess.TimeoutExpired('tool', 1)):
            self.assertEqual(verifier.c2pa_check(b'x', '.png')['status'], 'UNKNOWN')
        with patch.object(verifier.shutil, 'which', return_value='/trusted/tool'), \
             patch.object(verifier.subprocess, 'run', side_effect=self.fake_run({'validation_state': 'Valid'}, code=1)):
            self.assertEqual(verifier.c2pa_check(b'original', '.png')['status'], 'UNKNOWN')

    def test_unreadable_trust_policy_stops_before_executable(self):
        with patch.object(verifier.shutil, 'which', return_value='/trusted/tool'), \
             patch.object(verifier, 'read_file', side_effect=ValueError('bad trust file')), \
             patch.object(verifier.subprocess, 'run', side_effect=AssertionError('Unexpected execution')):
            self.assertEqual(verifier.c2pa_check(b'x', '.png', trust_anchors='missing.pem')['status'], 'NOT TESTED')

    def test_staging_permission_failure_still_returns_a_structured_check(self):
        with patch.object(verifier.shutil, 'which', return_value='/trusted/tool'), \
             patch.object(verifier.tempfile, 'TemporaryDirectory', side_effect=PermissionError('private path')), \
             patch.object(verifier.subprocess, 'run', side_effect=AssertionError('Unexpected execution')):
            report = verifier.c2pa_check(b'x', '.png')
        self.assertEqual(report['status'], 'UNKNOWN')
        self.assertNotIn('private path', json.dumps(report))

    def test_cli_preserves_originals_and_refuses_report_collisions_before_network(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / 'private-name.png'
            source.write_bytes(b'original')
            report = root / 'audit.json'
            command = [sys.executable, str(SCRIPT), 'openai-media', str(source), '--dry-run', '--report', str(report)]
            run = subprocess.run(command, capture_output=True, text=True)
            self.assertEqual(run.returncode, 2)
            audit = json.loads(report.read_text())
            self.assertEqual(audit['sha256'], hashlib.sha256(b'original').hexdigest())
            self.assertEqual(audit['check']['status'], 'NOT TESTED')
            previous = report.read_bytes()
            run = subprocess.run(command, capture_output=True, text=True)
            self.assertEqual(run.returncode, 2)
            self.assertEqual(report.read_bytes(), previous)
            self.assertEqual(source.read_bytes(), b'original')


if __name__ == '__main__':
    unittest.main()
