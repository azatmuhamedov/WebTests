import allure

from pages.BasePage import BasePageHelper
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
    RESTORE_BUTTON = (By.XPATH, "//a[contains(@class,'vkuiButton__modePrimary')]")
    GO_BACK_BUTTON = (By.XPATH, "//div[5]/button[contains(@class,'vkuiButton__modeSecondary')]")

class LoginPageHelper(BasePageHelper):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step('Проверяем корректность загрузки страницы'):
            self.attach_screenshot()
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

    @allure.step('Нажимаем на кнопку "Войти"')
    def click_login(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.LOGIN_BUTTON).click()

    @allure.step('Получаем текст ошибки')
    def get_error_text(self):
        self.attach_screenshot()
        return self.find_element(LoginPageLocators.ERROR_TEXT).text

    @allure.step('Заполняем поле логина')
    def send_login(self, login):
        self.find_element(LoginPageLocators.LOGIN_FIELD).send_keys(login)
        self.attach_screenshot()


    @allure.step('Заполняем поле пароля')
    def send_password(self, password):
        self.find_element(LoginPageLocators.PASSWORD_FIELD).send_keys(password)
        self.attach_screenshot()

    @allure.step('Переходим к восстановлению')
    def click_recovery(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.RESTORE_BUTTON).click()

    @allure.step('Переходим к регистрации')
    def click_registration(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.SIGN_UP_BUTTON).click()

