import time

from pages.forgot_password_page import ForgotPasswordPage
from  playwright.sync_api import expect
from helpers.email_service import GmailReader


def test_invalid_email_entered(config, page):
    forgot_page = ForgotPasswordPage(page)
    forgot_page.page.goto(config["url"]+"/forgot-password")
    forgot_page.enter_forgot_password_email("invalid")
    forgot_page.click_retrieve_password()
    # Expect
    expect(page.locator(forgot_page.fr_validation_msg_locator)).to_have_text("Please enter a valid email address.")

def test_open_forgot_password_link(config, page):
    forgot_page = ForgotPasswordPage(page)
    forgot_page.page.goto(config["url"] + "/forgot-password")
    forgot_page.enter_forgot_password_email(config["email_user"])
    forgot_page.click_retrieve_password()
    # Need to write expect for this
    gmail_reader = GmailReader(email_user="barry.rockhold@gmail.com", app_password="yncs blvu xjte qkgk")
    gmail_reader.connect()
    password_link = gmail_reader.get_forgot_password_link()
    gmail_reader.disconnect()
    forgot_page.page.goto(password_link)
    time.sleep(10)