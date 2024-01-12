from Base.page_base import PageBase
from Locators.locators import HomeLocators
import time

class HomePage(PageBase):
    def __init__(self, driver):
        super().__init__(driver)

    def get_welcome_message(self):
        return self.driver.find_element(*HomeLocators.welcome_message).text
    
    def verify_welcome_message(self, expected_message):
        try:
            actual_message = self.driver.find_element(*HomeLocators.welcome_message).text
        except Exception as e:
            print(e)
        #assert actual_message == expected_message, "El mesnaje de bienvenida no es el correcto."
        assert actual_message == expected_message, f'El mensaje de bienvenida es "{actual_message}". Se esperaba "{expected_message}"'