from pages.base_page import BasePage

class WebInputsPage(BasePage):
    # Locators
    web_input_num_locator = "//input[@id='input-number']"
    web_output_num_locator = "//strong[@id='output-number']"
    web_input_text_locator = "//input[@id='input-text']"
    web_output_text_locator = "//strong[@id='output-text']"
    web_output_password_locator = "//strong[@id='output-password']"
    web_output_date_locator = "//strong[@id='output-date']"


    def enter_web_input_number(self, number: int):
        self.page.locator(self.web_input_num_locator).fill(str(number))

    def enter_web_input_text(self, text: str):
        self.page.locator(self.web_input_text_locator).fill(text)

    def enter_web_input_password(self, password: str):
        self.page.get_by_label("Input: Password").fill(password)

    def enter_web_input_date(self, date: str):
        self.page.get_by_label("Input: Date").fill(date)

    def click_display_inputs_btn(self):
        self.page.get_by_role(role="button", name="Display Inputs").click()