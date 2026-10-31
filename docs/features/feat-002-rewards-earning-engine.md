# Feature Specification: FEAT-002 Rewards Earning Engine

## 1. Metadata
* **Feature ID**: `FEAT-002`
* **Title**: Points Earning Engine & Birthday Bonus
* **Status**: In Review / Specified
* **Owner**: Backend Loyalty Team
* **Source Link**: [Confluence - Features (Page ID: 163976)](https://joycekrystallagudas.atlassian.net/wiki/spaces/~5add6ce37b296356232d7884/pages/163976/Features)
* **Last Verified Date**: 2026-10-31

---

## 2. Business Outcome & Success Measure
Automatically calculates and awards loyalty points to customers based on purchase spending in Philippine Pesos (PHP) and distributes birthday rewards during the customer's birth month, maximizing customer retention.

---

## 3. Users & Target Personas
* **Customer**: Receives points into their rewards wallet upon purchasing items or upon reaching their birthday month.
* **Staff**: Configures and tunes the cost-to-points ratio to adjust loyalty margins.

---

## 4. Scope
* **In-Scope**:
  * Calculation of earned points per purchase amount using the active cost-to-points ratio.
  * System-wide ratio storage (Points per Peso).
  * Automated or scheduled birthday month bonus point distribution (awarded during customer's birthday month once per year).
  * Immutable transaction logging for each points credit.
* **Out-of-Scope**:
  * Multi-tiered loyalty statuses (Gold, Silver, Platinum) - can be layered in future releases.
  * Points expiration periods (points currently do not expire unless explicitly configured).

---

## 5. Domain Rules & Policies
1. **Purchase Points Formula**:
   $$\text{Points Earned} = \left\lfloor \frac{\text{Purchase Amount (PHP)}}{\text{Cost per Point Setting}} \right\rfloor$$
   *(Example: If ratio is 100 PHP per point, a 250 PHP purchase awards 2 points).*
2. **Configurability**:
   * The cost-to-points ratio must be dynamically modifiable by the system without requiring redeployment.
3. **Birthday Month Reward**:
   * Awarded to the customer during their birth month.
   * Cannot be awarded more than once per customer per calendar year.
   * The point amount for the birthday grant is managed via system settings (e.g., default 50 points or configurable).

---

## 6. Numbered Acceptance Criteria

* **AC-FEAT-002-01 (Purchase Points Calculation)**: Given a customer completes a product purchase of $N$ Pesos, when the active cost-to-points ratio is $R$ Pesos per point, then the customer's balance is credited with $\lfloor N / R \rfloor$ points.
* **AC-FEAT-002-02 (Dynamic Ratio Application)**: Given a change in the cost-to-points ratio by Staff, all subsequent purchases immediately calculate points using the newly configured ratio; historical point accruals remain unchanged.
* **AC-FEAT-002-03 (Birthday Month Eligibility)**: Given a registered customer with a recorded birth date, when the current date falls within the customer's birth month, then the system awards the birthday reward points to the customer.
* **AC-FEAT-002-04 (Birthday Reward Uniqueness)**: Given a customer who has already received their birthday bonus in the current calendar year, when subsequent checks occur within the same month or year, no duplicate points are awarded.
* **AC-FEAT-002-05 (Points Transaction Ledger)**: Given any point accrual (purchase or birthday), a corresponding record must be created in `POINTS_TRANSACTION` detailing transaction type, customer ID, points added, purchase value (if applicable), and timestamp.

---

## 7. Data Contracts Draft

### Event / Command: `AwardPurchasePoints`
```json
{
  "customer_id": "c1f7b02e-9d22-482d-8e6d-6fd21d3f0a14",
  "purchase_order_id": "po-991240",
  "total_amount_pesos": 1500.00,
  "currency": "PHP"
}
```
**Outcome**:
* Accrues points: $1500 / 100 = 15$ points.
* Creates `POINTS_TRANSACTION` with `transaction_type = "PURCHASE_ACCRUAL"`.
* Increments `CUSTOMER_PROFILE.current_points` by 15.
