from pages.base_page import BasePage

class DynamicTable(BasePage):
    chrome_cpu_value_locator = "//tr[td[contains(text(), 'Chrome')]]/td[contains(text(), '%')]"
    firefox_cpu_value_locator = "//tr[td[contains(text(), 'Firefox')]]/td[contains(text(), '%')]"

    def find_chrome_cpu_value(self):
        cpu_value = self.page.locator(self.chrome_cpu_value_locator).text_content()
        return cpu_value

    def find_firefox_cpu_value(self):
        cpu_value = self.page.locator(self.firefox_cpu_value_locator).text_content()
        return cpu_value





