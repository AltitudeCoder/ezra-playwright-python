# 🧪 Ezra QA Automation — Playwright (Python)

Automated tests built with **Playwright + Pytest** for Ezra’s staging environment.  
These scripts validate critical user flows such as **New Member Account creation** and **Selecting a Scan**.

---

## ⚙️ Setup Instructions

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
python -m playwright install chromium
```

### 4 Run tests
```bash
python -m pytest -s --browser=chromium --headed -n 1
```

### 5 To run a specific test:
```bash
python -m pytest -s tests/test_new_member_account.py --browser=chromium --headed
```

## 📁 Project Structure
```bash
ezra-playwright-python/
│
├── tests/
│   ├── test_new_member_account.py     # Creates a new account (Join flow)
│   ├── test_scan_select.py            # Logs in, books scan, selects plan
│
├── pytest.ini                         # Pytest config
├── requirements.txt                   # Dependencies
├── .gitignore                         # Files to ignore in Git
└── README.md                          # This file
```

## ⚖️ Trade-offs & Assumptions

**1. Authentication**

* Assumes the staging login is required for protected routes.

* Uses a single shared test user for simplicity.

- 🔁 Future improvement: use environment variables for credentials (```bashos.getenv()```).

**2. Selectors**

* Prefers ```bash id```, ```bash data-test```, or ```bash get_by_role()``` selectors.

* Where unavailable, uses text or class-based locators.

- ⚠️ May break if frontend markup changes; adding ```bashdata-test``` attributes would improve reliability.

**3. Waiting Strategy**

* Uses Playwright’s smart waiting (```bash expect(...).to_be_visible```, ```bash wait_until="domcontentloaded"```).

* Avoids long ```bash sleep()``` calls — short, targeted waits only.

**4. Randomized Data**

* Random first/last names, emails, and phone numbers for each run.

* Prevents duplicate user creation conflicts.

- Logs randomized data for easy debugging.

**5. Scope**

* Focuses on end-user journey validation (UI layer).

* Does not cover API or database verification at this stage.

### 🚀 Scalability & Future Enhancements
| Area | Next Steps |	Benefits | 
| :------------- | :------------- |:------------- |
| **Page Object Model (POM)**| Create `/pages/` directory and move locators/actions into classes| Improves readability, reduces duplication|
| **Environment Configs**|	Add `config.py` or `.env` for URLs & creds | Easier multi-env testing (staging/prod)
| **Reporting**|	Integrate Allure or pytest-html |	Produces shareable visual reports
| **CI/CD Integration**|	Add `.github/workflows/ci.yml` |	Auto-run tests on pull requests
| **Selectors**|	Use `data-test` attributes |	Prevents brittle locator failures |


## 🧱 Design Notes

* Language: Python 3.12+

* Frameworks: Playwright, Pytest

- Execution Mode: Headed by default (easy visual verification)

+ Parallelization: Limited to `-n 1` (ensures predictable sequencing)

+ Stability: Deterministic waits, no arbitrary sleep calls

## 🧩 Future Implementation Ideas

* Data-driven tests (parametrize across different plans or user types)

* Visual regression comparison for UI elements

- API-layer validation before UI submission

- Integration with Slack or email alerts for CI failures

+ Docker containerization for consistent environment setup


