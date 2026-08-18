# Swag Labs (saucedemo.com) — QA & Automation Project

## Project Overview
This repository contains manual QA testing artifacts (test plan, bug reports) and Selenium WebDriver automation for [Swag Labs](https://www.saucedemo.com), a demo e-commerce application used for QA/SDET practice.

The project covers:
- A structured test plan (scope, test types, environment, test data, test cases, risk assessment)
- 5 genuine bugs discovered through manual exploratory testing
- Automated Selenium test suite (Python + pytest) covering login, checkout, and negative login scenarios

---

## Requirements
- Python 3.10+ (tested on Python 3.14.5)
- Google Chrome (latest stable version)
- pip

---

## Installation

1. Clone this repository:
   ```bash
   git clone <repo-url>
   cd saucedemo-qa
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # macOS/Linux
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## How to Run Tests

Run the full test suite:
```bash
pytest tests/ -v
```

Run an individual test file:
```bash
pytest tests/test_login.py -v
pytest tests/test_checkout.py -v
pytest tests/test_locked_user.py -v
```

---

## Browser Requirements
Tests use Selenium's built-in Chrome WebDriver management (via the `selenium` package's `webdriver.Chrome()`), which automatically resolves the correct ChromeDriver version for the installed Chrome browser. Ensure Google Chrome is installed and up to date.

---

## Test Coverage

| Test File | Flow Covered | Status |
|---|---|---|
| `tests/test_login.py` | Valid login with `standard_user`, verifies redirect to inventory page | ✅ Passing |
| `tests/test_checkout.py` | Add item to cart → view cart → checkout → fill info → finish → verify order completion | ✅ Passing |
| `tests/test_locked_user.py` | Login with `locked_out_user`, verifies correct lockout error message | ✅ Passing |

All 3 tests pass when run individually and as a full suite (`pytest tests/ -v`).

---

## Project Structure

```
saucedemo-qa/
├── README.md          # This file
├── test_plan.md        # Full test plan: scope, test types, environment, test data, test cases, risk assessment
├── bug_reports.md      # 5 documented bugs found via manual exploratory testing
├── requirements.txt    # Python dependencies
└── tests/
    ├── test_login.py        # Automated: valid login flow
    ├── test_checkout.py     # Automated: add to cart → checkout flow
    └── test_locked_user.py  # Automated: locked-out user negative test
```

---

## Notes
- Manual exploratory testing was performed primarily using `standard_user` and `problem_user` accounts, which surfaced 5 distinct bugs (see `bug_reports.md`).
- Automation was found to occasionally show timing flakiness when all three tests run back-to-back (resolved by increasing explicit wait timeout on the order-confirmation assertion). This reflects a common real-world Selenium challenge and was handled via a longer explicit wait rather than a fixed sleep.
- See `test_plan.md` for full details on test types, environment, and risk prioritization.
