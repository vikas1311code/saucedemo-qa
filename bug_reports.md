# Bug Reports — Swag Labs (saucedemo.com)

Testing performed on: August 17, 2026
Environment: Google Chrome, Windows
Tested by: Vikas Pandey

---

## BUG-001: Zip/Postal Code field accepts alphabetic characters with no format validation

- **User/Role:** standard_user
- **Environment:** Chrome, Windows
- **Preconditions:** Item(s) added to cart, user on Checkout Step One (Your Information) page
- **Steps to Reproduce:**
  1. Add any product(s) to cart
  2. Go to Cart → Checkout
  3. Enter valid First Name and Last Name
  4. Enter Zip/Postal Code as `sbjksdw` (letters only, no digits)
  5. Click Continue → proceed through checkout → Finish
- **Expected Result:** System should validate postal code format and reject non-numeric/invalid input
- **Actual Result:** Field accepts pure alphabetic input, checkout proceeds to completion, and order is confirmed/dispatched (per order receipt) without any validation error
- **Severity:** Low–Medium
- **Priority:** Medium
- **Affected Feature:** Checkout — Your Information form validation
- **User Impact:** Orders can be placed with invalid shipping data, which could cause real-world delivery failures
- **Evidence:** Order confirmation receipt (PDF) showing postal code "sbjksdw" accepted; order total correctly calculated ($75.56)

---

## BUG-002: Incorrect/identical product images shown for all items

- **User/Role:** problem_user
- **Environment:** Chrome, Windows
- **Preconditions:** Logged in as problem_user
- **Steps to Reproduce:**
  1. Login with username `problem_user` / password `secret_sauce`
  2. Navigate to Products (inventory) page
  3. Observe product images for each item
- **Expected Result:** Each product should display its own correct, distinct image matching its name/description
- **Actual Result:** All products display the same identical image (a dog holding a tennis ball) regardless of product name/type
- **Severity:** High
- **Priority:** High
- **Affected Feature:** Product listing / Product images
- **User Impact:** Users cannot visually verify products before purchase; could lead to wrong orders and damages brand trust
- **Evidence:** Screenshot showing identical dog image across all products on the inventory page

---

## BUG-003: Removing item from Products page does not sync/update the Cart

- **User/Role:** problem_user
- **Environment:** Chrome, Windows
- **Preconditions:** Logged in as problem_user, one item added to cart from the Products page
- **Steps to Reproduce:**
  1. Login as problem_user
  2. On Products page, click "Add to cart" for any item (button changes to "Remove")
  3. Note cart badge count (increases by 1)
  4. On the same Products page, click "Remove" for that item
  5. Check cart badge count and open the cart
- **Expected Result:** Item should be removed from cart; cart count should decrease and the item should not appear in the cart
- **Actual Result:** Cart still shows the item as added — count does not update and item still exists in the cart. Removing the same item directly from the Cart page works correctly.
- **Severity:** High
- **Priority:** High
- **Affected Feature:** Cart / Product listing "Remove" action
- **User Impact:** Users may believe an item is removed but it still remains in their cart, potentially leading to unwanted purchases
- **Evidence:** Screenshots of cart badge count before/after Remove action from Products page

---

## BUG-004: Clicking a product opens the details page of a different product

- **User/Role:** problem_user
- **Environment:** Chrome, Windows
- **Preconditions:** Logged in as problem_user, on Products page
- **Steps to Reproduce:**
  1. Login as problem_user
  2. On Products page, click on "Sauce Labs Backpack" ($29.99)
- **Expected Result:** Product detail page for Sauce Labs Backpack ($29.99) should open
- **Actual Result:** Product detail page for "Sauce Labs Fleece Jacket" ($49.99) opens instead — wrong product name, image, and price shown
- **Severity:** Critical
- **Priority:** High
- **Affected Feature:** Product navigation / Product detail page routing
- **User Impact:** Customer may unknowingly view or purchase a completely different, more expensive product than intended
- **Evidence:** Screenshot of detail page URL/content mismatch when clicking Backpack

---

## BUG-005: Sorting dropdown options (Name Z-A, Price low-high, Price high-low) unresponsive

- **User/Role:** problem_user
- **Environment:** Chrome, Windows
- **Preconditions:** Logged in as problem_user, on Products page
- **Steps to Reproduce:**
  1. Login as problem_user
  2. Click sort dropdown, select "Name (Z to A)" / "Price (low to high)" / "Price (high to low)" one at a time
- **Expected Result:** Product list should re-sort according to the selected option
- **Actual Result:** Only "Name (A to Z)" applies correctly. The other three sort options do not change the product order when selected.
- **Severity:** Medium
- **Priority:** Medium
- **Affected Feature:** Product sorting/filtering
- **User Impact:** Users cannot sort by price, a commonly used shopping/comparison feature
- **Evidence:** Screenshots of dropdown selection with no change in product order

---

## Severity Definitions Used

- **Critical:** Blocks core functionality or causes incorrect transactions/data (e.g., wrong product delivered/ordered). No usable workaround.
- **High:** Major feature broken or misleading, but the app doesn't completely halt; has significant user/business impact.
- **Medium:** Feature partially broken or inconvenient; workaround exists, impact is moderate.
- **Low:** Minor/cosmetic issue with minimal user impact.

## Priority Definitions Used

- **High:** Should be fixed before next release — affects core flows or data integrity.
- **Medium:** Should be fixed soon but doesn't block release.
- **Low:** Fix when convenient; minimal impact on users.
