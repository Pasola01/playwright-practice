from pages.web_inputs_page import WebInputsPage
from  playwright.sync_api import expect
import re

def test_web_inputs(page, config):
    web_input_page = WebInputsPage(page)
    web_input_page.page.goto(config['url'] + "/inputs")
    web_input_page.enter_web_input_number(12345)
    web_input_page.enter_web_input_text("Simple Text")