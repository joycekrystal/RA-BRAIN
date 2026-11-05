# Create, update and use Business to Build

This repository is the source for the existing `business-to-build` plugin.
Its six skills can be distributed as a plugin or copied into an application
workspace. Copying skills does not install the account plugin or its integrations.

## Choose an installation

| Where you work | Route |
| --- | --- |
| Codex CLI | Local marketplace plugin, or workspace skills |
| Codex IDE extension in VS Code or a compatible editor | Workspace skills |
| Claude Code terminal | Local plugin session, or workspace skills |
| Claude Code IDE | Workspace skills; use the host's plugin manager for persistent plugins |
| Antigravity CLI or IDE | Workspace skills |
| Existing private ChatGPT/Codex plugin | Keep its existing identity and use the account update workflow |

The [official plugin documentation](https://learn.chatgpt.com/docs/plugins)
currently supports Codex CLI plugins, but excludes plugins from the Codex IDE
extension. Workspace skills are the portable route for this repository's IDE use.
Host behavior was reviewed on 2026-11-05; check your installed client's help if
commands differ.

## Quick start: Codex CLI and IDE through workspace skills

Requires Python 3, an existing application directory, and an installed,
authenticated Codex CLI or IDE extension. Run from this plugin repository;
replace the target with the application you want to work on:

```sh
python3 scripts/install_skills.py --target /absolute/path/to/application --assistants codex --dry-run
python3 scripts/install_skills.py --target /absolute/path/to/application --assistants codex
cd /absolute/path/to/application
codex
```

For IDE use, open that same application directory in your editor and start a
new Codex session. Use `/skills` or type `$` to select `delivery-standards`, then
ask it to onboard the application. See [OpenAI's skill guide](https://learn.chatgpt.com/docs/build-skills).

The installer copies all six sibling directories and support files into
`.agents/skills/`. It needs no Python dependencies. Do not copy just one skill:
shared relative references depend on the other directories.

## Codex CLI: install the full plugin locally

This is an alternative to workspace copies. Do not enable both routes for the
same skills in the same host. The commands below were checked against
`codex-cli 0.166.0` help; the guide does not register or install anything itself.

In a local checkout of this repository, create
`.agents/plugins/marketplace.json` with the following content. If that file
already exists, merge the entry rather than replacing other plugins:

```json
{
  "name": "business-to-build-local",
  "interface": { "displayName": "Business to Build Local" },
  "plugins": [
    {
      "name": "business-to-build",
      "source": { "source": "local", "path": "./" },
      "policy": {
        "installation": "AVAILABLE",
        "authentication": "ON_INSTALL"
      },
      "category": "Developer Tools"
    }
  ]
}
```

Here `./` points to the plugin repository root, where `plugin.json` lives.
The marketplace file is a catalog, separate from the plugin manifests. This is
an adaptation of the [official local marketplace layout](https://developers.openai.com/plugins/build/plugins),
not a marketplace already shipped in this repository.

Register the checkout and install its entry:

```sh
codex plugin marketplace add /absolute/path/to/codexskill
codex plugin add business-to-build@business-to-build-local
codex plugin list
cd /absolute/path/to/application
codex
```

Start a fresh session, open `/plugins` and confirm the plugin is installed.
Check `/skills` for its workflows. If registration fails, run
`codex plugin marketplace add --help` and check that the catalog is under the
registered root. Avoid manually editing Codex's plugin cache.

## Claude Code and Antigravity

For a Claude Code local plugin session, start from the application directory:

```sh
cd /absolute/path/to/application
claude --plugin-dir /absolute/path/to/codexskill
```

Invoke `/business-to-build:delivery-standards`. This session flag is not a
persistent marketplace installation. See [Claude Code plugins](https://code.claude.com/docs/en/plugins).

For workspace installation in Claude Code or Antigravity, run from this repo:

```sh
python3 scripts/install_skills.py --target /absolute/path/to/application --assistants claude antigravity --dry-run
python3 scripts/install_skills.py --target /absolute/path/to/application --assistants claude antigravity
```

Open the application in the chosen CLI or IDE and start a new session. Claude
workspace copies use `.claude/skills` and unnamespaced commands such as
`/delivery-standards`. Antigravity uses `.agents/skills`; request a skill by name.
See [Antigravity skills](https://antigravity.google/docs/skills) and the
[compatibility guide](COMPATIBILITY.md) for legacy layouts and verification limits.
This repo does not supply an Antigravity plugin manifest or a Claude marketplace.

## Create the plugin package

For this project, the plugin already exists: maintain it instead of creating a
second account plugin. Its package consists of:

```text
plugin.json                       # Portable plugin metadata and identity
.codex-plugin/plugin.json         # Codex compatibility metadata
.claude-plugin/plugin.json        # Claude Code metadata
skills/<name>/SKILL.md            # Canonical instructions and YAML metadata
skills/.../references/            # Packaged support files
README.md
AGENTS.md
CLAUDE.md
scripts/                          # Workspace installer and validation
tests/                            # Source-distribution checks
docs/                             # Linked documentation
```

Each skill has a matching directory/name and a description explaining when it
applies. Preserve the existing manifests, workflows, shared references and
`business-to-build` name. No custom MCP server, build step or credentials are
needed for these instruction-based skills.

To prepare a source archive locally, from the repository root:

```sh
python3 -B -m unittest discover -s tests -v
zip -r /tmp/business-to-build-source.zip plugin.json .codex-plugin/plugin.json .claude-plugin/plugin.json skills README.md AGENTS.md CLAUDE.md scripts tests docs -x '*/__pycache__/*' '*.pyc'
unzip -l /tmp/business-to-build-source.zip
```

Use a fresh output filename on subsequent exports: zip updates an existing
archive and can retain removed files. Review the inventory and omit application
knowledge or unrelated documents when preparing a plugin-only distribution;
retain every document referenced by included instructions. Never include Git
metadata, credentials or installed plugin caches. Local directory loading does
not require an archive. Account upload formats must follow the selected host's
current packaging requirements.

For a genuinely new plugin, use a separate source directory and new identity,
author its own manifests and skills, then test its host loading before account
creation. Do not rename this plugin to accomplish that.

## Update source, installations and the private account plugin

1. Read [RELEASING.md](RELEASING.md), inspect Git state and edit canonical
   `skills/` or the relevant source documentation. Preserve all three assistants.
2. Record dated changes and compatibility impact in [CHANGELOG.md](CHANGELOG.md).
   Before merge, classify the complete PR and synchronize all three manifest
   versions and the README. Never replace a published version in place.
3. Fetch the current target and validate:

   ```sh
   git fetch origin main
   python3 -B -m unittest discover -s tests -v
   python3 scripts/validate_release.py --base origin/main
   ```

4. Verify the affected workflows in each available host. Mark other host and
   provider checks unverified. Passing Python tests does not prove activation.
5. Refresh the distribution route you actually use:

   - Workspace copies: rerun the installer with `--dry-run`. Identical files
     are skipped; differing files are refused. Compare and manually reconcile
     only the six package directories, preserving local edits, then rerun.
     There is no force-update option.
   - Local Codex marketplace: update the source directory, run
     `codex plugin add business-to-build@business-to-build-local` again and
     inspect the result, then start a fresh session. Verify the installed
     version and changed instructions; do not assume a running session refreshed.
   - Git-backed Codex marketplace: after an explicitly authorized source push,
     use `codex plugin marketplace upgrade <marketplace-name>` before installing
     its updated entry. This command refreshes Git snapshots, not local source.
   - Claude session flag: restart with the same `--plugin-dir` pointing at
     updated source.

Account publication is separate from all these steps. When explicitly requested,
use the plugin-update workflow to read the existing plugin's current backend
release and ID, choose a higher version, validate the package and update that
same plugin with its guarded release ID. Read back saved files and record the
returned release ID. Consult [the handoff](AGENT_HANDOFF.md) for historical IDs;
retrieve current metadata instead of assuming that history is still current.
Do not push, merge or publish as a side effect of writing documentation.

## Use and verify

Start with a bounded prompt:

```text
Use Business to Build's delivery-standards skill to inspect this application
and draft its project profile and knowledge index. Report missing context.
```

Other workflows are `business-model`, `feature-specification`, `design-review`,
`feature-implementation` and `knowledge-maintenance`. See [USAGE_GUIDE.md](USAGE_GUIDE.md)
for inputs and examples. Store outputs in the target application or its selected
Confluence space.

Jira, Confluence, Figma and PR tools require separate connections in each host.
Installing these skills does not authenticate providers. Follow the
[Atlassian connection guide](../skills/delivery-standards/references/atlassian-mcp-setup.md)
when needed, and test a read before relying on external context.

If skills are missing, check the application directory, discovery path,
installation output and fresh-session skill list. If names appear twice,
inspect plugin and workspace installations for duplicates. To remove workspace
copies, review local edits and remove only this package's six skill directories.
For a Codex plugin, use `codex plugin remove business-to-build@business-to-build-local`
after checking `codex plugin remove --help`; leave unrelated plugins in place.

Verification for this guide: CLI help, relative links and all nine repository
tests passed. Release validation passed against the locally cached `origin/main`
(0.2.4 to the already prepared 0.3.0); fetch and rerun before merge. No
live installation, account publication, IDE activation or provider authentication
was performed as part of authoring it.
