from selenium.webdriver.common.by import By


class LoginPageLocators:
    USERNAME_INPUT = (By.CSS_SELECTOR, "#email")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#password")
    SUBMIT_BUTTON = (By.XPATH, "//button[text()='Войти']")
    ERROR_MESSAGE = (By.XPATH, "//div[text()='Неверный email или пароль']")
    INCORRECT_MESSAGE_EMAIL = (By.XPATH, "//span[text()='Email']")
    UNCORRECT_MESSAGE_PASSWORD = (By.XPATH, "//span[text()='Пароль']")



