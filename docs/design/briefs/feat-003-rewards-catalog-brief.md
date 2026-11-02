# Design Brief: Customer Rewards Catalog & Redemption Modal (FEAT-003)

Status: Ready for Figma Design  
Feature Specification: [FEAT-003 Specification](file:///Users/jclagudas/Downloads/rewardsapp/docs/features/feat-003-rewards-catalog-redemption.md)  
Design System Reference: [Brand Kit & Tokens](file:///Users/jclagudas/Downloads/rewardsapp/docs/design/brand-kit.md)  
Traceability Matrix: [Acceptance Criteria Traceability](file:///Users/jclagudas/Downloads/rewardsapp/docs/traceability.md#L20-L28)  

---

## 1. Objective & User Story
Provide customers with an intuitive, engaging rewards catalog where they can browse available products, check point costs and stock, and seamlessly redeem points through an interactive modal dialog with quantity selection.

> **User Story**:  
> *As a Customer, I want to see how many points I have, browse available reward products in clean cards with pagination, and click any item to select a quantity and redeem it, so that I can enjoy the benefits of my purchases.*

---

## 2. Screens & Core Layout Anatomy

```
+-----------------------------------------------------------------------------------+
|  [Logo] RewardsApp                  [⭐ 450 Points]  [Jane Doe ▼]                 |  <- Navbar
+-----------------------------------------------------------------------------------+
|                                                                                   |
|  Rewards Catalog                                                                  |  <- Page Title
|  Redeem your earned points for exclusive products                                 |
|                                                                                   |
|  +--------------------+  +--------------------+  +--------------------+           |
|  | [ Image / Icon ]   |  | [ Image / Icon ]   |  | [ Image / Icon ]   |           |
|  | Stainless Tumbler  |  | Canvas Tote Bag    |  | Wireless Earbuds   |           |
|  | 500ml insulated... |  | 100% cotton eco... |  | Noise-canceling... |           |
|  |                    |  |                    |  |                    |           |
|  | ⭐ 250 Points      |  | ⭐ 120 Points      |  | ⭐ 600 Points      |           |
|  | 📦 45 available    |  | 📦 12 available    |  | ⚠️ Out of Stock    |           |
|  | [ Redeem Reward ]  |  | [ Redeem Reward ]  |  | [ Unavailable ]    |           |
|  +--------------------+  +--------------------+  +--------------------+           |
|                                                                                   |
|                      [ < Prev ]  Page 1 of 4  [ Next > ]                          |  <- Pagination
+-----------------------------------------------------------------------------------+
```

---

## 3. Detailed Screen Specifications

### 3.1 Screen A: Customer Rewards Catalog Page
* **Route**: `/rewards`
* **Header Bar**:
  * Brand logo.
  * **Points Balance Chip**: Pill badge highlighted with gold amber background (`#FFFBEB`), showing the customer's live balance (e.g., `⭐ 450 Points Available`).
* **Main Content Area**:
  * Heading: "Rewards Catalog" (`H1`, 30px bold, `text-slate-900`).
  * Subtitle: Descriptive text (`text-slate-600`).
  * **Card Grid**: Responsive grid layout:
    * Desktop ($\ge 1024\text{px}$): 3 or 4 columns.
    * Tablet ($768\text{px} - 1023\text{px}$): 2 columns.
    * Mobile ($< 768\text{px}$): 1 column.
* **Pagination Bar**:
  * Bottom centered.
  * Controls: "Previous" button, Current page / Total pages indicator (e.g., `Page 1 of 4`), and "Next" button.
  * Disabled states for Previous on Page 1, and Next on the final page.

### 3.2 Screen B: The Reward Card (`RewardCard`)
Each card in the grid must explicitly render the 4 data points required by **`AC-FEAT-003-01`**:
1. **Reward Name**: Bold title, truncated to 2 lines max (`H3`, 18px semibold).
2. **Reward Description**: 2 to 3 lines of descriptive text (`text-slate-600`, 14px regular).
3. **Points Cost**: High-contrast badge with amber/gold styling (e.g., `⭐ 250 Points`).
4. **Number of Products Available**: Stock badge (e.g., `📦 45 in stock`).
5. **Call-to-Action**: "Redeem" button or whole card clickable with clear hover elevation (`shadow-md`).

---

### 3.3 Screen C: The Redemption Modal Dialog (`RedemptionDialog`)
Triggered when the user clicks any available reward card (**`AC-FEAT-003-03`**):

```
+--------------------------------------------------------------------+
|  Redeem Reward                                                [X]  |
+--------------------------------------------------------------------+
|                                                                    |
|  [ Product Thumbnail / Hero Icon ]                                 |
|                                                                    |
|  Stainless Steel Tumbler                                           |
|  500ml double-wall insulated water tumbler. Keeps beverages        |
|  hot for 12 hours or cold for 24 hours. Premium matte finish.      |
|                                                                    |
|  ----------------------------------------------------------------  |
|                                                                    |
|  Quantity to Redeem:                                               |
|  [ - ]   2   [ + ]        (Stock available: 45 units)              |
|                                                                    |
|  ----------------------------------------------------------------  |
|                                                                    |
|  Points Per Unit:            250 Points                            |
|  Total Points Required:      500 Points                            |
|  Your Remaining Points:      450 Points                            |
|                                                                    |
|  ⚠️ You need 50 more points to redeem 2 items.                     | <- If balance < total
|                                                                    |
+--------------------------------------------------------------------+
|                [ Cancel ]        [ Buy (500 Points) ]              |
+--------------------------------------------------------------------+
```

#### Modal Elements & Interaction Rules:
* **Description Area**: Complete, unabbreviated product description.
* **Quantity Input Stepper** (**`AC-FEAT-003-04`**):
  * Left button: Minus (`-`) — Disabled when quantity is 1.
  * Center field: Numeric display of selected quantity (Default = 1).
  * Right button: Plus (`+`) — Disabled when quantity reaches `available_quantity` or maximum units affordable.
* **Real-Time Points Calculator**:
  * Displays: $\text{Quantity} \times \text{Unit Points Cost} = \text{Total Points}$.
* **Action Buttons**:
  * **"Cancel" Button** (**`AC-FEAT-003-05`**): Closes dialog with zero side effects.
  * **"Buy" Button** (**`AC-FEAT-003-06`**):
    * Primary high-contrast button (`bg-indigo-600`).
    * Disabled or blocked with descriptive warning banner if $\text{Customer Points} < \text{Total Points}$ (**`AC-FEAT-003-07`**).

---

## 4. UI States Matrix to Design in Figma

| # | State Name | Figma Frame Name | Key Visual Requirements |
| --- | --- | --- | --- |
| 1 | **Catalog - Default Grid** | `Catalog / Desktop / Default` | 12 items per page, balanced grid, pagination at bottom. |
| 2 | **Catalog - Mobile View** | `Catalog / Mobile 375px / Default` | Single column stacked cards, sticky points chip in header. |
| 3 | **Card - Hover / Active** | `Component / Card / Hover` | Card border turns `--color-primary-500`, shadow elevates to Level 2. |
| 4 | **Card - Out of Stock** | `Component / Card / Out-of-Stock` | Grayed out image/content, badge: "Out of Stock", CTA disabled (`AC-FEAT-003-08`). |
| 5 | **Modal - Default (Qty = 1)** | `Modal / Redeem / Default` | Modal open with 1 item selected, points calculation matching unit cost. |
| 6 | **Modal - Stepper Active** | `Modal / Redeem / Stepper-Active` | Qty incremented to 3, total points multiplied, decrement button active. |
| 7 | **Modal - Insufficient Points** | `Modal / Redeem / Insufficient-Points` | Red banner (`--color-error`), "Buy" button disabled (`AC-FEAT-003-07`). |
| 8 | **Modal - Success State** | `Modal / Redeem / Success` | Checkmark animation, "Redemption Successful!", new points balance displayed. |
| 9 | **Catalog - Loading Skeleton** | `Catalog / Desktop / Loading` | Pulse skeleton cards for product image, title, and buttons. |
| 10 | **Catalog - Empty State** | `Catalog / Desktop / Empty` | Friendly giftbox illustration, "No rewards available yet. Check back soon!" |

---

## 5. Acceptance Criteria Traceability Checklist for Review

When Figma frames are ready, `/design-review` will verify:
* [ ] **`AC-FEAT-003-01`**: Does every card display Name, Description, Points Cost, and Stock Available?
* [ ] **`AC-FEAT-003-02`**: Are pagination controls clearly visible and positioned?
* [ ] **`AC-FEAT-003-03`**: Does clicking a card trigger the popup modal with full description, stepper, Buy & Cancel?
* [ ] **`AC-FEAT-003-04`**: Does the input stepper have `-` and `+` controls with minimum 1 constraint?
* [ ] **`AC-FEAT-003-05`**: Is there an explicit "Cancel" button that dismisses the dialog?
* [ ] **`AC-FEAT-003-06`**: Does the "Buy" button communicate the purchase action and point spend?
* [ ] **`AC-FEAT-003-07`**: Is there a visible error/disabled state when points are insufficient?
* [ ] **`AC-FEAT-003-08`**: Are out-of-stock items visually differentiated and un-redeemable?
