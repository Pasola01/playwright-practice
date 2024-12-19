import pytest
from playwright.sync_api import sync_playwright
import yaml
import  imaplib

@pytest.fixture(scope="session")
def config():
    with open("/Users/yuramelika/learn_projects/playwright-practice/config/config.yaml") as f:
        return yaml.safe_load(f)

@pytest.fixture(scope="session")
def browser(config):
    with sync_playwright() as p:
        browser = p[config['browser']].launch(headless=config['headless'])
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()


@pytest.fixture(scope="session")
def conf_web_inputs():
    with open("/Users/yuramelika/learn_projects/playwright-practice/test_data/web_inputs_data.yaml") as f:
        return yaml.safe_load(f)


@pytest.fixture(scope="session")
def conf_registration():
    with open("/Users/yuramelika/learn_projects/playwright-practice/test_data/registration_data.yaml") as f:
        return yaml.safe_load(f)

@pytest.fixture(scope="session")
def conf_validation_form():
    with open("/Users/yuramelika/learn_projects/playwright-practice/test_data/form_validation_data.yaml") as f:
        return yaml.safe_load(f)