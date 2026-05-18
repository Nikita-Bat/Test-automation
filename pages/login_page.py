from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    locators = LoginPageLocators()

    def fill_in_login_form(self, user):
        username = self.element_is_visible(self.locators.USERNAME_INPUT)
        username.clear()
        username.send_keys(user.username)
        password = self.element_is_visible(self.locators.PASSWORD_INPUT)
        password.clear()
        password.send_keys(user.password)
        button = self.element_is_visible(self.locators.SUBMIT_BUTTON)
        button.click()

    def is_error_message_apper(self) -> bool:
        try:
            return bool(self.element_is_presence_located(self.locators.ERROR_MESSAGE, timeout=10))
        except TimeoutError:
            return False


    def get_error_message(self)-> str:
        text = self.element_is_located(self.locators.ERROR_MESSAGE,timeout=10).text
        return text