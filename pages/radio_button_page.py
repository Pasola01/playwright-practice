from pages.base_page import BasePage

class RadioButton(BasePage):

    def select_favorite_color_btn(self, color):
        self.page.get_by_label(color).click()

    def select_favorite_sport_btn(self, sport):
        self.page.get_by_label(sport).click()