from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.select_plan_page import SelectPlanPage
from utils.config import config


def test_login_and_scan_select(page: Page):
    """
    Full flow: login → book scan → select plan → continue.
    Demonstrates POM structure and modular test design.
    """

    # Initialize Page Objects
    login_page = LoginPage(page, config.base_url)
    select_plan_page = SelectPlanPage(page, config.base_url)

    # Perform login
    login_page.navigate().login(
        "jason.m.lambert78+ezrajl1@gmail.com",
        "EzraQA!sAmazing1"
    ).assert_login_success()

    # Click “Book a scan” button
    page.wait_for_timeout(2000)  # Allow UI to stabilize
    book_scan_btn = page.get_by_role("button", name="Book a scan")
    book_scan_btn.scroll_into_view_if_needed()
    book_scan_btn.click()
    print("Clicked 'Book a scan' button.")

    # Select MRI plan and continue
    select_plan_page.assert_loaded().select_mri_plan().continue_next()

    # Optional wait (visual verification / stability)
    page.wait_for_timeout(3000)
    print("Test completed successfully — login and plan selection flow verified.")
