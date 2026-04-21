import allure
import random
from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class RegistrationPageLocators:
    COUNTRY_LIST = (By.XPATH, '//*[@class="vkuiFormField__iconWrapper"]')
    PHONE_FIELD = (By.XPATH, '//*[@type="tel"]')
    SUBMIT_BUTTON = (By.XPATH, '//button[contains(@class,"vkuiButton__modePrimary")]')
    COUNTRY_ITEM = (By.XPATH, '//span[text()="+"]')

class RegistrationPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step('Проверяем корректность загрузки страницы'):
            self.attach_screenshot()
            self.find_element(RegistrationPageLocators.PHONE_FIELD)
            self.find_element(RegistrationPageLocators.COUNTRY_LIST)
            self.find_element(RegistrationPageLocators.SUBMIT_BUTTON)

    @allure.step('Выбираем страну')
    def select_random_country(self):
        random_number = random.randint(0, 205)
        self.find_element(RegistrationPageLocators.COUNTRY_LIST).click()
        country_items = self.find_elements(RegistrationPageLocators.COUNTRY_ITEM)
        country_code = country_items[random_number].get_attribute('text')
        country_items[random_number].click()
        return country_code

    @allure.step('Проверяем код страны')
    def get_phone_field_value(self):
        return self.find_element(RegistrationPageLocators.PHONE_FIELD).get_attribute('text')