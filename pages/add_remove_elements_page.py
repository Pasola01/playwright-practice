from pages.base_page import BasePage

class AddRemoveElements(BasePage):
    add_element_locator = "//button[@class='btn btn-primary mt-3']"
    added_element_locator = "//button[@class='added-manually btn btn-info']"


    def click_add_element_btn(self):
        self.page.locator(self.add_element_locator).click()

    def remove_element(self):
        self.page.locator(self.added_element_locator).click()