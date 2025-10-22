from playwright.sync_api import Page, expect

class SelectPlanPage:
    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.url = f"{base_url}/book-scan/select-plan"
        self.book_scan_button = page.get_by_role("button", name="Book a scan")
        self.continue_button = page.locator("button.basic.normal.yellow[data-test='submit']").first

    def assert_loaded(self):
        expect(self.page).to_have_url(self.url, timeout=20_000)
        print("✅ Confirmed navigation to /book-scan/select-plan")
        return self

    def select_mri_plan(self):
        print("🧭 Selecting 'MRI Scan with Spine'...")
        plan_options = self.page.locator("p.encounter-title.h4", has_text="MRI Scan with Spine")
        expect(plan_options.first).to_be_visible(timeout=15_000)

        for i in range(plan_options.count()):
            option = plan_options.nth(i)
            if option.is_visible():
                option.scroll_into_view_if_needed()
                option.click()
                print(f"✅ Clicked MRI option #{i+1}")
                break
        return self

    def continue_next(self):
        print("➡️ Clicking 'Continue'...")
        expect(self.continue_button).to_be_visible(timeout=10_000)
        expect(self.continue_button).to_be_enabled()
        self.continue_button.scroll_into_view_if_needed()
        self.continue_button.click()
        print("✅ 'Continue' clicked — proceeding to next step.")
        return self
