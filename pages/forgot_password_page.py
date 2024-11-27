from pages.base_page import BasePage

class ForgotPasswordPage(BasePage):

    fr_validation_msg_locator = "//div[@class='ms-1 invalid-feedback']"
    forgot_password_msg_locator = "//div[@id='confirmation-alert']"

    def enter_forgot_password_email(self, email):
        self.page.get_by_label("E-mail").fill(email)

    def click_retrieve_password(self):
        self.page.get_by_role("button", name="Retrieve password").click()
