# Release notes

## 0.3.0 — 2026-10-31

Release type: minor
Rationale: Add an explicit canonical application knowledge-base creation/update workflow and reusable source-of-truth index while retaining existing skill inputs, outputs and assistant support.

- 2026-10-31: Extend knowledge-maintenance with canonical concern indexing, durable user-decision capture, explicit supersession and scoped evidence coverage.
- 2026-10-31: Add a packaged knowledge-base reference and shared index template, with guarded publication and saved-content verification guidance.
- 2026-10-31: Update usage documentation and handoff while preserving existing drift-review prompts and Claude Code, Codex and Antigravity layouts.

## 0.2.3 — 2026-10-31

Release type: patch
Rationale: Make the existing MCP access-recovery workflow actionable with referenced setup instructions; existing skill inputs, outputs and supported assistants are unchanged.

- 2026-10-31: Add a shared Atlassian MCP connection guide covering plugin setup, Codex CLI, Claude Code, portable host setup, permission troubleshooting and read-only verification.
- 2026-10-31: Require every skill to reference the guide and provide host-appropriate steps when Jira/Confluence access fails; link the guide from user documentation.

## 0.2.2 — 2026-10-31

Release type: patch
Rationale: Clarify existing cross-assistant compatibility guarantees without changing skill inputs or outputs.

- 2026-10-31: Require backward-compatible skill updates across Claude Code, Codex and Antigravity, with portable fallbacks and explicit per-host verification limits.

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
