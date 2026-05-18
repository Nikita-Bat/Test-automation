from webdriver_manager.firefox import GeckoDriverManager
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service

from config_file import BASE_URL
from pages.login_page import LoginPage


@pytest.fixture(scope="function")
def driver():
    # Modern approach using Service for Firefox
    options = webdriver.FirefoxOptions()
    options.add_argument("--guest")
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service, options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

@pytest.fixture
def login_as(driver):
    def _login_as_(user):
        page = LoginPage(driver)
        page.open(BASE_URL)
        page.fill_in_login_form(user)
        return page
    return _login_as_
