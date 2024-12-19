import time

from playwright.sync_api import expect

from pages.form_validation_page import FormValidation

def test_all_mandatory_fields_filled_valid(page, config, conf_validation_form):
    validation_form_page = FormValidation(page)
    validation_form_page.page.goto(config["url"] + "/form-validation")
    validation_form_page.enter_contact_name(conf_validation_form["form_name"])
    validation_form_page.enter_contact_number(conf_validation_form["valid_contact_number"])
    validation_form_page.select_payment_method("card")
    validation_form_page.enter_date("2024-12-18")
    validation_form_page.click_register()
    expect(page).to_have_url("https://practice.expandtesting.com/form-confirmation")