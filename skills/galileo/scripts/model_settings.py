#!/usr/bin/env python3
"""Offline model preferences: guided setup, validation and safe local persistence."""
import argparse
import json
import os
import sys
import tempfile
from pathlib import Path

FILENAME = 'galileo-models.json'
ALIASES = ('economical', 'balanced', 'frontier')
HARNESSES = ('codex', 'claude-code', 'opencode', 'copilot', 'other')
PROFILES = ('economy', 'balanced', 'quality')
ROLES = {
    'coordinator': 'Coordination and integration',
    'evidence': 'Literature and bibliography',
    'measurement_data': 'Measurement, scoring and data',
    'methodologist': 'Methods and analysis planning',
    'writer': 'Scientific writing',
    'figures': 'Scientific figures',
    'verifier': 'Source and consistency checks',
    'reviewer_domain': 'Domain reviewer',
    'reviewer_methods': 'Methods/statistics reviewer',
    'reviewer_technical': 'Measurement/technical reviewer',
    'editorial_secretary': 'File and format checks',
    'handling_editor': 'Simulated editorial decision',
    'copyeditor': 'Language and terminology',
    'presentation_designer': 'Slide design',
    'typesetter': 'Word/LaTeX production',
    'systematic_screener': 'Systematic-review screening',
    'defense_examiner': 'Defense rehearsal',
}


def defaults(harness='other'):
    return {
        'schema_version': 1,
        'harness': harness,
        'configuration_status': 'deferred',
        'available_models': [],
        'inventory_source': 'not_supplied',
        'provider_model_mapping': dict.fromkeys(ALIASES),
        'role_overrides': {},
        'cost_profile': 'balanced',
        'unavailable_model_policy': 'ask',
        'routing_status': 'preferences_only',
    }


def _identifier(value):
    return isinstance(value, str) and bool(value.strip()) and value == value.strip() and len(value) <= 200 and all(ord(c) >= 32 and ord(c) != 127 for c in value)


def validate(settings):
    if not isinstance(settings, dict) or set(settings) != set(defaults()):
        raise ValueError('Model settings must use the documented schema; unknown/missing fields are rejected')
    if type(settings['schema_version']) is not int or settings['schema_version'] != 1:
        raise ValueError('Unsupported model-settings schema version')
    if settings['harness'] not in HARNESSES:
        raise ValueError('Unknown harness')
    if settings['configuration_status'] not in ('deferred', 'configured'):
        raise ValueError('Invalid configuration status')
    inventory = settings['available_models']
    if not isinstance(inventory, list) or not all(_identifier(m) for m in inventory) or len(inventory) != len(set(inventory)):
        raise ValueError('Available models must be unique, nonempty identifiers')
    if settings['inventory_source'] not in ('not_supplied', 'user_supplied', 'provided_file'):
        raise ValueError('Invalid inventory source')
    if (settings['inventory_source'] == 'not_supplied') != (not inventory):
        raise ValueError('Inventory source must match the supplied model list')
    mapping = settings['provider_model_mapping']
    if not isinstance(mapping, dict) or set(mapping) != set(ALIASES):
        raise ValueError('Configure exactly economical, balanced and frontier aliases')
    overrides = settings['role_overrides']
    if not isinstance(overrides, dict) or not set(overrides) <= set(ROLES):
        raise ValueError('Unknown role override')
    for model in list(mapping.values()) + list(overrides.values()):
        if model is not None and (not isinstance(model, str) or model not in inventory):
            raise ValueError('Requested models must be in the supplied inventory; null means keep the current model')
    if settings['cost_profile'] not in PROFILES:
        raise ValueError('Invalid cost profile')
    if settings['unavailable_model_policy'] != 'ask' or settings['routing_status'] != 'preferences_only':
        raise ValueError('Settings cannot authorize automatic fallback or assert applied model routing')
    if settings['configuration_status'] == 'deferred' and (inventory or overrides or any(mapping.values())):
        raise ValueError('Deferred configuration cannot contain selected models')
    return settings


def load(path):
    return validate(json.loads(Path(path).read_text(encoding='utf-8')))


def load_inventory(path):
    value = json.loads(Path(path).read_text(encoding='utf-8'))
    if not isinstance(value, dict) or set(value) != {'harness', 'models'} or value['harness'] not in HARNESSES:
        raise ValueError('Inventory must contain harness and models only')
    models = value['models']
    if not isinstance(models, list) or not all(_identifier(m) for m in models) or len(models) != len(set(models)):
        raise ValueError('Invalid model inventory')
    return value


def infer_harness(destination):
    for folder, harness in (('.agents', 'codex'), ('.codex', 'codex'), ('.claude', 'claude-code'), ('.opencode', 'opencode'), ('.github', 'copilot')):
        if folder in Path(destination).parts:
            return harness
    return 'other'


def wizard(harness='other', inventory=None, input_fn=None, output_fn=None, existing=None):
    output = output_fn or (lambda line: print(line, file=sys.stderr))
    if existing is not None:
        existing = json.loads(json.dumps(validate(existing)))
    if input_fn is None:
        def input_fn(prompt):
            print(prompt, end='', file=sys.stderr, flush=True)
            return input()

    def choice(prompt, choices, default):
        while True:
            answer = input_fn(f'{prompt} [{default}]: ').strip() or default
            if answer in choices:
                return answer
            output('Choose one of: ' + ', '.join(choices))

    output('Galileo model setup. No network calls, client changes or paid API activation.')
    output('Model availability and routing will be checked by your assistant at runtime.')
    if choice('Configure now or later? (now/later)', ('now', 'later'), 'now') == 'later':
        return existing if existing is not None else defaults(harness)
    suggested = inventory['harness'] if inventory else (existing['harness'] if existing else harness)
    selected_harness = choice('Harness (' + ', '.join(HARNESSES) + ')', HARNESSES, suggested)
    if inventory and inventory['harness'] != selected_harness:
        raise ValueError('Inventory belongs to a different harness; provide a matching inventory')
    settings = defaults(selected_harness)
    settings['configuration_status'] = 'configured'
    if inventory:
        models = inventory['models']
        source = 'provided_file'
    else:
        output('Enter exact model IDs shown by your harness, separated by commas.')
        previous_models = existing['available_models'] if existing and existing['harness'] == selected_harness else []
        if previous_models:
            output('Enter keeps your previous inventory; 0 clears it to use the current model.')
        else:
            output('Leave blank to use the current harness model for all aliases.')
        while True:
            raw = input_fn('Available models' + (f' [{",".join(previous_models)}]' if previous_models else '') + ': ').strip()
            if not raw and previous_models:
                raw = ','.join(previous_models)
            if raw == '0':
                raw = ''
            models = [m.strip() for m in raw.split(',')] if raw else []
            if all(_identifier(m) for m in models) and len(models) == len(set(models)):
                break
            output('Use unique, nonempty model IDs without control characters.')
        source = 'user_supplied'
    settings['available_models'] = models
    settings['inventory_source'] = source if models else 'not_supplied'
    previous_settings = existing if existing and existing['harness'] == selected_harness else None
    if previous_settings:
        settings['role_overrides'] = {role: model for role, model in previous_settings['role_overrides'].items()
                                      if model is None or model in models}
        removed = set(previous_settings['role_overrides']) - set(settings['role_overrides'])
        if removed:
            output('Overrides removed from the proposed configuration because their models are absent: ' + ', '.join(sorted(removed)))
    output('0: keep the current harness model')
    for number, model in enumerate(models, 1):
        output(f'{number}: {model}')

    def select_model(prompt, default=None):
        default_number = str(models.index(default) + 1) if default in models else '0'
        while True:
            answer = input_fn(f'{prompt} [{default_number}]: ').strip() or default_number
            if answer == '0':
                return None
            if answer in models:
                return answer
            if answer.isdigit() and 1 <= int(answer) <= len(models):
                return models[int(answer) - 1]
            output('Choose a listed model number/ID, or 0 for the current model.')

    descriptions = {
        'economical': 'bounded language/file checks',
        'balanced': 'writing, evidence and coordination',
        'frontier': 'complex methods and unresolved scientific disputes',
    }
    previous = None
    if models:
        output('Aliases describe intended tasks, not verified model quality or price. The same model may fill all three.')
        for alias in ALIASES:
            default = previous_settings['provider_model_mapping'][alias] if previous_settings else previous
            if default is not None and default not in models:
                output(f'Previous {alias} model is not in the new inventory; choose again.')
                default = None
            previous = select_model(f'{alias} ({descriptions[alias]})', default)
            settings['provider_model_mapping'][alias] = previous
    output('economy: fewer repeated passes; balanced: standard role policy; quality: more intensive methods/conflict review.')
    output('Every profile retains evidence checks. Higher cost does not guarantee correctness.')
    settings['cost_profile'] = choice('Cost profile (economy/balanced/quality)', PROFILES,
                                      previous_settings['cost_profile'] if previous_settings else 'balanced')
    if models and choice('Advanced role overrides? (yes/no)', ('yes', 'no'), 'no') == 'yes':
        output('Role IDs: ' + ', '.join(ROLES))
        while True:
            role = input_fn('Role ID (prefix - to remove override; blank to finish): ').strip()
            if not role:
                break
            if role.startswith('-') and role[1:] in ROLES:
                settings['role_overrides'].pop(role[1:], None)
                continue
            if role not in ROLES:
                output('Unknown role ID; choose one from the list.')
                continue
            settings['role_overrides'][role] = select_model(ROLES[role], settings['role_overrides'].get(role))
    validate(settings)
    output('Preferences to save:\n' + json.dumps(settings, indent=2, ensure_ascii=False))
    if choice('Save these preferences? (yes/no)', ('yes', 'no'), 'yes') == 'no':
        raise ValueError('Setup cancelled; nothing installed or changed')
    return settings


def save(destination, settings, replace=False):
    """Atomically save; never overwrite by default, preserve a backup on replacement."""
    settings = validate(settings)
    destination = Path(destination).expanduser().resolve()
    destination.mkdir(parents=True, exist_ok=True)
    target = destination / FILENAME
    if target.is_symlink() or (target.exists() and not target.is_file()):
        raise ValueError('Refusing symlinked or non-file model settings')
    if target.exists() and not replace:
        raise FileExistsError(f'Refusing existing model settings: {target}; use explicit replacement after review')
    backup = None
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', prefix='.galileo-models-', suffix='.tmp', dir=destination, delete=False) as stream:
            temporary = Path(stream.name)
            stream.write(json.dumps(settings, indent=2, ensure_ascii=False) + '\n')
            stream.flush()
            os.fsync(stream.fileno())
        if replace and target.exists():
            with tempfile.NamedTemporaryFile(prefix='.galileo-models-backup-', suffix='.json', dir=destination, delete=False) as stream:
                backup = Path(stream.name)
                stream.write(target.read_bytes())
            os.replace(temporary, target)
        else:
            os.link(temporary, target)  # Atomic creation; refuses a concurrent collision.
        return {'path': str(target), 'backup': str(backup) if backup else None}
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dest', default=str(Path(__file__).resolve().parents[2]), help='Installed skill directory (inferred when run from an installed Galileo skill)')
    parser.add_argument('--settings-file', help='Import a validated preferences JSON instead of prompting')
    parser.add_argument('--available-models', help='Offline JSON with harness and models for guided setup')
    parser.add_argument('--replace', action='store_true', help='Explicitly replace existing preferences, keeping a backup')
    parser.add_argument('--dry-run', action='store_true', help='Validate/preview without prompting or writing')
    args = parser.parse_args()
    if args.settings_file and args.available_models:
        parser.error('--settings-file and --available-models are alternatives')
    try:
        target = Path(args.dest).expanduser().resolve() / FILENAME
        if target.is_symlink() or (target.exists() and not target.is_file()):
            raise ValueError('Refusing symlinked or non-file model settings')
        if target.exists() and not args.replace and not args.dry_run:
            raise FileExistsError('Existing preferences are preserved; use --replace to change them with a backup')
        inventory = load_inventory(args.available_models) if args.available_models else None
        if args.settings_file:
            settings = load(args.settings_file)
        elif args.dry_run:
            settings = load(target) if target.exists() else defaults(infer_harness(args.dest))
        else:
            if not sys.stdin.isatty():
                raise ValueError('Guided setup requires a terminal; use --settings-file for unattended configuration')
            settings = wizard(infer_harness(args.dest), inventory, existing=load(target) if target.exists() else None)
        if args.dry_run:
            print(json.dumps({'dry_run': True, 'settings': settings}, indent=2))
        else:
            print(json.dumps(save(args.dest, settings, replace=args.replace), indent=2))
    except (OSError, ValueError, EOFError, KeyboardInterrupt) as error:
        parser.exit(1, f'Model setup stopped: {error}\n')


if __name__ == '__main__':
    main()
