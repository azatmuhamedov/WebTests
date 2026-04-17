from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class LoginPageLocators:
    LOGIN_TAB = (By.XPATH, '//*[@data-l="t,login_tab"]')
    QRCODE_TAB = (By.XPATH, '//*[@data-l="t,qr_tab"]')
    LOGIN_FIELD = (By.XPATH, '//*[@id="field_email"]')
    PASSWORD_FIELD = (By.ID, 'field_password')
    PASSWORD_HIDDEN = (By.XPATH, '//*[@class="vkuiVisuallyHidden__host vkuiRootComponent__host"]')
    LOGIN_BUTTON = (By.XPATH, '//*[@data-test-id="enter-action"]')
    LOGIN_WITH_QRCODE = (By.XPATH, "//button[contains(@class,'vkuiButton__modeOutline')]")
    CANT_SIGN_IN_BUTTON = (By.XPATH, "//button[contains(@class,'vkuiLink__host')]")
    SIGN_UP_BUTTON = (By.XPATH, "//button[contains(@class,'vkuiButton__modeSecondary')]")
    VK_BUTTON = (By.XPATH, '//*[@class="h-mod __small __vk_id social-icon-button"]')
    MAIL_BUTTON = (By.XPATH, '//*[@class="i ic social-icon __s __mailru"]')
    YA_BUTTON = (By.XPATH, '//*[@class="i ic social-icon __s __yandex"]')
    ERROR_TEXT = (By.XPATH, "//span[contains(@class,'vkuiCaption__sizeYNone')]")

class LoginPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        self.find_element(LoginPageLocators.LOGIN_TAB)
        self.find_element(LoginPageLocators.QRCODE_TAB)
        self.find_element(LoginPageLocators.LOGIN_FIELD)
        self.find_element(LoginPageLocators.PASSWORD_FIELD)
        self.find_element(LoginPageLocators.LOGIN_BUTTON)
        self.find_element(LoginPageLocators.LOGIN_WITH_QRCODE)
        self.find_element(LoginPageLocators.CANT_SIGN_IN_BUTTON)
        self.find_element(LoginPageLocators.SIGN_UP_BUTTON)
        self.find_element(LoginPageLocators.VK_BUTTON)
        self.find_element(LoginPageLocators.MAIL_BUTTON)
        self.find_element(LoginPageLocators.YA_BUTTON)

    def click_login(self):
        self.find_element(LoginPageLocators.LOGIN_BUTTON).click()

    def get_error_text(self):
        return self.find_element(LoginPageLocators.ERROR_TEXT).text

    def send_login(self):
        self.find_element(LoginPageLocators.LOGIN_FIELD).send_keys("kek")