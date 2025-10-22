from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.email_input = page.locator("#email")
        self.password_input = page.locator("#password")
        self.submit_btn = page.locator("button.submit-btn").first
        self.base_url = "https://myezra-staging.ezra.com/sign-in"

    def login(self, email: str, password: str):
        print("🧭 Navigating to sign-in page...")
        self.page.goto(self.base_url, wait_until="domcontentloaded")

        self.email_input.fill(email)
        self.password_input.fill(password)
        print("📩 Credentials entered.")

        expect(self.submit_btn).to_be_visible(timeout=10_000)
        self.submit_btn.click()

        self.page.wait_for_url("https://myezra-staging.ezra.com/", timeout=20_000)
        print("✅ Login successful — landed on dashboard.")
        return self
