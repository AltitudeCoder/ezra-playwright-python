#  Manual Test Cases

A list of 15 detailed manual test cases created as part of this challenge can be found here:

####  [Ezra_Test_Cases.md](./Ezra_Test_Cases.md)

The first three test cases include short descriptions explaining why I consider them the most critical.  
The remaining cases are listed in order of priority — from most to least important.

---

#  Ezra QA Automation — Playwright

Automated tests built with **Playwright + Pytest** for Ezra’s staging environment.  
These scripts validate critical user flows such as **New Member Account creation** and **Scan Selection flow**, following a Page Object Model (POM) architecture for scalability and maintainability.


##  Setup Instructions

### 1 Clone the repository
```bash
git clone https://github.com/AltitudeCoder/ezra-playwright-python.git
cd ezra-playwright-python
```

### 2 Create a virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```
### 3 Install dependencies
```bash
pip install -r requirements.txt
playwright install chromium
```

### 4 Run all tests
```bash
python -m pytest -s -v --browser=chromium --headed -n 1
```

### 5 To run a specific test:
```bash
python -m pytest -s -v tests/test_login_and_scan_select.py --browser=chromium --headed
```

##  Project Structure
```bash
ezra-playwright-python/
│
├── pages/                            # Page Object classes
│   ├── base_page.py                  # Common methods and helpers
│   ├── login_page.py                 # Login page actions & locators
│   ├── select_plan_page.py           # Scan selection page logic
│   └── join_page.py                  # New member account page
│
├── tests/                            # Test cases
│   ├── test_login_and_scan_select.py # Full login + scan selection flow
│   ├── test_new_member_account.py    # Join flow (account creation)
│
├── utils/                            # Configs and helpers
│   └── config.py                     # Environment URLs and constants
│
├── fixtures/                         # (Optional) Reusable pytest fixtures
│
├── pytest.ini                        # Pytest config
├── requirements.txt                  # Dependencies
├── .gitignore                        # Ignored files
├── Ezra_Test_Cases.md                # Manual test cases
├── Ezra_Question2.md                 # Written response section
└── README.md                         # This file
```

##  Architecture Overview

#### Framework:

* Python + Playwright + Pytest

* Page Object Model (POM) — promotes modularity and reusability

- Clear separation between test logic, page interactions, and configuration

#### Execution Model:

* Headed by default for visibility (--headed)

* Parallel execution limited (-n 1) for consistency

* Configurable through pytest.ini

##  Trade-offs & Assumptions

| Area               | Decision                                        | Rationale                                           |
| :------------------ | :--------------------------------------------- | :-------------------------------------------------- |
| **Authentication** | Shared staging test user                        | Simplifies E2E flows; can be replaced with env vars |
| **Selectors**      | Prioritize `data-test`, `id`, or semantic roles | Reduces flakiness, improves readability             |
| **Waits**          | Use Playwright’s auto-wait + `expect()`         | Eliminates arbitrary `sleep()` usage                |
| **Scalability**    | POM structure + config abstraction              | Easier to extend (add more flows/pages)             |
| **Reporting**      | Console logs for now                            | Easy to add pytest-html or Allure later             |


###  Scalability & Future Enhancements

| Area                    | Next Steps                        | Benefit                                   |
| ----------------------- | --------------------------------- | ----------------------------------------- |
| **Environment Configs** | Add `.env` or secrets manager     | Secure and flexible credential management |
| **Reporting**           | Integrate Allure or `pytest-html` | Visual reports for QA leadership          |
| **CI/CD**               | Add GitHub Actions workflow       | Auto-run tests on pull requests           |
| **Data-Driven Testing** | Parametrize test data             | Expand coverage efficiently               |
| **API Validation**      | Add API layer verification        | Cross-check UI responses for accuracy     |



##  Design Notes

* **Language:** Python 3.13

* **Frameworks:** Playwright, Pytest
  
- **Design Pattern:** Page Object Model (POM)
  
- **Execution:** Headed mode, single browser session
  
+ **Scope:** UI-level end-to-end flow coverage
  
+ **OS:** macOS (Chromium browser installed via Playwright)

##  Future Implementation Ideas

* Data-driven tests (parametrize across different plans or user types)

* Visual regression comparison for UI elements

- API-layer validation before UI submission

- Integration with Slack or email alerts for CI failures
