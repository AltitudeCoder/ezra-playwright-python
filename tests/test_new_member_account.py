from pages.join_page import JoinPage
from utils.config import config

def test_new_member_account(page):
    JoinPage(page, config.base_url)\
        .open()\
        .fill_random_user_data()\
        .fill_phone_and_password()\
        .agree_terms()\
        .submit()
    