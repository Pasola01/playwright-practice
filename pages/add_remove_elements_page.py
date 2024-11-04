from pages.base_page import BasePage

class AddRemoveElements(BasePage):
    add_element_locator = "//button[@class='btn btn-primary mt-3']"


    def click_add_element(self):
        self.page.locator(self.add_element_locator).click()