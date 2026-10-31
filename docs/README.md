# Rewards Application Knowledge Base

## Project Profile

| Property | Value |
| --- | --- |
| **Project Name** | Rewards Application (`rewardsapp`) |
| **Status** | Active / Inception & Specification Phase |
| **Canonical Confluence Source** | [Confluence - Features (ID: 163976)](https://joycekrystallagudas.atlassian.net/wiki/spaces/~5add6ce37b296356232d7884/pages/163976/Features) |
| **Confluence Space** | `~5add6ce37b296356232d7884` |
| **Repository** | [github.com/joycekrystal/RA-BRAIN](https://github.com/joycekrystal/RA-BRAIN.git) |
| **Last Synchronized / Retrieved** | 2026-10-31 |
| **Jira Project** | Pending configuration |
| **Figma Workspace** | Pending design reference |
| **Document Owners** | Core Engineering & Product Team |

---

## 1. Business Objective
The Rewards Application is an e-commerce customer loyalty platform designed to incentivize product purchases. Customers earn reward points proportional to their purchase spending (in Philippine Pesos / PHP) based on a configurable conversion ratio, as well as special birthday rewards. Customers can subsequently browse an exclusive rewards catalog and redeem accumulated points for products through an interactive card and pagination interface.

---

## 2. Knowledge Base Navigation

| Directory / Document | Description |
| --- | --- |
| [docs/business/overview.md](file:///Users/jclagudas/Downloads/rewardsapp/docs/business/overview.md) | Business context, user personas, incentive mechanics, and success metrics. |
| [docs/domain/glossary.md](file:///Users/jclagudas/Downloads/rewardsapp/docs/domain/glossary.md) | Standardized domain terms, business rules, and definitions. |
| [docs/architecture/overview.md](file:///Users/jclagudas/Downloads/rewardsapp/docs/architecture/overview.md) | High-level system architecture, entity relationships, security, and token lifecycle. |
| [docs/traceability.md](file:///Users/jclagudas/Downloads/rewardsapp/docs/traceability.md) | Criterion-to-test and criterion-to-implementation traceability matrix. |

### Feature Specifications (`docs/features/`)
* [FEAT-001: Authentication & Access Control](file:///Users/jclagudas/Downloads/rewardsapp/docs/features/feat-001-authentication-access-control.md) – Email login, strict password policy, role privileges (Staff vs. Customer), and token/session lifecycle rules.
* [FEAT-002: Rewards Earning Engine](file:///Users/jclagudas/Downloads/rewardsapp/docs/features/feat-002-rewards-earning-engine.md) – Points accrual per purchase amount (cost-to-points ratio in Pesos) and Birthday Month reward distribution.
* [FEAT-003: Customer Rewards Catalog & Redemption](file:///Users/jclagudas/Downloads/rewardsapp/docs/features/feat-003-rewards-catalog-redemption.md) – Card grid view with pagination, detail popup modal, quantity stepper, points balance verification, and redemption execution.
* [FEAT-004: Admin Customer Management](file:///Users/jclagudas/Downloads/rewardsapp/docs/features/feat-004-admin-customer-management.md) – Customer roster, point balance inspection, redemption order history, total points spent, and enable/disable account toggling.
* [FEAT-005: Admin Catalog & System Configuration](file:///Users/jclagudas/Downloads/rewardsapp/docs/features/feat-005-admin-catalog-system-settings.md) – Reward product inventory management (create, update, adjust stock, enable/disable, remove) and system-wide cost-to-points ratio configuration.

---

## 3. Maintenance and Traceability Policy
* All feature modifications must maintain numbered acceptance criteria (`AC-FEAT-XXX-YY`).
* Source verification: Features in this repository are derived from the canonical Confluence page `163976`.
* Changes, additions, and architectural shifts must be recorded via Architecture Decision Records (`docs/decisions/`) and updated in [docs/traceability.md](file:///Users/jclagudas/Downloads/rewardsapp/docs/traceability.md).
