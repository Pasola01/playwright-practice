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
    email_user = config["email_user"]
    app_password = config["app_password"]

    forgot_page = ForgotPasswordPage(page)
    forgot_page.page.goto(config["url"] + "/forgot-password")
    forgot_page.enter_forgot_password_email(config["email_user"])
    forgot_page.click_retrieve_password()
    # Need to write expect for this
    gmail_reader = GmailReader(email_user, app_password)
    gmail_reader.connect()
    time.sleep(85)
    password_link = gmail_reader.get_forgot_password_link()
    forgot_page.page.goto(password_link)
    gmail_reader.delete_last_email()
    gmail_reader.disconnect()
