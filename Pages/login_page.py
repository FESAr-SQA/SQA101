from Base.page_base import PageBase
from Locators.locators import LoginLocators
import time

class LoginPage(PageBase):
    def __init__(self, driver):
        super().__init__(driver)

    def write_username(self, username):
        try:
            self.driver.find_element(*LoginLocators.username).send_keys(username)
        except Exception as e:
            print(e)

    def write_password(self, password):
        try:
            self.driver.find_element(*LoginLocators.password).send_keys(password)
        except Exception as e:
            print(e)

    def click_on_login(self):
        try:
            self.driver.find_element(*LoginLocators.login_button).click()
        except Exception as e:
            print(e)
