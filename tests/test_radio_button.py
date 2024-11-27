import time

from playwright.sync_api import expect

from pages.radio_button_page import RadioButton

def test_color_radio_buttons_clickable(page, config):
    radio_button_page = RadioButton(page)
    radio_button_page.page.goto(config["url"] + "/radio-buttons")
    radio_button_page.select_favorite_color_btn("Blue")
    radio_button_page.select_favorite_color_btn("Red")
    radio_button_page.select_favorite_color_btn("Yellow")
    radio_button_page.select_favorite_color_btn("Black")
    # To Do: Зробити перевірку Radio Button Green, щоб переконатися що вона присутня але не активна

def test_sport_radio_buttons_clickable(page, config):
    radio_button_page = RadioButton(page)
    radio_button_page.page.goto(config["url"] + "/radio-buttons")
    radio_button_page.select_favorite_sport_btn("Basketball")
    radio_button_page.select_favorite_sport_btn("Football")
    radio_button_page.select_favorite_sport_btn("Tennis")

