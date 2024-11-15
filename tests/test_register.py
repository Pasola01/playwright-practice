import time
from pages.register_page import RegisterPage
from  playwright.sync_api import expect
from datetime import *
from random import *

def test_registration_fails_without_all_mandatory_fields(page, config, load_registration_data):
    register_page = RegisterPage(page)
    register_page.page.goto(config["url"] + "/register")
    register_page.enter_username(load_registration_data["valid_username"])
    register_page.click_register_btn()
    # Expect
    expect(page.locator(register_page.flash_msg_locator)).to_have_text(load_registration_data["flash_msg_required_fields"])

def test_registration_fails_when_username_invalid(page, config, load_registration_data):
    register_page = RegisterPage(page)
    register_page.page.goto(config["url"] + "/register")
    register_page.enter_username(load_registration_data["invalid_username"])
    register_page.enter_password(load_registration_data["password_a"])
    register_page.enter_confirm_password(load_registration_data["password_a"])
    register_page.click_register_btn()
    # Expect
    expect(page.locator(register_page.flash_msg_locator)).to_have_text(load_registration_data["flash_msg_invalid_username"])


def test_registration_fails_when_passwords_do_not_match(page, config, load_registration_data):
    register_page = RegisterPage(page)
    register_page.page.goto(config["url"] + "/register")
    register_page.enter_username(load_registration_data['valid_username'])
    register_page.enter_password(load_registration_data["password_a"])
    register_page.enter_confirm_password(load_registration_data["password_b"])
    register_page.click_register_btn()
    # Expect
    expect(page.locator(register_page.flash_msg_locator)).to_have_text(load_registration_data['flash_msg_password_do_not_match'])


def test_registration_successful(page, config, load_registration_data):
    register_page = RegisterPage(page)
    register_page.page.goto(config["url"] + "/register")
    register_page.enter_username(load_registration_data["valid_username"]+datetime.now().strftime("%H%M%S"))
    register_page.enter_password(load_registration_data["password_a"])
    register_page.enter_confirm_password(load_registration_data["password_a"])
    register_page.click_register_btn()
    # Expect
    expect(page.locator(register_page.flash_msg_locator)).to_have_text(load_registration_data["flash_msg_registration_successful"])
