from pages.login_page import LoginPage
from  playwright.sync_api import expect
import re

def test_login(page, config):
    login_page = LoginPage(page)
    login_page.page.goto(config['url'] + "/login")
    login_page.enter_username("testuser")
    login_page.enter_password("password")
    login_page.click_submit()  # Або click_submit_by_role()
    # login_flash_message = page.locator('#flash b')
    expect(login_page.login_flash_message).to_contain_text(re.compile("Your username is invalid!"))
