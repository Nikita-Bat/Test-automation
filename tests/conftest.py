from webdriver_manager.chrome import ChromeDriverManager
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="function")
def driver():
    # Modern approach using Service
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()