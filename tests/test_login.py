from pages.login_page import LoginPage
from  playwright.sync_api import expect
import re

def test_login_invalid_username(page, config):
    login_page = LoginPage(page)
    login_page.page.goto(config['url'] + "/login")
    login_page.enter_username("invalid_username")
    login_page.enter_password("SuperSecretPassword!")
    login_page.click_submit()
    login_flash_message = page.locator('#flash b')
    expect(login_flash_message).to_contain_text(re.compile("Your username is invalid!"))

def test_login_invalid_password(page, config):
    login_page = LoginPage(page)
    login_page.page.goto(config['url'] + "/login")
    login_page.enter_username("practice")
    login_page.enter_password("invalid_password")
    login_page.click_submit()
    login_flash_message = page.locator('#flash b')
    expect(login_flash_message).to_contain_text(re.compile("Your password is invalid!"))


def test_login_valid_credentials(page, config):
    login_page = LoginPage(page)
    login_page.page.goto(config['url'] + "/login")
    login_page.enter_username("practice")
    login_page.enter_password("SuperSecretPassword!")
    login_page.click_submit()
    login_flash_message = page.locator('#flash b')
    expect(login_flash_message).to_contain_text(re.compile("You logged into a secure area!"))

def test_logout(page, config):
    login_page = LoginPage(page)
    login_page.page.goto(config['url'] + "/login")
    login_page.enter_username("practice")
    login_page.enter_password("SuperSecretPassword!")
    login_page.click_submit()
    login_flash_message = page.locator('#flash b')
    expect(login_flash_message).to_contain_text(re.compile("You logged into a secure area!"))
    login_page.click_logout()
    expect(login_flash_message).to_contain_text(re.compile("You logged out of the secure area!"))
