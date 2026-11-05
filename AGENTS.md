# Business to Build — repository instructions

## Project context

This repository contains the reusable Business to Build skills plugin for Claude
Code, Codex and Antigravity. It provides workflow instructions, shared references
and installation tooling; it is not a hosted application or MCP server.

Before editing, inspect `git status --short` and read `README.md`,
`docs/AGENT_HANDOFF.md` and the files relevant to the task. Preserve unrelated
local changes. Read a skill's `SKILL.md` and linked references before changing
its workflow.

## Repository map

- `skills/`: canonical definitions for the six skills and their support files.
- `skills/delivery-standards/references/`: shared rules, templates and Atlassian
  connection guidance used by the skills.
- `plugin.json`, `.codex-plugin/plugin.json`, `.claude-plugin/plugin.json`:
  manifests for the existing plugin and host integrations.
- `scripts/install_skills.py`: workspace installer; preserve its conflict and
  symlink protections.
- `scripts/validate_release.py` and `tests/`: release validation and Python tests.
- `docs/USAGE_GUIDE.md` and `docs/COMPATIBILITY.md`: workflow and installation
  documentation; keep them aligned with behavior changes.

## Release rules

Read `docs/RELEASING.md` before changing this plugin. Record every change in
`docs/CHANGELOG.md` with its date and impact. Before merging any change to `main`,
bump all three plugin manifests together according to the highest semantic
impact in the change set and run the release validation and tests. This applies
to documentation, tooling and CI changes too. Classify by compatibility and
behavior, not line count. Never edit an already published version in place.

Keep `skills/` canonical and preserve the existing plugin identity. Do not
publish, push, merge or change repository protection settings unless requested.

Keep the README version synchronized with all three manifests. Follow the
release policy for the exact next version, dated release entries and preservation
of existing history. Source changes do not publish the private plugin.

## Cross-assistant compatibility

Every skill update must preserve compatibility with Claude Code, Codex and
Antigravity. Follow the compatibility review in `docs/RELEASING.md`: retain
portable SKILL.md metadata, existing workflows and reference paths, and keep
host-specific capabilities optional with documented fallbacks. A major version
bump alone does not authorize dropping support for an assistant.

Do not edit installed copies as a substitute for changing canonical `skills/`.
Keep support files inside the packaged skill tree when installed workflows need
them. Distinguish static validation from actual activation and workflow checks
on each assistant; report unavailable host checks as unverified.

## Scope and integrations

Keep reusable standards separate from application-specific business rules and
implementation facts. Store new application knowledge in the target application
repository or selected Confluence space. Do not infer an application's stack
from this plugin repository.

Discover available Jira, Confluence, Figma and PR-hosting tools before relying on
them. Credentials and provider authentication belong to those integrations;
never embed them here. Follow the shared connection guide when linked sources
cannot be read, and mark dependent findings as unverified until access succeeds.
External writes must stay within the user's authorized scope.

## Validation and handoff

Run the existing test suite for repository changes:

```sh
python3 -B -m unittest discover -s tests -v
```

Before merging, fetch the latest `origin/main` and validate the full change set:

```sh
git fetch origin main
python3 scripts/validate_release.py --base origin/main
```

For installer changes, also review a dry run against a disposable workspace:

```sh
python3 scripts/install_skills.py --target /absolute/path/to/workspace --dry-run
```

Report what changed, the checks actually run and any remaining verification
limits. Do not claim publication, provider access, runtime compatibility or
repository protection based only on source files or passing unit tests.
