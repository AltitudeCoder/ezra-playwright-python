# 🧪 Ezra QA Automation — Playwright (Python)

Automated end-to-end tests built with **Playwright + Pytest** for Ezra’s staging environment.  
These scripts validate critical user flows such as **New Member Account creation** and **Scan Booking**.

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/ezra-playwright-python.git
cd ezra-playwright-python

Create a virtual environment
python3 -m venv .venv
source .venv/bin/activate

2️⃣ Create a virtual environment
python3 -m venv .venv
source .venv/bin/activate

3️⃣ Install dependencies
pip install -r requirements.txt
python -m playwright install chromium

4️⃣ Run tests
python -m pytest -s --browser=chromium --headed -n 1


To run a specific test:

python -m pytest -s tests/test_new_member_account.py --browser=chromium --headed

📁 Project Structure
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

⚖️ Trade-offs & Assumptions

Authentication

Assumes the staging login is required for protected routes.

Uses a single shared test user for simplicity.

🔁 Future improvement: use environment variables for credentials (os.getenv()).

Selectors

Prefers id, data-test, or get_by_role() selectors.

Where unavailable, uses text or class-based locators.

⚠️ May break if frontend markup changes; adding data-test attributes would improve reliability.

Waiting Strategy

Uses Playwright’s smart waiting (expect(...).to_be_visible, wait_until="domcontentloaded").

Avoids long sleep() calls — short, targeted waits only.

Randomized Data

Random first/last names, emails, and phone numbers for each run.

Prevents duplicate user creation conflicts.

Logs randomized data for easy debugging.

Scope

Focuses on end-user journey validation (UI layer).

Does not cover API or database verification at this stage.

🚀 Scalability & Future Enhancements
Area	Next Steps	Benefits
Page Object Model (POM)	Create /pages/ directory with reusable classes	Improves readability and reduces duplicate locators
Environment Configs	Add config.py or .env for URLs & creds	Enables easy staging vs production runs
Reporting	Integrate Allure or pytest-html	Produces shareable HTML reports
CI/CD Integration	Add .github/workflows/ci.yml	Auto-runs tests in GitHub Actions
Selectors	Work with devs to add data-test attributes	More stable and less fragile tests
🧱 Design Notes

Language: Python 3.12+

Frameworks: Playwright, Pytest

Execution Mode: Headed by default (for visibility)

Parallelization: Limited to -n 1 for sequential consistency

Stability: Deterministic waits, no arbitrary sleeps

Output: Uses print() checkpoints for clear runtime progress

🧠 Example Runtime Output

When running locally, you’ll see:

🔐 Navigating to sign-in page...
📩 Credentials entered.
✅ Login successful — landed on dashboard.
🔎 Looking for 'Book a scan' button...
✅ 'Book a scan' visible — clicking...
🧭 Selecting 'MRI Scan with Spine'...
✅ Clicked MRI option #1
✅ 'MRI Scan with Spine' selected.
✅ Navigated to /book-scan/select-plan.

🧩 Future Implementation Ideas

Data-driven test matrix for multiple plans or user types

Visual regression testing

API validation before form submission

Slack/Email alerts for CI failures

Docker containerization for consistent environments
