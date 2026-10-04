#!/usr/bin/env python3
"""Bounded provenance checks. No detector-score rewriting or automatic uploads."""
import argparse
from datetime import datetime, timezone
import hashlib
import io
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import urllib.error
import urllib.request
import uuid
import wave

ENDPOINT = 'https://api.openai.com/v1/content_provenance_checks'
MAX_FILE = 50 * 1024 * 1024
MAX_RESPONSE = 8 * 1024 * 1024
MEDIA = {'.png': 'image/png', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg',
         '.webp': 'image/webp', '.mp3': 'audio/mpeg', '.opus': 'audio/ogg',
         '.aac': 'audio/aac', '.flac': 'audio/flac', '.wav': 'audio/wav',
         '.pcm': 'audio/pcm'}
LIMIT = ('Results apply only to this file and check. They cannot establish human '
         'authorship, factual truth or absence of AI involvement.')
OFFLINE_SETTINGS = ('[core]\nallowed_network_hosts = []\n'
                    '[verify]\nverify_after_reading = true\nverify_trust = true\n'
                    'verify_timestamp_trust = true\nocsp_fetch = false\n'
                    'remote_manifest_fetch = false\n')


def result(status, reason, **fields):
    return dict(status=status, reason=reason, **fields)


def read_file(path):
    path = Path(path)
    if not path.is_file():
        raise ValueError('Input must be an existing regular file.')
    with path.open('rb') as stream:
        data = stream.read(MAX_FILE + 1)
    if not data or len(data) > MAX_FILE:
        raise ValueError('Input must contain 1 byte to 50 MiB.')
    return data


def normalize_c2pa(payload):
    if not isinstance(payload, dict):
        return result('UNKNOWN', 'Unrecognized C2PA report schema.')
    state = payload.get('validation_state')
    if isinstance(state, str) and state.lower() in ('trusted', 'valid', 'invalid'):
        state = state.lower()
        return result('INVALID' if state == 'invalid' else 'SIGNAL PRESENT',
                      'Validator-reported manifest state; not an AI-authorship verdict.',
                      validation_state=state)
    # No state in older CLI reports: preserve diagnostics without inventing validity.
    return result('UNKNOWN', 'No recognized validator state; inspect raw diagnostics.')


def c2pa_check(data, suffix, executable='c2patool', trust_anchors=None, timeout=45):
    try:
        return _c2pa_check(data, suffix, executable, trust_anchors, timeout)
    except OSError:
        return result('UNKNOWN', 'Local C2PA staging or file operation failed; no validity conclusion.')


def _c2pa_check(data, suffix, executable, trust_anchors, timeout):
    tool = shutil.which(executable)
    if not tool:
        return result('UNAVAILABLE', 'c2patool executable not found.')
    with tempfile.TemporaryDirectory(prefix='galileo-c2pa-') as directory:
        root = Path(directory)
        asset = root / ('asset' + suffix)
        asset.write_bytes(data)
        settings = root / 'offline.toml'
        settings.write_text(OFFLINE_SETTINGS, encoding='utf-8')
        command = [tool, str(asset), '--settings', str(settings)]
        trust = {'policy': 'tool defaults; no supplied trust list'}
        if trust_anchors:
            try:
                pem = read_file(trust_anchors)
            except (ValueError, OSError):
                return result('NOT TESTED', 'Supplied local trust list is missing, unreadable or outside the size limit.')
            local_pem = root / 'trust.pem'
            local_pem.write_bytes(pem)
            identifier = 'urn:sha256:' + hashlib.sha256(pem).hexdigest()
            command += ['trust', '--trust_anchors', str(local_pem),
                        '--trust_list_uri', identifier]
            trust = {'policy': 'supplied local PEM', 'sha256': identifier[11:]}
        # Exclude inherited C2PA configuration; never overwrite user preferences.
        environment = {k: v for k, v in os.environ.items() if not k.startswith('C2PA')}
        try:
            version = subprocess.run([tool, '--version'], capture_output=True, text=True,
                                     timeout=timeout, env=environment, cwd=root)
            with tempfile.TemporaryFile() as output, tempfile.TemporaryFile() as errors:
                completed = subprocess.run(command, stdout=output, stderr=errors,
                                           timeout=timeout, env=environment, cwd=root)
                output.seek(0)
                raw = output.read(MAX_RESPONSE + 1)
                errors.seek(0)
                diagnostic = errors.read(MAX_RESPONSE + 1).decode('utf-8', 'replace')
        except subprocess.TimeoutExpired:
            return result('UNKNOWN', 'C2PA check timed out.')
        except OSError:
            return result('UNAVAILABLE', 'C2PA executable could not run.')
        metadata = {'tool_version': version.stdout.strip()[:300], 'exit_code': completed.returncode,
                    'trust_policy': trust, 'network_policy': 'remote fetch and OCSP disabled; host allowlist empty',
                    'coverage': 'copied asset only; adjacent sidecars and remote credentials not resolved'}
        if len(raw) > MAX_RESPONSE or len(diagnostic.encode()) > MAX_RESPONSE:
            return result('UNKNOWN', 'C2PA output exceeded the report limit.', **metadata)
        try:
            payload = json.loads(raw)
        except (ValueError, UnicodeError):
            # Exact CLI diagnostic, not a fuzzy search for a c2pa byte/string.
            if completed.returncode != 0 and diagnostic.strip() in ('Error: No claim found', 'Error: JumbfNotFound'):
                return result('NOT FOUND IN THIS CHECK', 'No embedded manifest found by the validator; remote/sidecar credentials untested.',
                              raw_diagnostic=diagnostic, **metadata)
            return result('UNKNOWN', 'C2PA returned no readable JSON report.',
                          raw_diagnostic=diagnostic, **metadata)
        normalized = normalize_c2pa(payload)
        if completed.returncode != 0 and normalized['status'] != 'INVALID':
            normalized = result('UNKNOWN', 'C2PA command failed; inspect raw diagnostics.')
        return dict(normalized, raw_result=payload, raw_diagnostic=diagnostic, **metadata)


def normalize_openai(payload, expected):
    if not isinstance(payload, dict) or payload.get('object') != 'content_provenance_check':
        raise ValueError('Unrecognized official response object.')
    checks = payload.get('results')
    if not isinstance(checks, list):
        raise ValueError('Official response requires a results array.')
    found = {}
    for entry in checks:
        if not isinstance(entry, dict):
            raise ValueError('Malformed result entry.')
        scheme = entry.get('type')
        if scheme not in expected or scheme in found:
            raise ValueError('Unexpected or duplicate result type.')
        outcome = entry.get('outcome')
        if outcome not in ('detected', 'not_detected'):
            raise ValueError('Unrecognized result outcome.')
        item = result('SIGNAL PRESENT' if outcome == 'detected' else 'NOT FOUND IN THIS CHECK',
                      'Supported OpenAI signal only; negative results do not rule out AI.',
                      scheme=scheme, outcome=outcome)
        if scheme == 'c2pa':
            state = entry.get('validation_state')
            if state not in ('trusted', 'valid', 'invalid', 'not_present'):
                raise ValueError('Unrecognized C2PA validation state.')
            if outcome == 'detected' and state not in ('trusted', 'valid'):
                raise ValueError('Inconsistent C2PA detection/state.')
            item['validation_state'] = state
            item['credential_status'] = ('INVALID' if state == 'invalid' else
                                         'NOT FOUND IN THIS CHECK' if state == 'not_present' else 'SIGNAL PRESENT')
            # Non-OpenAI credentials can exist with outcome=not_detected.
            item['reason'] = 'OpenAI AI-generation signal and credential validity are separate fields.'
        found[scheme] = item
    if set(found) != set(expected):
        raise ValueError('Applicable result missing; not a negative check.')
    return list(found.values())


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def post_official(body, content_type, key, timeout):
    request = urllib.request.Request(ENDPOINT, data=body, method='POST',
                                    headers={'Authorization': 'Bearer ' + key,
                                             'Content-Type': content_type})
    opener = urllib.request.build_opener(NoRedirect())
    with opener.open(request, timeout=timeout) as response:
        data = response.read(MAX_RESPONSE + 1)
    if len(data) > MAX_RESPONSE:
        raise ValueError('Official response exceeded the report limit.')
    return json.loads(data)


def redact(value, secret):
    if isinstance(value, str):
        return value.replace(secret, '[REDACTED]')
    if isinstance(value, list):
        return [redact(v, secret) for v in value]
    if isinstance(value, dict):
        return {redact(k, secret): redact(v, secret) for k, v in value.items()}
    return value


def openai_check(data, suffix, allow_upload=False, dry_run=False, timeout=45, transport=None):
    media = MEDIA.get(suffix.lower())
    if not media:
        return result('UNAVAILABLE', 'Official media verification does not support this format or manuscript text.')
    if not data or len(data) > MAX_FILE:
        return result('NOT TESTED', 'File outside the official 1-byte to 50-MiB limit.')
    duration = 'server validation required for decoded audio duration'
    if suffix.lower() == '.wav':
        try:
            with wave.open(io.BytesIO(data), 'rb') as audio:
                seconds = audio.getnframes() / audio.getframerate()
            if seconds > 60:
                return result('NOT TESTED', 'WAV duration exceeds the official 60-second limit.')
            duration = {'seconds': seconds, 'method': 'Python wave; PCM WAV only'}
        except (wave.Error, EOFError, ZeroDivisionError):
            return result('NOT TESTED', 'WAV could not be locally decoded; file not uploaded.')
    plan = {'endpoint': ENDPOINT, 'media_type': media, 'audio_duration_check': duration if media.startswith('audio/') else 'not applicable',
            'zero_data_retention_eligible': False, 'automatic_retries': 0}
    if dry_run:
        return result('NOT TESTED', 'Dry run; no credentials read and no upload.', **plan)
    if not allow_upload:
        return result('NOT TESTED', 'Remote verification requires explicit --allow-upload authorization.', **plan)
    key = os.environ.get('OPENAI_API_KEY')
    if not key:
        return result('UNAVAILABLE', 'OPENAI_API_KEY is not configured.', **plan)
    boundary = 'galileo-' + uuid.uuid4().hex
    # Neutral filename: do not send the author's path/name or extra multipart fields.
    prefix = (f'--{boundary}\r\nContent-Disposition: form-data; name="file"; '
              f'filename="asset{suffix.lower()}"\r\nContent-Type: {media}\r\n\r\n').encode()
    body = prefix + data + f'\r\n--{boundary}--\r\n'.encode()
    try:
        payload = (transport or post_official)(body, 'multipart/form-data; boundary=' + boundary, key, timeout)
        payload = redact(payload, key)
        expected = ('c2pa', 'synthid') if media.startswith('image/') else ('synthid',)
        checks = normalize_openai(payload, expected)
        return result('COMPLETED', 'Read each scheme result independently.', checks=checks,
                      raw_result=payload, **plan)
    except urllib.error.HTTPError as error:
        status = 'UNAVAILABLE' if error.code in (401, 403, 404, 429) else 'UNKNOWN'
        reason = {400: 'Unsupported, malformed or blocked file.', 401: 'Authentication unavailable.',
                  403: 'Access forbidden.', 404: 'Organization access or endpoint unavailable.',
                  429: 'Rate limit reached; no retry performed.'}.get(error.code, 'HTTP request failed; no retry performed.')
        return result(status, reason, http_status=error.code, **plan)
    except (urllib.error.URLError, TimeoutError, OSError):
        return result('UNKNOWN', 'Network/transport failure; no result and no retry.', **plan)
    except (ValueError, TypeError, UnicodeError):
        return result('UNKNOWN', 'Malformed or incompatible official response; no negative conclusion.', **plan)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('mode', choices=('c2pa', 'openai-media'))
    parser.add_argument('file', type=Path)
    parser.add_argument('--report', type=Path, help='New JSON report; existing files are never overwritten')
    parser.add_argument('--c2patool', default='c2patool', help='Trusted installed executable or absolute path')
    parser.add_argument('--trust-anchors', type=Path, help='Existing local PEM trust list; no download')
    parser.add_argument('--allow-upload', action='store_true', help='Explicitly authorize sending this file to the official OpenAI API')
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args(argv)
    if args.mode == 'c2pa' and args.allow_upload:
        parser.error('--allow-upload is only used by openai-media')
    if args.mode != 'c2pa' and args.trust_anchors:
        parser.error('--trust-anchors is only used by c2pa')
    try:
        data = read_file(args.file)
        # Reserve output before any paid/network operation; never overwrite input.
        output = args.report.open('x', encoding='utf-8') if args.report else None
    except (ValueError, OSError) as error:
        parser.exit(2, f'Cannot inspect input/create new report: {type(error).__name__}.\n')
    try:
        if args.mode == 'c2pa':
            check = result('NOT TESTED', 'Dry run; executable not launched.') if args.dry_run else c2pa_check(
                data, args.file.suffix, args.c2patool, args.trust_anchors)
        else:
            check = openai_check(data, args.file.suffix, args.allow_upload, args.dry_run)
        report = {'schema_version': 1, 'checked_at': datetime.now(timezone.utc).isoformat(),
                  'file': args.file.name, 'sha256': hashlib.sha256(data).hexdigest(),
                  'size_bytes': len(data), 'mode': args.mode, 'check': check, 'limitations': LIMIT}
        text = json.dumps(report, indent=2, ensure_ascii=False) + '\n'
        if output:
            output.write(text)
        else:
            print(text, end='')
        return 0 if check['status'] in ('COMPLETED', 'SIGNAL PRESENT', 'NOT FOUND IN THIS CHECK') else 2
    finally:
        if output:
            output.close()


if __name__ == '__main__':
    raise SystemExit(main())
