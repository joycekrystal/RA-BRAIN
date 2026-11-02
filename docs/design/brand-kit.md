# Rewards Application Brand Kit & Design System Foundations

Status: Canonical Design System Reference  
Last Updated: 2026-11-02  
Applicable Features: All Application Interfaces (Customer & Staff)

---

## 1. Brand Identity & Visual Philosophy
The **Rewards Application** brand conveys **delight, tangible value, trust, and premium simplicity**. Earning and spending loyalty points should feel rewarding, tactile, and effortless.

* **Primary Tone**: Clean, modern, uplifting, and transparent.
* **Key Visual Motif**: Points and rewards should feel like valuable digital achievements. Accent gold and vivid indigo highlight reward currency, while crisp neutrals provide high legibility and structure.

---

## 2. Color Palette & Design Tokens

### 2.1 Brand & Action Palette
| Token Name | Hex Code | Tailwind Token | Semantic Usage |
| --- | --- | --- | --- |
| `--color-primary-50` | `#EEF2FF` | `indigo-50` | Light interactive hover states, selected card background |
| `--color-primary-100` | `#E0E7FF` | `indigo-100` | Subtle chips, inactive stepper track |
| `--color-primary-500` | `#6366F1` | `indigo-500` | Accent borders, focused input rings |
| `--color-primary-600` | `#4F46E5` | `indigo-600` | **Primary Brand Color**: Primary buttons, active tabs, main links |
| `--color-primary-700` | `#4338CA` | `indigo-700` | Button hover and pressed states |

### 2.2 Points & Currency Palette (The "Rewards" Glow)
| Token Name | Hex Code | Tailwind Token | Semantic Usage |
| --- | --- | --- | --- |
| `--color-points-50` | `#FFFBEB` | `amber-50` | Points balance chip background, reward card highlight |
| `--color-points-100` | `#FEF3C7` | `amber-100` | Points container border |
| `--color-points-500` | `#F59E0B` | `amber-500` | Points coin icon, star badge, points reward visual |
| `--color-points-600` | `#D97706` | `amber-600` | Points text on light backgrounds (WCAG AA contrast) |
| `--color-points-700` | `#B45309` | `amber-700` | High-emphasis points numbers |

### 2.3 Neutrals & Backgrounds (Slate Spectrum)
| Token Name | Hex Code | Tailwind Token | Semantic Usage |
| --- | --- | --- | --- |
| `--color-bg-canvas` | `#F8FAFC` | `slate-50` | Page backdrop / application canvas |
| `--color-bg-surface` | `#FFFFFF` | `white` | Card surface, modal dialog background, popovers |
| `--color-border-subtle` | `#F1F5F9` | `slate-100` | Card dividers, secondary separators |
| `--color-border-default` | `#E2E8F0` | `slate-200` | Standard card borders, input borders, pagination borders |
| `--color-border-strong` | `#CBD5E1` | `slate-300` | Stepper button borders, active input borders |
| `--color-text-primary` | `#0F172A` | `slate-900` | Headings, product titles, dialog headers |
| `--color-text-secondary` | `#475569` | `slate-600` | Body copy, card descriptions, pagination status |
| `--color-text-muted` | `#94A3B8` | `slate-400` | Helper text, disabled buttons, placeholder text |

### 2.4 Semantic Feedback & Statuses
| State | Light / Background | Core / Text | Semantic Meaning |
| --- | --- | --- | --- |
| **Success** | `#ECFDF5` (`emerald-50`) | `#059669` (`emerald-600`) | Redemption success, in-stock indicator |
| **Warning** | `#FFFBEB` (`amber-50`) | `#D97706` (`amber-600`) | Low stock badge (< 5 left) |
| **Error / Danger** | `#FEF2F2` (`red-50`) | `#DC2626` (`red-600`) | Insufficient points alert, out-of-stock badge, account disabled |

---

## 3. Typography Scale

* **Primary Font Family**: `Inter`, `-apple-system`, `BlinkMacSystemFont`, `Segoe UI`, `sans-serif`
* **Numeric Font Variant**: `font-variant-numeric: tabular-nums` (ensures points and quantities align cleanly in steppers and tables without shifting layout).

| Level | Size / Line Height | Weight | Tracking | Usage |
| --- | --- | --- | --- | --- |
| **Display / H1** | `30px / 38px` | `700 (Bold)` | `-0.02em` | Main page titles (e.g., "Rewards Catalog") |
| **Heading / H2** | `24px / 32px` | `600 (Semibold)` | `-0.015em` | Modal titles, section headings |
| **Heading / H3** | `18px / 26px` | `600 (Semibold)` | `-0.01em` | Product card titles, admin card titles |
| **Body Large** | `16px / 24px` | `500 (Medium)` | `0` | Points balance chip, stepper numbers, button labels |
| **Body Regular** | `14px / 20px` | `400 (Regular)` | `0` | Product descriptions, modal copy, table rows |
| **Body Small** | `12px / 16px` | `500 (Medium)` | `+0.01em` | Badges, stock counter, pagination labels, input helper text |

---

## 4. Spacing, Radii & Elevations

### 4.1 Spacing Scale (4px Base Grid)
`4px` (`spacing-1`), `8px` (`spacing-2`), `12px` (`spacing-3`), `16px` (`spacing-4`), `20px` (`spacing-5`), `24px` (`spacing-6`), `32px` (`spacing-8`), `48px` (`spacing-12`).

### 4.2 Border Radii (Soft Modern Feel)
* `--radius-sm`: `6px` (Badges, tags)
* `--radius-md`: `10px` (Input fields, stepper buttons, secondary buttons)
* `--radius-lg`: `16px` (Reward product cards, dropdown menus)
* `--radius-xl`: `24px` (Redemption modal dialog, hero sections)
* `--radius-full`: `9999px` (Pill badges, customer points balance chip)

### 4.3 Elevation & Shadows
* **Level 1 (`shadow-sm`)**: `0 1px 2px 0 rgba(0, 0, 0, 0.05)` — Neutral card borders, inputs.
* **Level 2 (`shadow-md`)**: `0 4px 6px -1px rgba(0, 0, 0, 0.08), 0 2px 4px -2px rgba(0, 0, 0, 0.04)` — Card hover state, dropdowns.
* **Level 3 (`shadow-xl`)**: `0 20px 25px -5px rgba(0, 0, 0, 0.12), 0 8px 10px -6px rgba(0, 0, 0, 0.08)` — Redemption popup modal.

---

## 5. Reusable Component Specifications

### 5.1 The Customer Points Balance Chip
* **Visual**: Pill-shaped badge displayed in the navigation bar/header.
* **Appearance**: Background `--color-points-50`, border `1px solid --color-points-100`.
* **Content**: Sparkle/Coin icon (`#F59E0B`) + **`450 Points Available`** in `--color-points-700` (`font-weight: 600`).

### 5.2 The Reward Product Card
* **Container**: White background, `1px solid var(--color-border-default)`, `border-radius: 16px`, `padding: 20px`.
* **Hover State**: Elevates to `shadow-md`, subtle border transition to `var(--color-primary-500)`.
* **Header / Image area**: 1:1 or 4:3 product thumbnail or gift illustration placeholder.
* **Badges**:
  * Points Cost: Amber pill badge (e.g., `⭐ 250 Points`).
  * Stock Badge: Emerald pill if $>5$ (e.g., `45 in stock`), Amber pill if $\le 5$ (e.g., `Only 2 left!`), Slate pill if 0 (`Out of Stock`).
* **Title & Description**: 2-line title truncate (`text-slate-900`), 3-line description clamp (`text-slate-600`).
* **Action**: "Redeem Reward" button or full card clickable tap target.

### 5.3 The Quantity Input Stepper
* **Container**: Pill or rounded-md container with light slate border.
* **Controls**:
  * Decrement Button (`-`): 36px $\times$ 36px touch target; disabled when `quantity <= 1`.
  * Numeric Value: 48px width, centered, bold `tabular-nums`.
  * Increment Button (`+`): 36px $\times$ 36px touch target; disabled when `quantity >= max_available` or customer lacks points.

### 5.4 The Redemption Modal Dialog
* **Backdrop**: Semi-transparent dark blur (`rgba(15, 23, 42, 0.5)` with `backdrop-filter: blur(4px)`).
* **Modal Body**: Centered, max-width `480px`, radius `24px`, padding `32px`.
* **Footer**: Two distinct buttons side-by-side:
  * "Cancel": Secondary ghost/outline button (`color: slate-600`, hover `bg-slate-100`).
  * "Buy / Confirm Redemption": High-contrast primary button (`bg-indigo-600`, text `white`, hover `bg-indigo-700`).

---

## 6. Accessibility & Contrast Standards
* All text tokens meet **WCAG 2.1 AA** contrast standards ($> 4.5:1$ for normal text, $> 3:1$ for large text).
* Interactive elements have explicit `:focus-visible` outline rings (`2px solid #6366F1`, `offset: 2px`).
* All icons paired with meaningful labels for screen readers.
