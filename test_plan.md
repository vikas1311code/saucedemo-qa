# Test Plan — Swag Labs (saucedemo.com)

## 1. Introduction
This document outlines the test strategy, scope, environment, test data, test cases, and risk assessment for QA testing of the Swag Labs e-commerce demo application (https://www.saucedemo.com).

---

## 2. Scope

In-scope areas for this testing cycle:

- **Login** — authentication for all provided user roles
- **Product Browsing** — inventory listing, sorting/filtering
- **Product Details** — individual product detail page
- **Shopping Cart** — add/remove items, cart state management
- **Checkout** — information form, order summary, order completion

Out of scope: performance/load testing beyond basic observation, security penetration testing, accessibility (WCAG) audit.

---

## 3. Types of Testing

| Type | Purpose |
|---|---|
| Functional Testing | Verify core features (login, add to cart, checkout) work per expected app behavior |
| UI Testing | Verify layout, images, text, buttons render correctly and consistently |
| Negative Testing | Verify app handles invalid/missing input gracefully (empty fields, invalid formats) |
| Edge-case Testing | Verify unusual but plausible flows (rapid clicks, back/forward navigation, repeated actions) |
| Cross-browser Testing | Verify consistent behavior across supported browsers |

---

## 4. Test Environment

**Browsers:**
- Google Chrome (primary — latest stable version)
- Mozilla Firefox
- Microsoft Edge

**Operating Systems:**
- Windows 10/11 (primary)
- macOS (secondary, if available)

**Desktop/Mobile Considerations:**
- Primary testing on desktop viewport
- Basic responsive check on mobile viewport (browser dev tools device emulation) — note any layout breakage separately, as this is a demo app not explicitly built mobile-first

---

## 5. Test Data

| User | Password | Purpose |
|---|---|---|
| standard_user | secret_sauce | Baseline functional testing — expected to work normally |
| locked_out_user | secret_sauce | Negative testing — verify login is blocked with correct error |
| problem_user | secret_sauce | UI/functional bug-hunting — known to have intentional defects |
| performance_glitch_user | secret_sauce | Performance observation — expect delayed page loads |

---

## 6. Test Cases

> Note: "Expected Result" below is based on normal, reasonable application behavior for an e-commerce checkout flow (standard UX conventions), not on invented specifics. "Actual Result" is filled in only from real testing — leave blank/TBD until you execute it yourself, or fill in what we've already confirmed together.

### TC-01: Valid Login — standard_user
- **Type:** Functional / Positive
- **Preconditions:** On login page
- **Steps:** Enter username `standard_user`, password `secret_sauce`, click Login
- **Expected Result:** User is redirected to Products (inventory) page
- **Actual Result:** *(confirmed working during exploratory testing)*

### TC-02: Invalid Login — locked_out_user
- **Type:** Functional / Negative
- **Preconditions:** On login page
- **Steps:** Enter username `locked_out_user`, password `secret_sauce`, click Login
- **Expected Result:** Login blocked; an error message is displayed indicating the user is locked out
- **Actual Result:** **Pass** — Login is blocked, error message displayed: "Epic sadface: Sorry, this user has been locked out."

### TC-03: Product Sort — Price (Low to High / High to Low)
- **Type:** Functional
- **Preconditions:** Logged in, on Products page
- **Steps:** Select each sort option from dropdown and observe order
- **Expected Result:** Products re-order correctly according to selected criteria
- **Actual Result:**
  - standard_user: **Pass** — all 4 sort options work correctly (verified)
  - problem_user: **Fail** — only "Name (A to Z)" applies; other 3 options unresponsive (BUG-005)

### TC-04: Add to Cart / Remove from Products Page
- **Type:** Functional
- **Preconditions:** Logged in, on Products page
- **Steps:** Click "Add to cart" on an item, verify cart count increases; click "Remove" on same item from Products page, verify cart count decreases and item is removed
- **Expected Result:** Cart state updates correctly for both add and remove actions, regardless of which page the action is performed from
- **Actual Result:**
  - standard_user: **Pass**
  - problem_user: **Fail** — Remove from Products page does not update cart (BUG-003)

### TC-05: Checkout — Mandatory Field Validation
- **Type:** Negative
- **Preconditions:** Item(s) in cart, on Checkout Step One page
- **Steps:** Leave First Name / Last Name / Zip-Postal Code fields empty (individually and together), click Continue
- **Expected Result:** Form should not proceed; an error message should indicate which field is missing
- **Actual Result:** **Pass** — verified errors: "Error: First Name is required" and "Error: Last Name is required" appear correctly when respective fields are empty

### TC-06: Checkout — Postal Code Format Validation
- **Type:** Negative / Edge-case
- **Preconditions:** Item(s) in cart, on Checkout Step One page, First/Last Name filled
- **Steps:** Enter non-numeric value (e.g., letters only) in Zip/Postal Code field, click Continue through to order completion
- **Expected Result:** System should validate the postal code format and reject clearly invalid values, or at minimum flag it
- **Actual Result:** **Fail** — alphabetic-only postal code ("sbjksdw") accepted with no validation; order completed successfully (BUG-001)

### TC-07: Product Detail Navigation Accuracy
- **Type:** Functional
- **Preconditions:** Logged in, on Products page
- **Steps:** Click on a specific product's name/image, verify the detail page shown matches the product clicked
- **Expected Result:** Detail page shows the same product (name, price, image) that was clicked
- **Actual Result:**
  - standard_user: **Pass**
  - problem_user: **Fail** — clicking "Sauce Labs Backpack" ($29.99) opens "Sauce Labs Fleece Jacket" ($49.99) detail page (BUG-004)

### TC-08: Product Image Accuracy
- **Type:** UI
- **Preconditions:** Logged in, on Products page
- **Steps:** Visually inspect each product's image against its name/description
- **Expected Result:** Each product displays a distinct, correct image
- **Actual Result:**
  - standard_user: **Pass**
  - problem_user: **Fail** — all products show an identical unrelated image (BUG-002)

*(Add more test cases as you continue testing — locked_out_user error text, performance_glitch_user load time observation, cross-browser checks, etc.)*

---

## 7. Risk Assessment

| Area | Risk Level | Reason |
|---|---|---|
| Checkout data validation | High | Confirmed gap — invalid postal code accepted, order still completes. Directly affects order fulfillment/shipping in a real system. |
| Cart state consistency (problem_user) | High | Remove action from Products page silently fails to update cart — could lead to unintended purchases if this pattern existed in production. |
| Product-to-detail-page routing (problem_user) | Critical | Wrong product opens on click — direct risk of customers viewing/ordering the wrong item. |
| Product image accuracy (problem_user) | High | Broken visual trust — customers can't identify what they're buying. |
| Sorting/filtering (problem_user) | Medium | Reduces usability but doesn't block core purchase flow. |
| Cross-browser rendering | Medium (untested) | Not yet verified across browsers — layout or JS behavior could differ. |
| Performance (performance_glitch_user) | Medium (untested) | Deliberately slow user — needs load-time observation before rating. |

**Prioritization rationale:** Issues that affect order accuracy or data integrity (wrong product shown, invalid data accepted) are ranked highest because they have direct real-world business impact (wrong shipments, undeliverable orders). UI-only issues (images) are high but slightly lower priority than flow-breaking ones. Usability issues (sorting) are medium — annoying but not blocking.

---

## 8. Notes
This test plan reflects testing performed as of August 17, 2026, on Chrome/Windows. Update "Actual Result" fields and Risk Assessment as further test cases are executed.
