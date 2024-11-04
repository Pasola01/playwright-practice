from pages.add_remove_elements_page import AddRemoveElements

def test_add_remove_elements(page, config):
    add_remove_elements_page = AddRemoveElements(page)
    add_remove_elements_page.page.goto(config['url'] + "/add-remove-elements")
    add_remove_elements_page.add_element_locator