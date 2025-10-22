import random
import uuid
import re
from playwright.sync_api import Page, expect

def test_new_member_account(page: Page):
    #Sign-in page to test Join link
    page.goto("https://myezra-staging.ezra.com/sign-in", wait_until="domcontentloaded")

    #Select the Join link
    join_link = page.locator('a[aria-label="Join"][href="/join"]').first
    expect(join_link).to_be_visible(timeout=10_000)
    join_link.click()
    print("Clicked Join link, navigating to /join...")

    #Verify navigation to /join
    expect(page).to_have_url("https://myezra-staging.ezra.com/join", timeout=10_000)

    #Generate random first and last names
    first_names = ["Alex", "Jordan", "Taylor", "Morgan", "Casey", "Blake", "Jamie", "Riley", "Drew", "Avery"]
    last_names  = ["Smith", "Johnson", "Brown", "Garcia", "Davis", "Miller", "Wilson", "Moore", "Anderson", "Thomas"]

    random_first_name = random.choice(first_names) + str(random.randint(100, 999))
    random_last_name  = random.choice(last_names) + str(random.randint(100, 999))
    print("First and Last names created...")

    #Generate unique email
    unique_email = f"{random_first_name.lower()}.{random_last_name.lower()}_{uuid.uuid4().hex[:6]}@example.com"
    print(f"Using email: {unique_email}")
    
    #Fill the fields
    page.locator('input#firstName').fill(random_first_name)
    page.locator('input#lastName').fill(random_last_name)
    page.locator('input#email').fill(unique_email)
    print("Unique email created")

    #Fill phone number (AZ area codes)
    az_area_codes = ["480", "602", "623", "520"]
    area = random.choice(az_area_codes)
    prefix = random.randint(200, 999)
    line   = random.randint(1000, 9999)
    digits = f"{area}{prefix}{line}"
    

    phone_input = page.locator("#phoneNumber")
    expect(phone_input).to_be_visible(timeout=10_000)
    phone_input.click()
    phone_input.fill("")
    phone_input.type(digits, delay=20)
    print(f"Using phone: ({area}) {prefix}-{line}")
    print("Phone number added")

    #Password (fixed)
    password = "EzraQA!sAmazing2025"
    pw = page.locator("#password")
    expect(pw).to_be_visible(timeout=10_000)
    pw.fill(password)

    #Consent checkbox (styled <button class="checkbox">)
    consent = page.locator('button.checkbox').first
    expect(consent).to_be_visible(timeout=10_000)
    if "checked" not in (consent.get_attribute("class") or ""):
        consent.click()
    expect(consent).to_have_class(re.compile(r"\bcheckbox\b.*\bchecked\b", re.I))

    # 🔟 Submit the form
    submit_btn = page.locator("button[type='submit']").first
    
    submit_btn.click()
    print("Form submitted.")

    print("New Member created... yay!!")

    # small pause so you can visually confirm while debugging
    page.wait_for_timeout(3000)
