from pages.add_remove_elements_page import AddRemoveElements
from  playwright.sync_api import expect

def test_add_remove_elements_add_element(page, config):
    add_remove_elements_page = AddRemoveElements(page)
    add_remove_elements_page.page.goto(config['url'] + "/add-remove-elements")
    add_remove_elements_page.click_add_element_btn()
    expect(page.locator(add_remove_elements_page.added_element_locator)).to_be_visible()

def test_add_remove_elements_add_few_elements(page, config):
    add_remove_elements_page = AddRemoveElements(page)
    add_remove_elements_page.page.goto(config['url'] + "/add-remove-elements")
    add_remove_elements_page.click_add_element_btn()
    add_remove_elements_page.click_add_element_btn()
    add_remove_elements_page.click_add_element_btn()
    expect(page.locator(add_remove_elements_page.added_element_locator)).to_have_count(3)

def test_add_remove_elements_remove_element(page, config):
    add_remove_elements_page = AddRemoveElements(page)
    add_remove_elements_page.page.goto(config['url'] + "/add-remove-elements")
    add_remove_elements_page.click_add_element_btn()
    add_remove_elements_page.remove_element()
    expect(page.locator(add_remove_elements_page.added_element_locator)).not_to_be_visible()
