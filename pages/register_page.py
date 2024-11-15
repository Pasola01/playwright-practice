from pages.base_page import BasePage

class RegisterPage(BasePage):
    # Locators
    register_btn_locator = "//button[@type='submit']"
    flash_msg_locator = "//div[@id='flash']"
    password_locator = "//input[@id='password']"
    confirm_password_locator = "//input[@id='confirmPassword']"


    def enter_username(self, username):
        self.page.get_by_label("Username").fill(username)

    def enter_password(self, password):
        self.page.locator(self.password_locator).fill(password)

    def enter_confirm_password(self, confirm_password):
        self.page.locator(self.confirm_password_locator).fill(confirm_password)

    def click_register_btn(self):
        self.page.locator(self.register_btn_locator).click()