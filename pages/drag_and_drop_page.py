from pages.base_page import BasePage

class DragAndDrop(BasePage):
    column_a_locator = "//div[@id='column-a']"
    column_b_locator = "//div[@id='column-b']"

    def drag_a_to_b(self):
        self.page.locator(self.column_a_locator).drag_to(self.page.locator(self.column_b_locator))

    def drag_b_to_a(self):
        self.page.locator(self.column_b_locator).drag_to(self.page.locator(self.column_a_locator))