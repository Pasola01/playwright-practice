from pages.base_page import BasePage

class WebInputsPage(BasePage):
    # Locators
    web_input_num_locator = "//input[@id='input-number']"
    web_input_text_locator = "//input[@id='input-text']"


    def enter_web_input_number(self, number: int):
        self.page.locator(self.web_input_num_locator).fill(str(number))

    def enter_web_input_text(self, text: str):
        self.page.locator(self.web_input_text_locator).fill(text)

    # def enter_web_input_text(self, text: str):
    #     self.page.locator(self.web_input_text_locator).fill(text)

    def main_branch_test_1_as_Yurii(self):
        pass