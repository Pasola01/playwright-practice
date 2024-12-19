import time
from helpers.email_service import GmailReader
from pages.otp_page import OtpPage


def test_enter_email_for_otp(page, config):
    email_user = config["email_user"]
    app_password = config["app_password"]

    otp_page = OtpPage(page)
    otp_page.page.goto(config["url"] + "/otp-login")
    otp_page.enter_email_for_otp(email_user)
    otp_page.click_send_otp_code()
    # # Ініціалізація читача Gmail
    gmail_reader = GmailReader(email_user, app_password)
    gmail_reader.connect()
    time.sleep(85)
    otp_code = gmail_reader.get_otp()
    gmail_reader.delete_last_email()
    otp_page.enter_otp_code(otp_code)
    otp_page.click_verify_otp_code()
    gmail_reader.disconnect()

