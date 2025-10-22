from playwright.sync_api import expect
import re, random, uuid

class JoinPage:
    def __init__(self, page, base_url):
        self.page = page
        self.base_url = base_url

    def open(self):
        self.page.goto(f"{self.base_url}/join", wait_until="domcontentloaded")
        expect(self.page).to_have_url(f"{self.base_url}/join")
        return self

    def fill_random_user_data(self):
        first_names = ["Alex", "Jordan", "Taylor", "Morgan"]
        last_names  = ["Smith", "Johnson", "Brown", "Davis"]
        self.first = random.choice(first_names)
        self.last = random.choice(last_names)
        self.email = f"{self.first.lower()}.{self.last.lower()}_{uuid.uuid4().hex[:6]}@example.com"

        self.page.fill("#firstName", self.first)
        self.page.fill("#lastName", self.last)
        self.page.fill("#email", self.email)
        print(f"Generated user: {self.first} {self.last} ({self.email})")
        return self

    def fill_phone_and_password(self):
        area_codes = ["480", "602", "623", "520"]
        phone = f"{random.choice(area_codes)}{random.randint(2000000, 9999999)}"
        self.page.fill("#phoneNumber", phone)
        self.page.fill("#password", "EzraQA!sAmazing2025")
        print(f"Filled phone: {phone}")
        return self

    def agree_terms(self):
        consent = self.page.locator("button.checkbox").first
        expect(consent).to_be_visible()
        if "checked" not in (consent.get_attribute("class") or ""):
            consent.click()
        return self

    def submit(self):
        btn = self.page.locator("button[type='submit']").first
        btn.click()
        print("Form submitted.")
        self.page.wait_for_timeout(2000)
        return self