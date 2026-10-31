# Business to Build usage guide

Status: reference documentation for the repository's six skills  
Reviewed: 2026-10-31  
Source: the [skill files](../skills/) and [shared delivery rules](../skills/delivery-standards/references/shared-rules.md)

Business to Build helps move from a business idea to a specified, reviewed, implemented and documented feature. You can use an individual skill for a focused task or combine skills across a delivery workflow. Start with the skill that matches the work you need; completing all six is not a prerequisite.

## Before you start

Install or enable Business to Build in your host using the [Claude Code, Codex and Antigravity setup guide](COMPATIBILITY.md). You can use workspace skill copies or the supported plugin layout described there. For Jira and Confluence context, separately connect a supported integration; for design context, connect Figma. The available tools and your permissions determine which reads and writes are possible. This package provides skill instructions, shared rules and templates; it does not provide credentials, hosted storage, automatic synchronization or background monitoring.

Give the agent the application repository or working directory, the outcome you want, and relevant source links or IDs. Include the existing documentation index, Jira issue/project, Confluence page/space and Figma file/node when applicable. You do not need every integration for every task. Without a provider, the agent can prepare local drafts and identify which source checks remain pending.

Ask for a skill by its name and plugin, for example: “Use Business to Build's feature-specification skill to specify this feature.” The prompts below use this wording so that your intent is explicit. Replace angle-bracket placeholders with your actual paths, IDs and links.

Specify where artifacts should be saved and whether you want drafts or an external update. A request to draft a feature does not authorize creating Jira issues or publishing Confluence pages. Explicitly request an external action and destination when you want one. Repository source changes also do not publish a new plugin release.

## Choose a skill

If Jira or Confluence cannot be accessed, use the [Atlassian MCP setup guide](../skills/delivery-standards/references/atlassian-mcp-setup.md). Each skill should explain the failure and provide the relevant host's connection steps, then verify access before resuming source-dependent work.

| Your task | Skill | Main outputs |
| --- | --- | --- |
| Onboard an application or agree delivery practices | [delivery-standards](#delivery-standards) | Project profile, knowledge index, standards proposal |
| Explore a product idea or revise its business model | [business-model](#business-model) | Business model canvas, solution brief, MVP and validation plan |
| Define a feature before implementation | [feature-specification](#feature-specification) | Feature document, numbered acceptance criteria, Jira-ready content |
| Review a design, compare frontend code with Figma, or prepare a design handoff | [design-review](#design-review) | Prioritized findings, implementation fidelity coverage, design brief or handoff |
| Implement or review a feature | [feature-implementation](#feature-implementation) | Code changes or review findings, verification evidence, delivery summary |
| Update documentation or find documentation drift | [knowledge-maintenance](#knowledge-maintenance) | Targeted document updates, decisions, traceability and drift findings |

## delivery-standards

Use this skill when starting work on an existing application, onboarding a new project, or establishing how business, design and engineering work should connect. It inspects the project's actual conventions and proposes only the process needed for its maturity and risk.

**Provide:** the application repository, product purpose, known users, existing guidance and documentation, and any relevant Jira, Confluence and Figma sources. Unknown details can remain explicitly unresolved.

**Example prompt:**

```text
Use Business to Build's delivery-standards skill to onboard <repository-path>.
The product helps <users> achieve <outcome>.
Read our existing guidance and knowledge index at <path-or-link>.
Relevant sources: Jira <project>, Confluence <space-or-page>, Figma <file>.
Save a project profile, concise knowledge index and engineering standards
proposal in the repository's established documentation location.
Separate existing adopted standards from proposals and list open decisions.
```

**Expect:** a project profile covering the business context, domain terms, actual stack, environments and constraints; an index of canonical documents; and a standards proposal grounded in the repository. The output should connect business objectives, feature IDs, acceptance criteria, design references, code, tests and documentation.

**Next:** review proposed standards and resolve material unknowns. Use business-model for unresolved product questions or feature-specification for a concrete feature. A proposal is not an accepted project decision until it is approved.

Source: [delivery-standards instructions](../skills/delivery-standards/SKILL.md).

## business-model

Use this skill to explore or revise a product strategy, business solution or business requirements. It can work before a repository exists.

**Provide:** the idea or existing business brief, target customers and decision makers, the problem, known alternatives, constraints and available evidence. Include existing decisions so the agent can preserve or explicitly question them.

**Example prompt:**

```text
Use Business to Build's business-model skill for <product-or-idea>.
Our target users are <users>, and the problem is <problem>.
Existing evidence and decisions: <sources>.
Constraints: <budget, timeline, operations or other constraints>.
Create a business model canvas, short solution brief, prioritized MVP
capabilities and exclusions. Map capabilities to measurable outcomes and
propose ways to validate the highest-risk assumptions.
Save the drafts to <documentation-location>.
```

**Expect:** customer and value-proposition analysis, channels and relationships, revenue and cost assumptions, key partners/resources/activities, risks, domain entities and workflows. The MVP should explain how each capability contributes to an outcome and how hypotheses could be tested. Financial figures and demand claims remain assumptions unless supported by verified evidence.

**Next:** review the assumptions and approve or revise the scope. Link accepted decisions into the knowledge index, then specify a prioritized capability with feature-specification. A generated canvas is a draft, not verified market research or an approved business plan.

Source: [business-model instructions](../skills/business-model/SKILL.md).

## feature-specification

Use this skill to turn a capability or request into reviewable feature documentation, a PRD, Jira-ready tickets or an implementation plan.

**Provide:** the requested behavior and business outcome, business brief, existing ticket/specification, relevant design nodes, repository context and known constraints. If there is no ticket yet, request a draft with a local feature identifier.

**Example prompt:**

```text
Use Business to Build's feature-specification skill to specify <feature>.
Business brief: <path-or-link>. Existing issue: <issue-ID-or-none>.
Design references: <Figma-nodes-or-none>. Repository: <path>.
Save a reviewable specification and Jira-ready ticket draft to <location>.
Include scope and exclusions, domain rules, permissions, contracts,
numbered observable acceptance criteria, failure and boundary cases,
dependencies, verification expectations and rollout considerations.
Map criteria to design, code and test expectations and list open decisions.
```

**Expect:** source references, users and journey, business outcome, data lifecycle, API/event contracts where relevant, analytics and migration/rollout needs. Business acceptance criteria should be distinct from engineering tasks and nonfunctional constraints. Performance, accessibility, privacy and reliability requirements should follow project evidence or be marked as unresolved proposals.

**Next:** review ambiguities and approve behavior before dependent implementation. Use design-review to reconcile designs, then feature-implementation to deliver the approved specification. If you want Jira issues created, explicitly request creation in the intended project; a Jira-ready draft has not been published.

Source: [feature-specification instructions](../skills/feature-specification/SKILL.md).

## design-review

Use this skill to compare a Figma flow with feature requirements, check frontend implementation against Figma, prepare an implementation handoff, or draft a brief for new designs.

**Provide:** a PR URL and application repository for an implementation review, or the exact Figma file/node or flow for a design review. The agent should read the PR description for direct design links and ticket links, then read the linked tickets for Figma references and criteria. You can also supply a ticket directly. Include design-system references, the feature specification and any approved deviations when available. For a new design brief, provide users, desired behavior, constraints and any existing component system.

**Example frontend implementation review prompt:**

```text
Use Business to Build's design-review skill to check whether the frontend
implementation in <PR-URL> matches its specified Figma design.
Repository: <application-repository>. Preview/setup: <URL-or-instructions>.
Read the PR description and its linked ticket to find the relevant Figma
file/nodes and acceptance criteria. Record the source chain and review the
code at the PR head, including relevant components, styles and assets.
Compare layout, spacing, typography, tokens, content, responsive behavior,
UI states and interactions. Where available, inspect the rendered UI at
matching viewports and states and capture supporting evidence.
Save prioritized findings with Figma nodes, code locations, expected versus
observed behavior and suggested corrections to <location>. Include coverage
and distinguish verified matches, mismatches and unverified comparisons.
```

**Example review prompt:**

```text
Use Business to Build's design-review skill to review <Figma-file-and-nodes>
against <feature-specification> and <Jira-issue>.
Check alternate flows, loading/empty/error/success states, responsive
behavior, keyboard and focus behavior, labels, permissions and destructive
actions. Save prioritized findings tied to nodes and acceptance criteria,
plus an implementation handoff with components, assets, tokens,
interactions and open questions, to <location>.
```

**Example new-design prompt:**

```text
Use Business to Build's design-review skill to prepare a design brief for
<feature> using <specification> and <design-system-reference>.
Save the brief to <location>, including required flows, states,
component guidance and unresolved questions.
```

**Expect:** actionable findings that distinguish observed defects, suggested refinements and missing evidence. Findings should identify specific nodes and criteria where available. The handoff should give an implementer the design context needed to build the feature.

For implementation reviews, expect the PR/ticket/Figma source chain, reviewed code revision, precise code locations, and a coverage table mapping design nodes, states and viewports to routes/components and evidence. Static code checks and rendered browser observations are reported separately. Passing build or lint checks does not establish visual fidelity. Conflicting design references, unavailable previews and unreviewed states remain explicit; one screenshot does not verify every breakpoint or interaction. Approved deviations should be distinguished from defects.

**Next:** resolve material gaps in the design or specification before dependent implementation. Figma creation/editing requires supported connected tools and an authorized action. If the agent cannot read the design, it should identify that limitation and provide a draft or checklist rather than claim a completed design review.

Use feature-implementation for requested code fixes. A review alone does not authorize changing code, posting PR comments or updating external sources. PR, ticket, Figma and runtime access depend on available tools; unavailable comparisons remain unverified.

Source: [design-review instructions](../skills/design-review/SKILL.md).

## feature-implementation

Use this skill to implement an application feature or review existing code against its specification, ticket and design.

**Provide:** the actual application repository, approved feature specification, numbered criteria, relevant Jira/Confluence/Figma references, and any agreed decisions. The plugin repository is not a substitute for the application repository.

**Example implementation prompt:**

```text
Use Business to Build's feature-implementation skill to implement <feature-ID>
in <application-repository> using <approved-specification>, <Jira-issue>
and <Figma-nodes>. Read repository guidance and existing architecture first.
Map criteria to affected components, contracts and verification, then make
focused changes using existing conventions and test tools.
Run relevant checks, update documentation and criterion-to-test traceability,
and provide a PR-ready summary with actual results and remaining gaps.
```

For a review, replace “implement” with “review the existing implementation” and request findings with criterion coverage and missing evidence.

**Expect:** a short delivery plan, focused implementation or review findings, and verification appropriate to the feature's risk. Relevant concerns include validation, authorization, type safety, error handling, observability, accessibility and architectural boundaries. Tests should cover meaningful business rules, integration boundaries, critical journeys and negative paths as appropriate.

The delivery report should state exact commands run and their outcomes, distinguish executed checks from proposed/manual checks, and include documentation and migration/rollback notes where relevant. A named test without a recorded run does not prove a criterion passed.

**Next:** review remaining gaps and delivery evidence. Commits, pushes, merges, deployments and ticket completion require authorization within the requested scope; implementing a feature alone does not authorize them. Material contradictions among sources should be resolved before dependent code changes while independent work continues.

Source: [feature-implementation instructions](../skills/feature-implementation/SKILL.md).

## knowledge-maintenance

For the canonical knowledge-base workflow and reusable structure, read the [knowledge-base reference](../skills/knowledge-maintenance/references/knowledge-base.md). The skill now creates or updates an application index that maps each concern to its source of truth, preserving accepted decisions, supersession, source revisions and verification gaps. Existing drift-review and documentation-update prompts remain supported.

```text
Use Business to Build's knowledge-maintenance skill to create or update this
application's canonical knowledge base from <page-or-repository>.
Read the existing index first. Maintain one canonical document per concern,
record confirmed decisions and open questions, and map criteria to evidence.
Publish to <Confluence-page-URL> and update the index; preserve history and
unrelated content, verify saved revisions, and report remaining gaps.
```

Use this skill to establish or improve a documentation structure, update documents after a change, record architectural decisions, or inspect a bounded set of sources for documentation drift.

**Provide:** the existing knowledge index and canonical document locations, the feature or change being reviewed, relevant code/tickets/designs, and known owners or accepted decisions. Bound drift checks to a feature, change set or document set so findings can be supported by evidence.

**Example prompt:**

```text
Use Business to Build's knowledge-maintenance skill to review documentation
drift for <feature-or-change-set> in <application-repository>.
Knowledge index: <path-or-link>. Related sources: <tickets, pages, designs>.
Compare these sources with <document-set>, identify concrete stale sections
or conflicts, and make targeted updates in <canonical-location>.
Preserve approved decisions and history, record new decisions with their
status, and update the index, change history and criterion-to-test table.
```

**Expect:** targeted updates to the relevant business, domain, feature, architecture, contract, engineering, test, operational or release documents. Record source IDs/URLs, exposed revisions, status and review dates, plus owners when known. Decisions can use ADRs with context, options, decision and consequences; superseded decisions should remain traceable.

**Next:** resolve conflicts requiring a product or technical decision and review pending source verification. Keep one canonical document per concern and link other systems to it. Application facts belong in the application's repository or selected Confluence space; reusable plugin improvements should be proposed separately. This skill runs when requested and does not monitor or synchronize documents in the background.

Source: [knowledge-maintenance instructions](../skills/knowledge-maintenance/SKILL.md).

## Combine the skills for a feature

A typical sequence is:

1. **delivery-standards:** establish the project context and knowledge index.
2. **business-model:** clarify the outcome and MVP when product assumptions remain open.
3. **feature-specification:** define the selected feature and numbered acceptance criteria.
4. **design-review:** check design coverage and prepare the implementation handoff.
5. **feature-implementation:** deliver the feature and record observed verification results.
6. **knowledge-maintenance:** reconcile documents and preserve decisions after delivery.

Repeat or skip steps according to existing evidence. For example, an approved specification and reviewed design may let you start at implementation. A design review may reveal a business rule that requires revisiting the specification.

For a combined request, make the outcome, sources and destinations explicit:

```text
Use Business to Build to deliver <feature> in <application-repository>.
Start from our knowledge index at <location> and the approved business
brief at <location>. Relevant sources are <Jira-issue> and <Figma-nodes>.
Use the relevant skills to reconcile the specification and design,
implement the feature, verify criteria and update canonical repository docs.
Surface material decisions before dependent work and keep missing evidence
explicit. Finish with criterion coverage, commands run, results and gaps.
```

## Review the result

Each workflow should leave concrete artifacts at the requested destination. Check that facts, assumptions, proposals and accepted decisions are distinguishable; source references are recorded; and unresolved questions are visible.

For feature delivery, use the [shared templates](../skills/delivery-standards/references/templates.md) to maintain this evidence chain:

```text
Business objective → feature → numbered acceptance criterion → design
→ code → test and observed result → documentation
```

Missing links should remain pending. If a source link cannot be read, the assistant should explain the failure and ask you to connect the relevant provider MCP server, or reconnect/authenticate the existing connection. A wrong URL or restricted page may also require a corrected link or owner-granted access. The assistant should retry the read after connection before treating the corresponding source checks as verified. External writes should be reported with their actual returned links and results.
