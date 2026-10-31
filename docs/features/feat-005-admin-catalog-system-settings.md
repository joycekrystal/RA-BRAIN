# Feature Specification: FEAT-005 Admin Catalog & System Settings

## 1. Metadata
* **Feature ID**: `FEAT-005`
* **Title**: Admin Reward Product Management & Conversion Settings
* **Status**: In Review / Specified
* **Owner**: Backoffice & Inventory Team
* **Source Link**: [Confluence - Features (Page ID: 163976)](https://joycekrystallagudas.atlassian.net/wiki/spaces/~5add6ce37b296356232d7884/pages/163976/Features)
* **Last Verified Date**: 2026-10-31

---

## 2. Business Outcome & Success Measure
Provides administrators with full management over the reward product lifecycle (create, update, adjust inventory, toggle visibility, and delete) and dynamic control over the system-wide purchase cost-to-points accrual ratio.

---

## 3. Users & Target Personas
* **Staff (Admin)**: Manages reward product catalog, monitors available stock levels, adjusts inventory, and calibrates points-per-peso ratios.

---

## 4. Scope
* **In-Scope**:
  * **Cost-to-Points Ratio Setting**:
    * Global setting defining the currency expenditure (in Philippine Pesos) needed to earn 1 point.
    * Real-time update capability.
  * **Reward Product Creation**:
    * Fields: Product Name, Description, Points Cost, Available Quantity, Enabled/Disabled status.
  * **Reward Product Inventory & Details Management**:
    * Admin list of all products (both enabled and disabled).
    * Detail view with inline or dedicated edit capabilities.
    * Quantity adjustment: increment or decrement available stock.
    * Visibility toggle (`is_enabled` flag): directly controls display to customers.
  * **Product Removal**:
    * Deletion or soft-deletion of reward products from the catalog.
* **Out-of-Scope**:
  * Supplier purchase order tracking / vendor management.
  * Barcode scanning.

---

## 5. Domain Rules & Policies
1. **Visibility Control**:
   * If `is_enabled == false`, the product is immediately hidden from customer-facing catalog queries (`GET /api/v1/rewards`).
   * If `available_quantity <= 0`, customers cannot place redemption orders for the product.
2. **Inventory Quantity Rules**:
   * Stock quantity cannot be negative.
   * Adjusting stock updates the database with concurrency safety.
3. **Product Removal**:
   * Products that have existing customer redemption orders cannot be hard-deleted from the database (to prevent foreign key violations and broken historical records); they are marked archived/deleted. Products with zero order history may be permanently deleted.
4. **Ratio Setting**:
   * Ratio value must be a positive number ($> 0$).

---

## 6. Numbered Acceptance Criteria

* **AC-FEAT-005-01 (Cost-to-Points Ratio Setting)**: Given an authenticated Staff member, the admin interface allows viewing and editing the system cost-to-points ratio (Pesos per Point). Upon saving, the new ratio takes immediate effect for all subsequent purchase accruals.
* **AC-FEAT-005-02 (Create Reward Product)**: Given an admin completing the product creation form with Name, Description, Points Cost, Initial Quantity, and Visibility status, when submitted, a new reward product is persisted and assigned a unique ID.
* **AC-FEAT-005-03 (Admin Product List & Details)**: Given an admin navigating to Product Management, the system displays all products with their names, descriptions, points cost, available quantity, and visibility status.
* **AC-FEAT-005-04 (Enable/Disable Visibility Toggle)**: Given any product in the admin catalog, when the admin toggles its visibility to `Disabled`, it is immediately suppressed from customer catalog views; when toggled to `Enabled`, it becomes visible if stock $> 0$.
* **AC-FEAT-005-05 (Inventory Stock Adjustment)**: Given an existing product, the admin can add or reduce available quantity. The resulting available quantity must be an integer $\ge 0$.
* **AC-FEAT-005-06 (Remove Product)**: Given an existing product, when an admin selects remove/delete, the product is removed from active admin and customer listings. If prior redemption records exist, historical order integrity is preserved.

---

## 7. API Contract Draft

### `GET /api/v1/admin/settings/cost-to-points-ratio`
**Response (200 OK)**:
```json
{
  "key": "COST_TO_POINTS_RATIO",
  "currency": "PHP",
  "cost_per_point": 100.0,
  "updated_at": "2026-10-31T22:30:00Z"
}
```

### `PUT /api/v1/admin/settings/cost-to-points-ratio`
**Request Body**:
```json
{
  "cost_per_point": 150.0
}
```

### `POST /api/v1/admin/products`
**Request Body**:
```json
{
  "name": "Canvas Tote Bag",
  "description": "Eco-friendly branded cotton tote bag.",
  "points_cost": 120,
  "available_quantity": 50,
  "is_enabled": true
}
```
**Response (201 Created)**:
```json
{
  "id": "e2c3b881-817a-426b-9cb6-990712a1ef55",
  "name": "Canvas Tote Bag",
  "points_cost": 120,
  "available_quantity": 50,
  "is_enabled": true
}
```

### `PATCH /api/v1/admin/products/{id}/inventory`
**Request Body**:
```json
{
  "adjustment_type": "INCREMENT",
  "quantity_delta": 25
}
```
**Response (200 OK)**:
```json
{
  "id": "e2c3b881-817a-426b-9cb6-990712a1ef55",
  "available_quantity": 75,
  "updated_at": "2026-10-31T22:30:00Z"
}
```

### `DELETE /api/v1/admin/products/{id}`
**Response (200 OK)**:
```json
{
  "success": true,
  "message": "Product archived successfully."
}
```
