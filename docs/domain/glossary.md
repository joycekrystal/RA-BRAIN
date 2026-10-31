# Domain Glossary

This document establishes the official terminology, business definitions, and system concepts for the Rewards Application.

| Term | Definition | Context / Constraints |
| --- | --- | --- |
| **Customer** | An end-user who registers and shops on the platform, earns loyalty points, and redeems them for reward products. | Role identifier: `CUSTOMER`. Can be enabled or disabled by staff. |
| **Staff / Admin** | An administrative internal user with privileges to manage customers, configure system ratios, and manage reward inventory. | Role identifier: `STAFF`. Has access to backoffice administration. |
| **Reward Point** | The virtual currency earned by customers and redeemed for products in the rewards catalog. | Unit of value; non-negative balance. |
| **Cost-to-Points Ratio** | The rate defining how many Philippine Pesos (PHP) must be spent on a purchase to earn 1 reward point (e.g., $100\text{ PHP} = 1\text{ Point}$). | Configurable by Staff in the admin console. |
| **Birthday Reward** | A promotional grant of reward points delivered to a customer during their registered birth month. | Granted once per calendar year in the customer's birthday month. |
| **Reward Product** | A catalog item available for acquisition exclusively using reward points. | Contains: Name, Description, Points Cost, Available Quantity, and Visibility Status (Enabled/Disabled). |
| **Available Quantity (Stock)** | The current count of physical or digital units of a reward product remaining in inventory. | Decremented upon successful redemption; adjustable by Staff. Cannot drop below zero. |
| **Product Visibility (Enabled/Disabled)** | A binary flag that controls whether a reward product is visible and purchasable in the customer-facing catalog. | `ENABLED`: Visible and purchasable if stock $> 0$. `DISABLED`: Hidden from customer catalog. |
| **Customer Status (Enabled/Disabled)** | A binary flag controlling whether a customer can log in, accrue points, or redeem rewards. | `ENABLED`: Normal operation. `DISABLED`: Account blocked from authentication/transactions. |
| **Redemption Order** | A completed transaction where a customer spends points to acquire one or more units of a reward product. | Records customer ID, product ID, quantity, total points deducted, and timestamp. |
| **Input Stepper** | A user interface control featuring increment (+) and decrement (-) buttons alongside a numeric field to select item quantities in the redemption modal. | Enforces minimum of 1 and maximum limited by customer's point balance and available stock. |
| **Session Expiration** | The duration after which an active authenticated browser/app session terminates (configured to 6 hours). | Requires session renewal or re-authentication. |
| **Access Token Expiration** | The maximum lifespan of an issued JWT/access token (configured to 1 day). | Defines the maximum token validity window. |
| **Access Token Idle Expiration** | Inactivity timeout for the access token (configured to 2 days). | Token invalidated if unused across the idle window. |
| **Refresh Token Expiration** | The absolute maximum lifespan of a refresh token (configured to 30 days). | Absolute expiration ceiling requiring complete re-login. |
| **Refresh Token Idle Expiration** | Inactivity timeout for a refresh token (configured to 7 days). | Token revoked if no refresh requests occur within 7 days. |
