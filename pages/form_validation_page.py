from pages.base_page import BasePage

class FormValidation(BasePage):
    number_validation_msg_locator = ""
    pick_up_data_locator = "//input[@name='pickupdate']"

    def enter_contact_name(self, name):
        self.page.get_by_label("Contact Name").fill(name)

    def enter_contact_number(self, num):
        self.page.get_by_label("Contact number").fill(num)

    def select_payment_method(self, option):
        self.page.get_by_label("Payment Method").select_option(option)

    def enter_date(self, date: str):
        self.page.locator(self.pick_up_data_locator).fill(date)

    def click_register(self):
        self.page.get_by_role("button", name="Register").click()