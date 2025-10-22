from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url

    def navigate(self):
        print("🧭 Navigating to sign-in page...")
        self.page.goto(f"{self.base_url}/sign-in", wait_until="domcontentloaded")
        return self

    def login(self, email: str, password: str):
        print("📩 Filling credentials...")
        self.page.fill("#email", email)
        self.page.fill("#password", password)
        submit_btn = self.page.locator("button.submit-btn").first
        expect(submit_btn).to_be_visible(timeout=10_000)
        submit_btn.click()
        print("✅ Submitted login form.")
        return self

    def assert_login_success(self):
        expect(self.page).to_have_url(f"{self.base_url}/", timeout=20_000)
        print("🏠 Login successful — landed on dashboard.")
        return self
