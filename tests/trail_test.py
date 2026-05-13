import time

from pages.base_page import BasePage


def test_trail(driver):
    page = BasePage(driver)
    page.open("http://www.google.com")
    time.sleep(10)