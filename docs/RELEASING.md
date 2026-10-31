# Change history and release policy

Every change to this repository must be recorded in `docs/CHANGELOG.md` with the
date it happened, what changed and its compatibility impact. Before a PR merges
to `main`, its cumulative changes must have a new semantic version and release
entry. Documentation, tests, tooling and CI changes are included. Use one version
for the complete PR; individual commits do not each require a separate version.
If the PR grows, update the entry and increase the bump level when necessary.

## Select the version

The public contract includes skill names and triggering scope, workflow inputs
and promised outputs, shared references, installation paths/options and required
integrations. Classify the highest impact relative to the current `main` version:

| Type | When | Example from 0.2.0 |
| --- | --- | --- |
| patch | Compatible corrections, clarifications, documentation, tests or maintenance with no new user workflow | 0.2.1 |
| minor | Compatible new skills, workflow capabilities, optional inputs/outputs or assistant support; deprecations | 0.3.0 |
| major | Incompatible removal/rename, changed required inputs, removed outputs or installation changes requiring user migration | 1.0.0 |

Use compatibility and behavior, not the number of changed files or lines.
Reset lower components on a minor or major bump. This repository deliberately
applies the same explicit breaking-change rule during `0.x` development, although
SemVer permits unstable APIs before 1.0. See [Semantic Versioning](https://semver.org/).
Normal releases currently use `MAJOR.MINOR.PATCH`; prereleases and build metadata
require extending the validator before use.

## Before merging to main

1. Review the entire change set against the latest target branch and select the
   highest applicable type: `patch`, `minor` or `major`.
2. Set the next version in `plugin.json`, `.codex-plugin/plugin.json` and
   `.claude-plugin/plugin.json`. Keep the README version synchronized. Do not
   modify a version already published; use a new one.
3. Prepend a dated entry in `docs/CHANGELOG.md`, preserving older entries. Include
   `Release type: patch` (or `minor`/`major`), a `Rationale:` line explaining the
   classification, and dated bullets for each change. Use the actual change date;
   the heading date is the release preparation date. Unknown historical dates
   remain unknown rather than being invented. Include migration notes for a major.
4. Run the commands below. If `main` advances, reconcile and rerun against its
   latest version. Reviewers must check that the declared impact matches the
   behavior; automation cannot infer semantic impact reliably.
5. Require the `Release policy` status check in GitHub branch protection/rulesets
   for `main`, require branches to be current, and restrict bypasses/direct pushes
   according to the team's policy. The workflow is supplied here; repository
   settings must be configured separately before it is a mandatory merge gate.

```sh
python3 -B -m unittest discover -s tests -v
python3 scripts/validate_release.py --base origin/main
```

Fetch the latest `origin/main` before the local check. CI compares against the PR
target commit and runs on every PR to `main`, including documentation-only PRs.
It checks the declared bump, synchronized manifests/README, dated current entry
and preservation of existing release history. The repository intentionally uses
the exact next version for the declared impact rather than skipping versions.

## Publication is separate

A merge does not publish the private plugin. When publication is requested, read
the backend's current release, retain its exact identity and guarded release ID,
and ensure the candidate version is higher than the published version. If the
backend has advanced beyond `main`, reconcile both before choosing a new version.
Package and validate the source, publish through the existing update workflow,
then read back the saved files and record the returned release ID in the handoff.
Never automatically push, merge, publish or change branch protection as part of
version validation.
