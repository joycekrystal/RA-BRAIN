# Repository instructions

Read `docs/RELEASING.md` before changing this plugin. Record every change in
`docs/CHANGELOG.md` with its date and impact. Before merging any change to `main`,
bump all three plugin manifests together according to the highest semantic
impact in the change set and run the release validation and tests. This applies
to documentation, tooling and CI changes too. Classify by compatibility and
behavior, not line count. Never edit an already published version in place.

Keep `skills/` canonical and preserve the existing plugin identity. Do not
publish, push, merge or change repository protection settings unless requested.

Every skill update must preserve compatibility with Claude Code, Codex and
Antigravity. Follow the compatibility review in `docs/RELEASING.md`: retain
portable SKILL.md metadata, existing workflows and reference paths, and keep
host-specific capabilities optional with documented fallbacks. A major version
bump alone does not authorize dropping support for an assistant.
