# Rewards Application UI & Component Design System (design.md)

Status: Canonical Component Architecture & Layout Specifications  
Linked References: [Brand Kit & Tokens](file:///Users/jclagudas/Downloads/rewardsapp/docs/design/brand-kit.md) | [FEAT-003 Design Brief](file:///Users/jclagudas/Downloads/rewardsapp/docs/design/briefs/feat-003-rewards-catalog-brief.md) | [Acceptance Criteria Traceability](file:///Users/jclagudas/Downloads/rewardsapp/docs/traceability.md)

---

## 1. Global Shell & Navigation Architecture

The application adopts a responsive, app-like layout structure designed to keep points visibility persistent and rewards discovery front-and-center.

```
+-----------------------------------------------------------------------------------------+
| [Logo] RewardsApp           [Browse Rewards]  [My Orders]      [⭐ 450 Points]  [User]   | <- Top Nav Shell
+-----------------------------------------------------------------------------------------+
|                                                                                         |
|  < Main Application Viewport: max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 >                   |
|                                                                                         |
|  +-----------------------------------------------------------------------------------+  |
|  | Page Header: Title, Subtitle, Filter/Sort Pills                                   |  |
|  +-----------------------------------------------------------------------------------+  |
|                                                                                         |
|  +-----------------------------------------------------------------------------------+  |
|  | Card Grid (1 col on mobile, 2 cols on tablet, 3-4 cols on desktop)                |  |
|  +-----------------------------------------------------------------------------------+  |
|                                                                                         |
|  +-----------------------------------------------------------------------------------+  |
|  | Centered Pagination Bar (Previous, Page X of Y, Next)                             |  |
|  +-----------------------------------------------------------------------------------+  |
|                                                                                         |
+-----------------------------------------------------------------------------------------+
```

### 1.1 Responsive Breakpoints
* **Mobile (`< 768px`)**: Single-column card stack, full-width touch targets ($44\text{px}$ minimum), sticky top bar with compact points pill.
* **Tablet (`768px – 1023px`)**: 2-column card grid, standard top navigation.
* **Desktop (`≥ 1024px`)**: 3 or 4-column card grid ($1200\text{px}$ max container width).

---

## 2. Component Design & Anatomy

### 2.1 Customer Points Balance Badge (`PointsChip`)
* **Role**: Primary indicator of purchasing power, visible across all customer pages.
* **Visual Tokens**:
  * Background: `var(--color-points-50)` (`#FFFBEB`)
  * Border: `1px solid var(--color-points-100)` (`#FEF3C7`)
  * Label: `var(--color-points-700)` (`#B45309`), font weight `600`, `font-variant-numeric: tabular-nums`
  * Icon: Coin / Star SVG in `#F59E0B`
* **Interaction**: Clicking opens a quick ledger dropdown showing recent point accruals and expirations.

---

### 2.2 Reward Product Card (`RewardCard`)
Each card is an interactive tile representing an available reward item:

```
+-------------------------------------------------------+
|  +-------------------------------------------------+  |
|  |                                                 |  |
|  |             [ Product Image / Icon ]            |  | <- 4:3 Aspect Ratio Container
|  |                                                 |  |
|  +-------------------------------------------------+  |
|                                                       |
|  [⭐ 250 Points]                       [45 in stock]  | <- Points Badge & Stock Badge
|                                                       |
|  Stainless Steel Tumbler                              | <- H3 Semibold (18px)
|  500ml double-wall insulated water tumbler. Keeps     | <- Body Regular (14px, 2-line clamp)
|  beverages hot or cold for hours...                   |
|                                                       |
|  +-------------------------------------------------+  |
|  |                Redeem Reward                    |  | <- Primary Button (bg-indigo-600)
|  +-------------------------------------------------+  |
+-------------------------------------------------------+
```

#### States:
1. **Default**: `border: 1px solid var(--color-border-default)`, `shadow-sm`.
2. **Hover**: Smooth elevation shift to `shadow-md`, border highlight to `var(--color-primary-500)`.
3. **Out of Stock**: Opacity `0.6`, grayscale image, stock badge in slate (`Out of Stock`), CTA disabled (`AC-FEAT-003-08`).

---

### 2.3 Quantity Input Stepper (`InputStepper`)
Used inside modals and administrative adjustment rows:

```
[  —  ]      2      [  +  ]
 (btn)    (number)   (btn)
```
* **Minus Button**: Disabled when `current_quantity <= 1`.
* **Value Field**: Centered, `font-weight: 700`, `tabular-nums`.
* **Plus Button**: Disabled when `current_quantity >= available_stock` or when customer's point balance is insufficient for another unit.

---

### 2.4 The Redemption Modal Dialog (`RedemptionModal`)
The focus modal triggered when redeeming a product:

```
+-------------------------------------------------------------------+
|  Confirm Redemption                                          [X]  |
+-------------------------------------------------------------------+
|                                                                   |
|  [ Product Thumbnail ]   Stainless Steel Tumbler                  |
|                          ⭐ 250 Points per item                   |
|                                                                   |
|  500ml double-wall insulated water tumbler. Keeps beverages       |
|  hot for 12 hours or cold for 24 hours. Premium matte finish.     |
|                                                                   |
|  ---------------------------------------------------------------  |
|                                                                   |
|  Quantity to Redeem:                                              |
|  [ — ]      2      [ + ]            (45 items available)          |
|                                                                   |
|  ---------------------------------------------------------------  |
|                                                                   |
|  Cost Calculation:                                                |
|  2 items  ×  250 points            =  500 Points                  |
|  Your Available Balance:              450 Points                  |
|                                                                   |
|  +-------------------------------------------------------------+  |
|  | ⚠️ Insufficient Points: You need 50 more points.            |  | <- Error Alert Box
|  +-------------------------------------------------------------+  |
|                                                                   |
|  +-----------------------------+ +-----------------------------+  |
|  |           Cancel            | |    Buy Now (500 Points)     |  | <- Action Buttons
|  +-----------------------------+ +-----------------------------+  |
+-------------------------------------------------------------------+
```

#### Modal Rules & State Transitions:
1. **Open Trigger**: Triggered on card click; backdrop blurs main content (`backdrop-filter: blur(4px)`).
2. **Dynamic Points Math**:
   $$\text{Total Required} = \text{Selected Quantity} \times \text{Unit Points Cost}$$
3. **Validation & Guard**:
   * If $\text{Total Required} \le \text{Available Points}$: "Buy Now" button active in primary indigo.
   * If $\text{Total Required} > \text{Available Points}$: Amber/Red warning banner appears, "Buy Now" button disabled.
4. **Cancel Flow**: Closes dialog with zero modifications (**`AC-FEAT-003-05`**).
5. **Execution Flow**: Submits POST request, displays inline spinner, updates points balance, and displays success state (**`AC-FEAT-003-06`**).

---

## 3. UI State Machines & Empty States

| State | Visual Treatment | Trigger |
| --- | --- | --- |
| **Loading Skeleton** | Shimmer pulse boxes for images, titles, and buttons | Initial catalog fetch or pagination switch |
| **Empty Catalog** | Centered gift illustration, "No rewards currently available" | Database contains 0 enabled items |
| **Out of Stock** | Item dimmed, "Out of Stock" chip, modal trigger disabled | `available_quantity == 0` |
| **Redemption Success** | Checkmark celebration icon, "Item Redeemed Successfully!" | Completed API transaction |
| **API Error** | Floating toast notification with retry button | Network disconnection or server 500 |

---

## 4. Accessibility & Micro-Interactions
* **Keyboard Focus**: Focus visible rings (`outline: 2px solid #6366F1`) on cards, stepper buttons, and dialog CTAs.
* **Escape Key**: Pressing `Escape` closes the modal immediately.
* **Screen Reader Semantics**: `role="dialog"`, `aria-modal="true"`, `aria-labelledby="dialog-title"`.
