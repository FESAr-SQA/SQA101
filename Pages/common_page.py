from Base.page_base import PageBase
from selenium.webdriver.common.by import By
from Locators.locators import CommonLocators
import time

class CommonPage(PageBase):
    def __init__(self, driver):
        super().__init__(driver)


    def click_on_button_menu(self, menu_name):
        try:
            formated_locator = CommonLocators.button_xpath.format(menu_name)
            print(formated_locator)
            locator = (By.XPATH, formated_locator)
            self.driver.find_element(*locator).click()
        except Exception as e:
            print(e)