from pages.dynamic_table_page import DynamicTable
from  playwright.sync_api import expect

def test_compare_chrome_cpu(page, config):
    dynamic_table_page = DynamicTable(page)
    dynamic_table_page.page.goto(config["url"] +"/dynamic-table")
    cpu_values_chrome = dynamic_table_page.find_chrome_cpu_value()
    print(cpu_values_chrome)
    chrome_cpu = "//p[@id='chrome-cpu']"
    expect(page.locator(chrome_cpu)).to_have_text(f"Chrome CPU: {cpu_values_chrome}")

