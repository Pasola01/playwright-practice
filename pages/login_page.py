from pages.base_page import BasePage


class LoginPage(BasePage):
    # Локатори
    username_input_locator = "#username"
    password_input_locator = "#password"
    submit_button_locator = "//button[@type='submit' and @class='btn btn-bg btn-primary d-block w-100']"
    login_flash_message = '#flash b'

    def enter_username(self, username):
        self.page.locator(self.username_input_locator).fill(username)  # Прямий доступ

    def enter_password(self, password):
        self.page.locator(self.password_input_locator).fill(password)

    def click_submit(self):
        self.page.locator(self.submit_button_locator).click()

    def click_submit_by_role(self):
        self.page.get_by_role("button", name="Submit").click()  # Використання get_by_role
