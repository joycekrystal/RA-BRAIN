# Application knowledge templates

Use existing project locations if established. Otherwise propose docs/README.md as an index, docs/business/overview.md, docs/domain/glossary.md, docs/features/<feature-id>.md, docs/architecture/overview.md, docs/decisions/<id>.md, docs/engineering/standards.md and docs/operations/runbook.md. Use equivalent Confluence pages when selected as canonical. Avoid duplicate authorities.

## Application knowledge index

Application/purpose; canonical index path/URL; maintained scope; status; owner when known; review date. For each concern record canonical path/URL and source ID, ownership/status, exposed revision/commit, review date, related evidence and gap. Reuse existing documents and mark missing sources pending. Distinguish requirements/decisions, implementation, runtime data and observed verification. See ../../knowledge-maintenance/references/knowledge-base.md for the workflow.

## Project profile
Product and business objective; stakeholders and users; business model assumptions; scope; domain terms; stack and supported versions discovered from repo; repository; Jira project; Confluence space/index; Figma file/design system; environments; security/data constraints; established conventions; unresolved decisions.

## Feature specification
ID/title/status/owner; business outcome and success measure; source links and revisions; users; scope/exclusions; journey; domain rules; permissions; data/contracts; numbered acceptance criteria; UI states/design references; nonfunctional constraints; dependencies; implementation plan; verification strategy; rollout/migration/rollback; risks and open questions; change history.

## Traceability table
| Feature | Jira issue | Criterion ID and behavior | Business source | Design node | Code component | Test and result | Documentation | Gap |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
Only populate verified links. Use pending for missing evidence. A test name without a recorded passing run is not proof of acceptance.

## Engineering standards
Record existing architecture and module boundaries, naming and formatting tools, type checking, lint/build commands, dependency policy, API compatibility, validation/authentication/authorization, data migration practices, logging and error conventions, accessibility requirements, test layers and CI checks, code review criteria and release/rollback procedure. Separate adopted standards from suggested improvements. Set risk-based quality criteria and record rationale.

## Architecture decision record
ID; title; date; status (proposed/accepted/superseded); context; constraints; options; decision; consequences; source links; supersedes/superseded-by.

## Delivery review
Business objective; changes; criterion coverage; linked design/spec; tests run and outcomes; unverified checks; risks; migration/rollback; documentation updates; pending approvals or product decisions.
