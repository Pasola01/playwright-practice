from pages.web_inputs_page import WebInputsPage
from  playwright.sync_api import expect

def test_web_inputs(page, config, test_data_web_inputs):
    web_input_page = WebInputsPage(page)
    web_input_page.page.goto(config['url'] + "/inputs")
    web_input_page.enter_web_input_number(test_data_web_inputs["input_num"])
    web_input_page.enter_web_input_text(test_data_web_inputs["input_text"])
    web_input_page.enter_web_input_password(test_data_web_inputs["input_text"])
    web_input_page.enter_web_input_date(test_data_web_inputs["input_date"])
    web_input_page.click_display_inputs_btn()
    # Expect
    expect(page.locator(web_input_page.web_output_num_locator)).to_have_text(test_data_web_inputs["input_num"])
    expect(page.locator(web_input_page.web_output_text_locator)).to_have_text(test_data_web_inputs["input_text"])
    expect(page.locator(web_input_page.web_output_password_locator)).to_have_text(test_data_web_inputs["input_text"])
    expect(page.locator(web_input_page.web_output_date_locator)).to_have_text(test_data_web_inputs["input_date"])