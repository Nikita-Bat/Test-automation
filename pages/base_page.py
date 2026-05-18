from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)


    def wait(self, timeout: object = 5):
        return WebDriverWait(self.driver, timeout)

    def element_is_visible(self, locator, timeout = 5):
        return self.wait(timeout).until(EC.visibility_of_element_located(locator))

    def element_is_not_visible(self, locator, timeout = 5):
        return self.wait(timeout).until(EC.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout = 5):
        return self.wait(timeout).until(EC.element_to_be_clickable(locator))

    def element_is_presence_located(self, locator, timeout = 5):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def element_is_located(self, locator, timeout = 5):
        return self.wait(timeout).until(EC.visibility_of_element_located(locator))

