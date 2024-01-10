from Base.page_base import PageBase
from Locators.locators import LoginLocators

class LoginPage(PageBase):
    def __init__(self, driver):
        super().__init__(driver)

    def write_username(self, username):
        self.driver.find_element(*LoginLocators.username).send_keys(username)