# Application knowledge base and canonical references

## Purpose and boundaries

Create or maintain durable documentation that future contributors and assistants
can use to understand an application. A knowledge base is an index plus scoped
documents and evidence links; it is not a hosted service, database, automatic
synchronizer or promise of cross-chat memory.

Choose one canonical document per concern. A feature specification describes
intended behavior, an accepted ADR records a decision, code records implementation,
the application database stores runtime records, and observed tests provide
verification. Do not treat any single source as proof of all these concerns.
Report contradictions and obtain material decisions before dependent work.

Reuse an existing application index or selected Confluence page. When none exists,
propose `docs/README.md` in the application repository or an index in the chosen
Confluence location. A small application can use sections of one page; create
linked documents only when scope or ownership warrants them. Do not create empty
placeholder pages or duplicate an existing authority.

## Minimum index

Record application name and purpose, the index location, maintained scope, status,
owner if known and review date. For each concern, maintain:

| Concern / scope | Canonical path or URL / ID | Status / owner | Source revision / review date | Related evidence / gap |
| --- | --- | --- | --- | --- |
| Business context and glossary | Existing application source or pending | Known values or unassigned | Exposed values only | Link verified sources |
| Capability / feature rules and criteria | Existing specification or pending | Draft, accepted or superseded | Exposed values only | Jira / design / code / tests as available |
| Architecture and contracts | Existing document or pending | Known values | Commit/version if exposed | Do not infer a stack without repository evidence |
| Engineering, tests and operations | Existing guidance or pending | Known values | Reviewed revision/date | Executed checks distinct from proposed checks |
| Decisions and release history | Existing ADR/log or pending | Decision status | Date/revision | Supersedes / superseded-by links |

This table is a concern checklist, not a requirement to create every document.
When a task covers only a feature, explicitly state that bounded scope.

## Feature knowledge record

- Feature ID/title, business outcome, scope/exclusions and glossary references.
- Status, owner when known, source links/IDs, exposed revision and review date.
- Confirmed rules and observable numbered criteria; negative/boundary behavior
  where known. Preserve prior IDs; map replacements if renumbering is necessary.
- Accepted decisions with their source and date; separate unresolved questions
  and technical proposals. Record old and superseding requirements explicitly.
- Jira, Figma nodes, code components, contracts, tests and observed results.
  Use pending for missing references; a test plan is not an executed result.
- Dated change history, implementation gaps and decisions needed next.

Capture decisions supplied in chat into authorized durable documentation, with a
concise attribution such as requester decision and date. Do not invent a ticket
or URL for a chat decision, identify a source author as owner without evidence,
or publish unrelated chat contents. Preserve the exact business meaning and mark
ambiguity instead of silently choosing values.

## Maintenance cycle

1. Read the index and a bounded set of relevant current documents and evidence.
2. Compare new decisions and changed tickets/design/code with existing rules.
3. Prepare focused updates, resolve material conflicts and identify supersession.
4. Save authorized repository changes or publish only to requested external
   destinations. A request to review or draft alone does not authorize publishing.
5. Use current revision guards where supported, read back saved content and
   verify the index references. Retry only after reconciling concurrent changes.
6. Report what was saved, canonical links/revisions, actual verification, remaining
   gaps and next decisions. Include a handoff that does not depend on chat memory.

Keep application-specific knowledge in its application repository or selected
Confluence space. The Business to Build repository holds only this reusable
workflow and generic templates. Use supported integrations and fallbacks per
host; no proprietary assistant command is required for the documentation model.

## Example requests

```text
Use knowledge-maintenance to create or update the application knowledge base
from <source-page-or-repository>. Read the existing index first. Reuse canonical
documents, capture confirmed rules and decisions, list open questions, and map
criteria to source/design/code/test evidence. Save drafts to <destination>.
```

```text
Publish the reviewed decisions to <Confluence-page-URL> and update its canonical
knowledge index. Preserve unrelated content and history, show superseded rules,
read back the result, and report the saved revision and remaining gaps.
```
