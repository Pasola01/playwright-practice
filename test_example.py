import re
from locators import *
from playwright.sync_api import Page, expect
import pytest


@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    print("before the test runs")

    # Go to the starting url before each test.
    page.goto('https://missliberte.com/')
    expect(page).to_have_url('https://missliberte.com/')
    yield

    print("after the test runs")


def test_test_box(page: Page):
    close_modal_locator = "//span[@class='ic-close close-modal']"
    page.locator(close_modal_locator).click()