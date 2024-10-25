from pages.base_page import BasePage


class LoginPage(BasePage):
    # Locators
    login_username_input_locator = "//input[@id='username']"
    login_password_input_locator = "//input[@id='password']"
    submit_button_locator = "//button[@type='submit']"
    logout_btn_locator = "//i[@class='icon-2x icon-signout']"

    def enter_username(self, username):
        self.page.locator(self.login_username_input_locator).fill(username)

    def enter_password(self, password):
        self.page.locator(self.login_password_input_locator).fill(password)

    def click_submit(self):
        self.page.locator(self.submit_button_locator).click()

    def click_submit_by_role(self):
        self.page.get_by_role("button", name="Submit").click()

    def click_logout(self):
        self.page.locator(self.logout_btn_locator).click()
