from selenium.webdriver.common.by import By


class LoginPageLocators:
    USERNAME_INPUT = (By.CSS_SELECTOR, "#email")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#password")
    SUBMIT_BUTTON = (By.XPATH, "//button[text()='Войти']")
    ERROR_MESSAGE = (By.XPATH, "//div[text()='Неверный email или пароль']")
    INCORRECT_EMAIL_MESSAGE = (By.XPATH, "//span[text()='Email']")
    INCORRECT_PASSWORD_MESSAGE = (By.XPATH, "//span[text()='Пароль']")



