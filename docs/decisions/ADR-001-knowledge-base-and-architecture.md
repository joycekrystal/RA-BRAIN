# ADR-001: Adoption of Modular Loyalty Knowledge Base & Token Lifecycle Architecture

## 1. Metadata
* **ID**: `ADR-001`
* **Title**: Adoption of Modular Loyalty Knowledge Base & Token Lifecycle Architecture
* **Date**: 2026-10-31
* **Status**: Accepted
* **Author / Owners**: Core Engineering Team
* **Source Link**: [Confluence - Features (ID: 163976)](https://joycekrystallagudas.atlassian.net/wiki/spaces/~5add6ce37b296356232d7884/pages/163976/Features)
* **Supersedes**: None
* **Superseded By**: None

---

## 2. Context & Problem Statement
The Rewards Application requires a standardized, durable engineering and business knowledge base representing loyalty rules, administrative controls, and strict authentication constraints specified in the Confluence documentation. The project needed an architectural baseline for token lifecycle management, transactional balance safety, and traceability.

---

## 3. Decision Drivers & Constraints
* Canonical Confluence Source: Page ID `163976` in space `~5add6ce37b296356232d7884`.
* Strict session and token parameters (6h session, 1d access token, 2d idle access timeout, 30d refresh max, 7d refresh idle timeout).
* Immediate data consistency between reward points deduction and product inventory decrement during redemption.
* Compliance with the delivery standards guidelines (no duplicate authorities, numbered acceptance criteria, explicit traceability).

---

## 4. Options Considered
1. **Monolithic Single-Document Specification**:
   * *Pros*: Simple single file.
   * *Cons*: Difficult to trace granular acceptance criteria, hard to maintain as features grow, violates modular documentation standards.
2. **Modular Domain-Driven Knowledge Base with Traceability Matrix (Selected)**:
   * *Pros*: Clear separation between Business Overview, Domain Glossary, Architecture, Individual Feature Specifications (FEAT-001 through FEAT-005), and an end-to-end Traceability Matrix.
   * *Cons*: Requires disciplined maintenance when requirements shift.

---

## 5. Decision Outcome
Adopted the **Modular Knowledge Base Structure** under `docs/`:
1. `docs/README.md` as the central index and project profile.
2. `docs/business/overview.md` for business model, user personas, and incentives.
3. `docs/domain/glossary.md` for authoritative terms.
4. `docs/architecture/overview.md` for entity relationships and token lifecycle.
5. `docs/features/FEAT-001` to `FEAT-005` for discrete functional modules with numbered ACs.
6. `docs/traceability.md` for end-to-end tracking to verification.

---

## 6. Consequences & Next Steps
* **Positive**: Full alignment with delivery standards; every acceptance criterion is ready for Jira issue binding and test suite linking.
* **Open Questions / Pending Items**:
  * Jira project keys to be mapped to `docs/traceability.md`.
  * Figma design node links to be attached once wireframes/designs are ready.
