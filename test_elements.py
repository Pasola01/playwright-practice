import re
from locators import *
from playwright.sync_api import Page, expect
import pytest


@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    print("before the test runs")

    # Go to the starting url before each test.
    page.goto('https://demoqa.com/')
    expect(page).to_have_url('https://demoqa.com/')
    page.locator(LocatorsElements.element_block_locator).click()
    yield

    print("after the test runs")


def test_test_box(page: Page):
    page.get_by_text('Text Box').click()
    page.get_by_placeholder('Full Name').fill('Yurii Melika')
    page.get_by_placeholder('name@example.com').fill('test@mail.com')
    page.get_by_placeholder('Current Address').fill('Ukraine, Uzhorod')
    page.locator(LocatorsElements.input_permanent_address_locator).fill('Ukraine, Mukachevo')
    page.get_by_role('button', name='Submit').click()
    # Expect
    expect(page.locator(LocatorsElements.output_name_locator)).to_have_text(re.compile('Yurii'))
    expect(page.locator(LocatorsElements.output_email_locator)).to_have_text(re.compile('test@mail.com'))
    expect(page.locator(LocatorsElements.output_currentAddress_locator)).to_have_text(re.compile('Uzhorod'))
    expect(page.locator(LocatorsElements.output_permanent_address_locator)).to_have_text(re.compile('Mukachevo'))


def test_check_box(page: Page):
    page.get_by_text('Check Box').click()
