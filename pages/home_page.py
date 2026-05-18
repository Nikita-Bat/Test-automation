from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage


class HomePage(BasePage):
    locators = HomePageLocators()

    def page_is_opened_url(self):
        return self.driver.current_url

    def page_is_opened_title(self):
        return self.element_is_visible(self.locators.PAGE_TITLE).text
