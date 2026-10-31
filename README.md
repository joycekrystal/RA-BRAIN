# codexskill

## Business to Build

A reusable skills package for Claude Code, Codex and Antigravity covering business modeling, feature documentation, design reviews, implementation and application knowledge maintenance. The existing private Codex plugin identity is preserved.

## Setup

For a workspace installation across all three assistants, run from this repository:

```sh
python3 scripts/install_skills.py --target /absolute/path/to/application --dry-run
python3 scripts/install_skills.py --target /absolute/path/to/application
```

See the [compatibility and installation guide](docs/COMPATIBILITY.md) for per-assistant options, Claude Code local plugin loading, update handling and verification limits. All six skills remain canonical under `skills/`.

Alternatively, retain the existing private Codex plugin installation. Separately configure supported Atlassian (Jira and Confluence), Figma and PR-hosting integrations in each assistant as needed. Provider authentication stays with those integrations. No MCP endpoints or credentials are embedded in this package. External read/write capability depends on available tools and permissions.

Start with: “Use Business to Build to onboard this repository and establish the application knowledge base.” Supply the repository and, when relevant, the Jira project, Confluence space and Figma file. Existing project conventions take precedence over generic suggestions.

Other prompts: “Create a business model and MVP brief”; “Specify feature ABC-123 with criterion-to-test traceability”; “Review this Figma flow against ABC-123”; “Implement ABC-123 using the approved specification”; “Review documentation drift for this feature.”

For frontend design checks: “Use design-review to review PR <URL> against Figma. Find the design references in the PR description and linked ticket, compare the frontend code and rendered UI where available, and report mismatches with design nodes, code locations and verification gaps.”

Application knowledge remains in repository files and/or Confluence; chat memory is not a database. This package provides reusable skills, not hosted storage or automatic synchronization. Future standards updates can be made to this same plugin; integrate further providers when required.

## Current private release

Version: 0.1.0

Plugin: https://chatgpt.com/plugins/plugins_6ae5e74e99bc819199d832480fcbb620

This repository is the source for future updates to the same plugin. Package the root manifest, `.claude-plugin/plugin.json`, skills, README and linked documentation as one plugin archive; exclude Git metadata, caches and unrelated development artifacts. Include the installer when distributing source for workspace setup. Repository compatibility changes do not publish a new private release.

## Usage guide

Read the [complete skill usage guide](docs/USAGE_GUIDE.md) for when to use each of the six skills, required context, copyable example prompts, expected outputs and a combined feature delivery workflow.

## Agent handoff

Read [the agent reference and handoff](docs/AGENT_HANDOFF.md) for project intent, repository structure, integration status, delivery standards and instructions for future updates.
