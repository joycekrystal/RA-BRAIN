# Assistant compatibility and installation

Business to Build keeps all six workflows in canonical `skills/<name>/SKILL.md` directories. Shared references stay under `delivery-standards/references`; always distribute all six directories together because the skills reference one another. The skill content is shared across assistants; discovery and integrations depend on the host.

## Quick setup for an application workspace

Requires Python 3. From this repository, run:

```sh
python3 scripts/install_skills.py --target /absolute/path/to/application --dry-run
python3 scripts/install_skills.py --target /absolute/path/to/application
```

The default installs all six skills into both `.agents/skills` (shared by Codex and current Antigravity) and `.claude/skills` (Claude Code). To install for selected assistants:

```sh
python3 scripts/install_skills.py --target /absolute/path/to/application --assistants codex antigravity
python3 scripts/install_skills.py --target /absolute/path/to/application --assistants claude
```

The installer copies references, deduplicates shared destinations, skips identical files and checks every destination for conflicts before writing. It refuses differing content and symlink destinations. It does not alter project instructions, settings, credentials or unrelated skills. Interrupted filesystem writes may leave a partial installation; rerun after inspecting any reported conflict. No Python packages are required.

Installed copies are snapshots. After source updates, use `--dry-run` to identify conflicts and manually reconcile the six installed skill directories with canonical source, preserving local changes. There is no force overwrite, automatic update or uninstall. To remove a snapshot, remove only the six directories installed by this package after checking for local edits; do not remove an entire shared skills directory.

Open the application workspace in the assistant and check its skill list; restart the session if necessary. Commit installed copies if your team wants workspace-scoped distribution. Avoid enabling both a plugin and workspace copy of these skills in the same assistant, which can create duplicate or ambiguous names.

## Host-specific options

| Assistant | Supported layout supplied here | How to use |
| --- | --- | --- |
| Codex | Existing root `plugin.json`, or copied `.agents/skills/<name>` | Retain the existing private plugin installation, or use the workspace installer. Ask to use `design-review` or another skill by name. |
| Claude Code | `.claude-plugin/plugin.json` with canonical root `skills/`, or copied `.claude/skills/<name>` | For a local plugin session, run `claude --plugin-dir /absolute/path/to/business-to-build` from your application workspace. Alternatively use the installer. |
| Antigravity | Copied `.agents/skills/<name>` | Use the installer, open the workspace, and request a skill by name. Current documentation covers this location for App, CLI and IDE. |

Claude Code plugin skills use namespaced invocation, for example `/business-to-build:design-review`; workspace skills use `/design-review`. Natural-language requests work as a common entry point. This repository does not register a Claude marketplace or publish an Antigravity plugin. Older Antigravity releases may use `.agent/skills`; if your release requires that layout, copy all six directories there instead of `.agents/skills`, preserving sibling references and avoiding duplicate installations.

## Same workflow across assistants

```text
Use the design-review skill from Business to Build to review PR <URL>.
Application repository: <path>. Read the PR description and linked ticket
to find the Figma nodes. Compare the frontend implementation with the
specified design, inspect the rendered UI where available, and report
findings with design nodes, code locations, evidence and remaining gaps.
```

Configure PR hosting, Jira/Confluence and Figma access separately in each assistant using its supported authenticated tooling. Browser comparison additionally requires a runnable application or accessible preview and browser tools. Missing capabilities must be reported as unverified checks. Skills do not grant permissions or transfer access between assistants. Keep application-specific documentation in the application repository or its selected canonical documentation system.

See the [usage guide](USAGE_GUIDE.md) for every skill's inputs and outputs.

For Jira/Confluence connection problems, follow the [Atlassian MCP setup and troubleshooting guide](../skills/delivery-standards/references/atlassian-mcp-setup.md). It includes the plugin-directory route, Codex CLI and Claude Code commands, portable remote MCP guidance, and a read-only verification prompt.

If a linked source cannot be accessed, the assistant should explain the failure and ask you to connect the relevant provider MCP server in the assistant you are using, or reconnect/authenticate an existing connection. For example: “Please connect the Atlassian MCP server with access to this Confluence space so I can read the Features page.” Missing links or page permissions may additionally require a corrected URL or access from the owner. Do not share credentials in chat. After connection, the assistant must retry the read before treating the source as verified.

## Verification and official references

Future skill updates must preserve existing workflows across Claude Code, Codex
and Antigravity. Host-specific features must remain optional with portable
fallbacks. Review metadata, reference paths, manifests and installer layouts
before merge, and record per-host checks and unverified behavior. See the
[release policy](RELEASING.md) for the required compatibility review. A version
bump does not itself authorize removing support for an assistant.

Source layouts follow the official documentation reviewed on 2026-10-31:

- [OpenAI: Build skills](https://learn.chatgpt.com/docs/build-skills) — Codex workspace discovery in `.agents/skills`.
- [Claude Code: Skills](https://code.claude.com/docs/en/skills) — `.claude/skills` and namespaced plugin skills.
- [Claude Code: Plugin manifest](https://code.claude.com/docs/en/plugins-reference) — `.claude-plugin/plugin.json` and root `skills/` layout.
- [Claude Code: Plugins](https://code.claude.com/docs/en/plugins) — local loading with `--plugin-dir`.
- [Google Antigravity: Agent skills](https://antigravity.google/docs/skills) — workspace discovery and legacy locations.

Installer tests check copying, repeat installs, reference preservation, conflict handling and symlink refusal. These checks and manifest validation do not prove that every assistant has loaded or executed the workflows. End-to-end skill activation and provider operations must be checked in each configured host; no live three-host integration test has been completed.
