---
name: design-review
description: "Use when reviewing Figma designs, checking frontend implementation against Figma references discovered through PR descriptions and linked tickets, reconciling designs with acceptance criteria, or preparing a design handoff or new design brief."
---

Read ../delivery-standards/references/shared-rules.md and ../delivery-standards/references/templates.md. Support design/specification reviews, frontend implementation reviews and new design briefs. Keep a review scoped to the requested feature, PR or flow.

## Resolve the design and implementation sources

For a PR review, read its description, base/head revisions and changed files using available connected tools or repository tooling. Extract direct Figma links and linked ticket URLs/IDs from the description. Read the relevant linked tickets, including their description, acceptance criteria, design links and explicitly referenced design decisions. Follow relevant specification links only as needed to resolve this feature's design source. Do not stop at the PR description when its ticket contains the design reference. A supplied ticket or Figma node can also be the starting point when there is no PR.

Record the source chain: PR → ticket → Figma file/node, including direct PR-to-Figma references when present. Record URLs/IDs, exposed revisions/status and retrieval dates. Retrieve the relevant Figma nodes, visual references and available design-system information alongside the feature specification and criteria. If links conflict, point to different variants, omit a node, or refer to a superseded design, inspect the available context and accepted decisions; surface unresolved material ambiguity before judging dependent implementation. Do not choose an unrelated frame or assume the newest design is the approved one. Ask for the missing reference only after inspecting accessible PR and ticket context.

Inspect the actual frontend code at the reviewed PR head, its diff and relevant surrounding components/styles/assets. Confirm the local checkout or preview corresponds to that revision; otherwise identify the mismatch and scope the evidence accordingly. A PR description or screenshot alone is not evidence that the code implements the design. If a provider, repository, design node or runtime is unavailable, continue independent checks and state precisely which comparisons remain unverified.

## Review design coverage and frontend fidelity

Check primary and alternate flows, loading/empty/error/success states, responsive behavior, keyboard/focus behavior, labels and semantics, permissions, destructive actions and reusable components against the specification and criteria.

For frontend implementation reviews, map the relevant Figma frames/components and states to routes, code components and changed lines. Compare layout, alignment, spacing, sizing, typography, colors/tokens, borders/radii/shadows, icons/images, content, component variants and interactions. Inspect responsive rules, overflow, long content and state transitions where specified. Check reuse of the established design system and distinguish approved deviations from implementation defects. Do not invent viewport requirements, design tokens or pixel tolerances absent from project guidance.

When the application can run with available tools, follow its documented setup and use a browser or existing preview to inspect the affected routes and states. Compare rendered UI with Figma at matching viewport dimensions and equivalent content/state; record the route, viewport, state, reviewed revision and screenshot evidence when available. Exercise relevant interactions and keyboard/focus behavior. Use existing visual or interaction tests where useful and report commands actually run. Account for differing data, fonts and assets before attributing a visual difference to code. Static inspection supports code findings but cannot establish rendered visual fidelity; clearly distinguish static checks from observed browser results. Do not claim all breakpoints or states match from one screenshot.

## Report findings and coverage

Deliver prioritized, actionable findings tied to the Figma node, criterion when available, and precise code location. Each implementation finding should explain the expected design, observed implementation, user impact and suggested correction, with supporting visual or code evidence. Distinguish observed defects, proposed refinements, accepted deviations and unavailable evidence. Avoid speculative defects; report no findings when the reviewed evidence supports that result, while retaining scope and verification limits.

Include a concise coverage table with: PR/ticket reference, design node/state/viewport, route/component and code location, check performed, evidence/result and remaining gap. Use verified match, mismatch or unverified for each scoped comparison; do not equate passing build/lint checks with design fidelity. Summarize the reviewed revision, source chain, commands and observed results, unresolved decisions and unreviewed states. Use the shared traceability template when acceptance criteria are involved.

For design/specification reviews, also deliver an implementation handoff listing assets, component mappings, interactions, tokens and open questions. For new designs, produce a concrete brief and use supported Figma creation tools only when connected and authorized; otherwise deliver a draft brief without claiming Figma edits. A review request does not authorize code fixes, PR comments, ticket updates or Figma edits; perform those only within the user's requested scope. Route requested implementation fixes through feature-implementation.
