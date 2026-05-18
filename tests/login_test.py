import time

import pytest

from config_file import HOME_PAGE_URL
from data.data_user import TestData
from pages.home_page import HomePage
from pages.login_page import LoginPage


class TestLoginPage():

    def test_correct_login(self, driver, login_as):
        user = TestData.STANDARD_USER
        products_page = HomePage(driver)
        login_as(user)
        time.sleep(10)

        assert products_page.page_is_opened_url() == HOME_PAGE_URL
        assert products_page.page_is_opened_title() == 'Статистика'

    @pytest.mark.parametrize('user, error_message', [
        (TestData.WRONG_EMAIL_USER, 'Неверный email или пароль'),
        (TestData.WRONG_PASSWORD_USER, 'Неверный email или пароль')

    ])


    def test_incorrect_login(self, driver, login_as, user, error_message):
        #user = TestData.WRONG_PASSWORD_USER
        login_page: LoginPage = login_as(user)


        assert login_page.is_error_message_apper(), 'Сообщение об ошибке не появилось'
        assert login_page.get_error_message() == error_message, 'Неверное сообщение об ошибке'
