from playwright.sync_api import expect
from pages.drag_and_drop_page import DragAndDrop

def test_drag_and_drop_a_to_b(page, config):
    drag_and_drop_page = DragAndDrop(page)
    drag_and_drop_page.page.goto(config["url"] + "/drag-and-drop")
    expect(page.locator(drag_and_drop_page.column_a_locator)).to_have_text("A")
    expect(page.locator(drag_and_drop_page.column_b_locator)).to_have_text("B")
    drag_and_drop_page.drag_a_to_b()
    expect(page.locator(drag_and_drop_page.column_a_locator)).to_have_text("B")
    expect(page.locator(drag_and_drop_page.column_b_locator)).to_have_text("A")


def test_drag_and_drop_b_to_a(page, config):
    drag_and_drop_page = DragAndDrop(page)
    drag_and_drop_page.page.goto(config["url"] + "/drag-and-drop")
    expect(page.locator(drag_and_drop_page.column_a_locator)).to_have_text("A")
    expect(page.locator(drag_and_drop_page.column_b_locator)).to_have_text("B")
    drag_and_drop_page.drag_b_to_a()
    expect(page.locator(drag_and_drop_page.column_a_locator)).to_have_text("B")
    expect(page.locator(drag_and_drop_page.column_b_locator)).to_have_text("A")
