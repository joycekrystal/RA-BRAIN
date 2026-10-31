# Release notes

## 0.2.1 — 2026-10-31

Release type: patch
Rationale: Repository release governance and validation; no change to skill inputs, outputs or user workflows.

- 2026-10-31: Require dated change records and an impact-based semantic version bump before every merge to main, including documentation and tooling changes.
- 2026-10-31: Add synchronized manifest/README version validation, preservation of release history, PR checks and a review template.
- 2026-10-31: Add repository instructions for assistants and release-validator tests; document the separately configured required GitHub status check.

## 0.2.0 — 2026-10-31

- Extend design-review to discover Figma references from PR descriptions and linked tickets and compare frontend code and rendered UI with the design.
- Add Claude Code plugin metadata, a workspace installer for Claude Code, Codex and Antigravity, and assistant-neutral shared rules.
- Require an explicit provider MCP connection request when a linked source cannot be read, followed by a verified retry.
- Add complete skill usage and compatibility guides.
- Preserve the existing private plugin identity, presentation, default prompt and six skills. Provider authentication remains separate.

## 0.1.0

Initial private release with six workflow skills, shared rules and application knowledge templates.
