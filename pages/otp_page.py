from pages.base_page import BasePage

class OtpPage(BasePage):


    def enter_email_for_otp(self, email):
        self.page.get_by_label("Your Email Address").fill(email)

    def click_send_otp_code(self):
        self.page.get_by_role("button", name="Send OTP Code").click()

    def enter_otp_code(self, code):
        self.page.get_by_placeholder("Enter OTP code").fill(code)

    def click_verify_otp_code(self):
        self.page.get_by_role("button", name="Verify OTP Code").click()

