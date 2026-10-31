# Feature Specification: FEAT-004 Admin Customer Management

## 1. Metadata
* **Feature ID**: `FEAT-004`
* **Title**: Admin Customer Management & Loyalty Ledger
* **Status**: In Review / Specified
* **Owner**: Backoffice Engineering Team
* **Source Link**: [Confluence - Features (Page ID: 163976)](https://joycekrystallagudas.atlassian.net/wiki/spaces/~5add6ce37b296356232d7884/pages/163976/Features)
* **Last Verified Date**: 2026-10-31

---

## 2. Business Outcome & Success Measure
Empowers administrative staff with full visibility into the customer base, loyalty balances, redemption histories, and account status management (enable/disable), ensuring comprehensive oversight and fraud prevention.

---

## 3. Users & Target Personas
* **Staff**: Operates the administrative console to review customer engagement, audit point transactions, and enforce access controls.

---

## 4. Scope
* **In-Scope**:
  * Paginated roster of registered customers with search and filter capabilities.
  * Customer Detail View displaying:
    * Customer identity (Email, Registration Date, Account Status).
    * Current remaining points balance.
    * History of reward products purchased (Redemption Orders).
    * Aggregate count of total redemption orders and points expended.
    * Total points earned from purchases and birthday bonuses.
  * Account status toggle: Enable or Disable customer accounts.
* **Out-of-Scope**:
  * Direct manual password editing by staff (staff can trigger a reset link instead).
  * Direct customer deletion (soft disabling is used to preserve financial and audit ledger integrity).

---

## 5. Domain Rules & Policies
1. **Access Authorization**:
   * All customer management endpoints require active `STAFF` credentials.
2. **Account Disablement Impact**:
   * When an admin sets `is_enabled = false`:
     * Customer's active tokens and sessions are immediately revoked.
     * Customer cannot log in or perform redemptions.
     * Historical points and orders remain stored and untouched for audit purposes.
3. **Ledger Integrity**:
   * Remaining points shown on the customer profile must reconcile exactly with the ledger sum:
     $$\text{Remaining Points} = \sum (\text{Accrued Points}) - \sum (\text{Redeemed Points}) + \sum (\text{Adjustments})$$

---

## 6. Numbered Acceptance Criteria

* **AC-FEAT-004-01 (Registered Customer List)**: Given an authenticated Staff member in the Admin section, the system must display a list of all registered customers showing email, registration date, current status (Active/Disabled), and remaining points.
* **AC-FEAT-004-02 (Customer Details View)**: Given a Staff user selects a specific customer, the system must present a detailed view showing:
  * Customer email and registration details.
  * Remaining points balance.
  * List of reward products purchased with points (including product name, quantity, points spent, order date).
  * Total number of redemption orders placed.
  * Total lifetime points earned and spent.
* **AC-FEAT-004-03 (Enable/Disable Customer)**: Given an admin viewing a customer record, the admin can toggle the customer's account status between `Enabled` and `Disabled`.
* **AC-FEAT-004-04 (Disabled Enforcement)**: Given a customer whose status has been changed to `Disabled`, when that customer makes any API request or attempts login, access is denied immediately with HTTP 403.
* **AC-FEAT-004-05 (Re-enabling Customer)**: Given a previously disabled customer, when the admin toggles status back to `Enabled`, the customer can log in again with their previous balance and order history intact.

---

## 7. API Contract Draft

### `GET /api/v1/admin/customers?page=1&limit=20`
**Response (200 OK)**:
```json
{
  "customers": [
    {
      "id": "c1f7b02e-9d22-482d-8e6d-6fd21d3f0a14",
      "email": "jane.doe@example.com",
      "current_points": 450,
      "is_enabled": true,
      "created_at": "2026-09-15T08:30:00Z"
    }
  ],
  "pagination": { "current_page": 1, "total_pages": 5, "total_items": 92 }
}
```

### `GET /api/v1/admin/customers/{id}`
**Response (200 OK)**:
```json
{
  "id": "c1f7b02e-9d22-482d-8e6d-6fd21d3f0a14",
  "email": "jane.doe@example.com",
  "is_enabled": true,
  "current_points": 450,
  "lifetime_points_earned": 1200,
  "total_orders_count": 3,
  "redemption_history": [
    {
      "order_id": "ord-883921",
      "product_id": "7b587a12-c2e9-4e78-958a-a43bfa99b11c",
      "product_name": "Stainless Steel Tumbler",
      "quantity": 2,
      "total_points_spent": 500,
      "created_at": "2026-10-20T14:10:00Z"
    }
  ]
}
```

### `PATCH /api/v1/admin/customers/{id}/status`
**Request Body**:
```json
{
  "is_enabled": false
}
```
**Response (200 OK)**:
```json
{
  "id": "c1f7b02e-9d22-482d-8e6d-6fd21d3f0a14",
  "is_enabled": false,
  "updated_at": "2026-10-31T22:30:00Z"
}
```
