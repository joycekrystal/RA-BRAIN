#!/usr/bin/env python3
"""Validate the next normal release against a Git target revision."""
import argparse
from datetime import date
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
MANIFESTS = ('plugin.json', '.codex-plugin/plugin.json', '.claude-plugin/plugin.json')


def version(value):
    if not isinstance(value, str) or not re.fullmatch(r'(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)', value):
        raise ValueError(f'Expected normal MAJOR.MINOR.PATCH version: {value!r}')
    return tuple(map(int, value.split('.')))


def validate(base_manifest, manifests, old_log, log, readme):
    current = manifests[0]['version']
    new = version(current)
    old = version(base_manifest['version'])
    for manifest in manifests:
        if manifest.get('name') != base_manifest['name'] or manifest.get('version') != current:
            raise ValueError('All three manifests must preserve the name and have the same version')
    if f'Version: {current}' not in readme.splitlines():
        raise ValueError('README version must match the manifests')
    entries = re.split(r'(?m)^## ', log)
    if len(entries) < 2:
        raise ValueError('Missing release entry')
    heading, _, body = entries[1].partition('\n')
    match = re.fullmatch(re.escape(current) + r' — (\d{4}-\d{2}-\d{2})', heading)
    if not match:
        raise ValueError('First changelog entry must match the version and include an ISO date')
    date.fromisoformat(match[1])
    impact = re.findall(r'^Release type: (patch|minor|major)$', body, re.M)
    if len(impact) != 1 or not re.search(r'^Rationale: \S.+', body, re.M):
        raise ValueError('Specify one Release type and a Rationale in the current entry')
    expected = {'patch': (old[0], old[1], old[2]+1),
                'minor': (old[0], old[1]+1, 0),
                'major': (old[0]+1, 0, 0)}[impact[0]]
    if new != expected:
        raise ValueError(f'{impact[0]} bump from {base_manifest["version"]} requires {".".join(map(str, expected))}')
    bullets = re.findall(r'^- (.+)$', body, re.M)
    if not bullets or any(not re.match(r'\d{4}-\d{2}-\d{2}: \S', item) for item in bullets):
        raise ValueError('Every change bullet must start with YYYY-MM-DD: and describe the change')
    for item in bullets:
        date.fromisoformat(item[:10])
    old_entries = old_log[old_log.find('\n## '):] if '\n## ' in old_log else ''
    if old_entries and not log.endswith(old_entries):
        raise ValueError('Preserve existing changelog entries unchanged after the new entry')
    return f'{base_manifest["version"]} → {current} ({impact[0]})'


def git_text(base, path):
    return subprocess.check_output(['git', 'show', f'{base}:{path}'], cwd=ROOT, text=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--base', required=True, help='Fetched target branch or target commit')
    args = parser.parse_args()
    try:
        # Resolve the revision first so arbitrary input cannot become a git option.
        base = subprocess.check_output(['git', 'rev-parse', '--verify', '--end-of-options',
                                        args.base + '^{commit}'], cwd=ROOT, text=True).strip()
        base_manifest = json.loads(git_text(base, 'plugin.json'))
        exists = subprocess.run(['git', 'cat-file', '-e', f'{base}:docs/CHANGELOG.md'],
                                cwd=ROOT, capture_output=True).returncode == 0
        old_log = git_text(base, 'docs/CHANGELOG.md') if exists else ''
        result = validate(base_manifest,
                          [json.loads((ROOT / p).read_text()) for p in MANIFESTS],
                          old_log, (ROOT / 'docs/CHANGELOG.md').read_text(),
                          (ROOT / 'README.md').read_text())
        print(f'Release policy passed: {result}')
    except (ValueError, KeyError, OSError, subprocess.CalledProcessError) as error:
        print(f'Release policy failed: {error}', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
