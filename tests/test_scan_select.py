from playwright.sync_api import Page, expect
import time


def login(page: Page):
    """Logs into Ezra staging."""
    print("🔐 Navigating to sign-in page...")
    page.goto("https://myezra-staging.ezra.com/sign-in", wait_until="domcontentloaded")

    # --- Fill credentials (replace if needed) ---
    email = "jason.m.lambert78+ezrajl1@gmail.com"
    password = "EzraQA!sAmazing1"

    page.fill("#email", email)
    page.fill("#password", password)
    print("📩 Credentials entered.")

    # --- Submit ---
    submit_btn = page.locator("button.submit-btn").first
    expect(submit_btn).to_be_visible(timeout=10_000)
    submit_btn.click()

    # --- Wait for redirect to dashboard/home ---
    page.wait_for_url("https://myezra-staging.ezra.com/", timeout=20_000)
    print("✅ Login successful — landed on dashboard.\n")


def test_scan_select(page: Page):
    """Logs in, clicks Book a Scan, and selects the MRI plan."""

    # 1️⃣ Log in
    login(page)

    # 2️⃣ Click the "Book a scan" button on the dashboard
    print("🔎 Looking for 'Book a scan' button...")

    page.wait_for_load_state("domcontentloaded", timeout=10000)
    page.wait_for_timeout(2000)  # Allow UI transitions

    book_scan_btn = page.get_by_role("button", name="Book a scan")
    book_scan_btn.scroll_into_view_if_needed()
    page.wait_for_timeout(500)

    if book_scan_btn.is_visible():
        print("✅ 'Book a scan' visible — clicking...")
        book_scan_btn.click()
    else:
        print("⚠️ Button hidden — forcing click...")
        book_scan_btn.click(force=True)

    expect(page).to_have_url("https://myezra-staging.ezra.com/book-scan/select-plan", timeout=20_000)
    print("✅ Navigated to /book-scan/select-plan.\n")

    # 3️⃣ Select the "MRI Scan with Spine" plan
    print("🧭 Selecting 'MRI Scan with Spine'...")

    plan_options = page.locator("p.encounter-title.h4", has_text="MRI Scan with Spine")

    # Wait until at least one appears
    expect(plan_options.first).to_be_visible(timeout=15_000)

    # Count how many we have
    count = plan_options.count()
    print(f"🔢 Found {count} matching 'MRI Scan with Spine' options")

    # Click the first visible one
    clicked = False
    for i in range(count):
        option = plan_options.nth(i)
        if option.is_visible():
            option.scroll_into_view_if_needed()
            option.click()
            print(f"✅ Clicked MRI option #{i+1}")
            clicked = True
            break

    if not clicked:
        raise AssertionError("❌ No visible 'MRI Scan with Spine' option found!")

    page.wait_for_timeout(2000)
    print("✅ 'MRI Scan with Spine' selected.\n")
    
    # 4️⃣ Click the "Continue" button
    print("➡️ Looking for the 'Continue' button...")

    continue_btn = page.locator("button.basic.normal.yellow[data-test='submit']").first

    # Wait for it to become visible & enabled
    expect(continue_btn).to_be_visible(timeout=15_000)
    expect(continue_btn).to_be_enabled(timeout=15_000)

    # Scroll into view and click
    continue_btn.scroll_into_view_if_needed()
    page.wait_for_timeout(500)
    continue_btn.click()

    print("✅ Clicked 'Continue' button — proceeding to next step.\n")

    # Wait for navigation (the next page usually loads)
    page.wait_for_load_state("networkidle", timeout=15_000)
    page.wait_for_timeout(2000)
    
    # Optional pause for visual confirmation
    time.sleep(5)
