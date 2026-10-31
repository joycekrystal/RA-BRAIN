# Feature Specification: FEAT-001 Authentication & Access Control

## 1. Metadata
* **Feature ID**: `FEAT-001`
* **Title**: User Authentication, Password Policy & Token Lifecycle
* **Status**: In Review / Specified
* **Owner**: Core Engineering / Security Team
* **Source Link**: [Confluence - Features (Page ID: 163976)](https://joycekrystallagudas.atlassian.net/wiki/spaces/~5add6ce37b296356232d7884/pages/163976/Features)
* **Last Verified Date**: 2026-10-31

---

## 2. Business Outcome & Success Measure
Provides secure, standards-compliant authentication and authorization for both Customers and Staff members, ensuring robust credential security and granular session lifetime control to protect user point balances and back-office management.

---

## 3. Users & Target Personas
* **Customer**: Logs in to review point balances, browse rewards, and redeem items.
* **Staff**: Logs in to access administrative customer management and catalog configuration.

---

## 4. Scope
* **In-Scope**:
  * User login with email as username.
  * Password complexity validation (minimum 8 characters, special character, numbers, uppercase letter, lowercase letter).
  * Role-based access control (Staff and Customer privileges).
  * Token expiration and sliding-window idle timeouts (Session: 6h; Access token: 1d active, 2d idle; Refresh token: 30d max, 7d idle).
  * Account active status verification (enabled vs. disabled).
* **Out-of-Scope**:
  * Third-party social OAuth (Google, Facebook) - deferred to future iterations.
  * Biometric WebAuthn authentication.

---

## 5. Domain Rules & Policies
1. **Identifier**: Username must always be a valid, normalized RFC 5322 email address.
2. **Password Complexity**:
   * Minimum length: 8 characters.
   * At least 1 lowercase alphabetical character (`[a-z]`).
   * At least 1 uppercase alphabetical character (`[A-Z]`).
   * At least 1 numeric digit (`[0-9]`).
   * At least 1 special character (`[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]`).
3. **Roles & Permissions**:
   * `STAFF`: Access to Admin API routes (`/api/v1/admin/*`) and back-office UI.
   * `CUSTOMER`: Access to Customer API routes (`/api/v1/rewards/*`, `/api/v1/customers/me/*`).
4. **Token & Session Timing**:
   * Session duration: 6 hours.
   * Access Token lifespan: 1 day (24 hours).
   * Access Token idle timeout: 2 days (48 hours).
   * Refresh Token lifespan: 30 days maximum.
   * Refresh Token idle timeout: 7 days.
5. **Disabled Accounts**:
   * If a user has `is_enabled = false`, authentication attempts must fail with an account disabled error.

---

## 6. Numbered Acceptance Criteria

* **AC-FEAT-001-01 (Email as Username)**: Given a login attempt, when a user enters their credentials, then the system must treat the entered username as an email address and reject non-email strings with a validation error.
* **AC-FEAT-001-02 (Password Validation Rules)**: Given a user registration or password reset, when a user enters a password, the system must enforce:
  * Minimum 8 characters.
  * At least 1 lowercase letter.
  * At least 1 uppercase letter.
  * At least 1 number.
  * At least 1 special character.
  Passwords not matching all criteria must be rejected with descriptive guidance.
* **AC-FEAT-001-03 (Role Segregation)**: Given an authenticated user, when the user possesses the `STAFF` role, then they can access admin features; when the user possesses the `CUSTOMER` role, admin routes must return HTTP 403 Forbidden.
* **AC-FEAT-001-04 (Account Status Check)**: Given a user account where `is_enabled` is set to `false`, when that user attempts to log in, the authentication must fail with HTTP 403 / "Account disabled" and issue no tokens.
* **AC-FEAT-001-05 (Session Lifetime Enforced)**: Given an active user session, when 6 hours elapse from session initiation, the session must expire and require re-authentication or session refresh.
* **AC-FEAT-001-06 (Access Token Lifecycle)**: Given an issued access token, it must remain valid for exactly 1 day (24h) under active use, and be invalidated if unused across a 2-day (48h) idle window.
* **AC-FEAT-001-07 (Refresh Token Lifecycle)**: Given an issued refresh token, when used within 7 days of the previous activity, it successfully issues a new access token; if idle for $> 7$ days or if total age exceeds 30 days, the token must be revoked and the user prompted to log in.

---

## 7. API Contract Draft

### `POST /api/v1/auth/login`
**Request Body**:
```json
{
  "email": "customer@example.com",
  "password": "Password123!"
}
```
**Response (200 OK)**:
```json
{
  "access_token": "jwt.token.here",
  "refresh_token": "uuid-or-refresh-token",
  "token_type": "Bearer",
  "expires_in": 86400,
  "user": {
    "id": "c1f7b02e-9d22-482d-8e6d-6fd21d3f0a14",
    "email": "customer@example.com",
    "role": "CUSTOMER"
  }
}
```

### `POST /api/v1/auth/refresh`
**Request Body**:
```json
{
  "refresh_token": "uuid-or-refresh-token"
}
```
**Response (200 OK)**:
```json
{
  "access_token": "new.jwt.token",
  "refresh_token": "new-or-rotated-refresh-token",
  "expires_in": 86400
}
```
