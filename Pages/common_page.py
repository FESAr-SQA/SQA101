from selenium.webdriver.common.by import By
from Base.page_base import PageBase
from Locators.locators import CommonLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CommonPage(PageBase):
    def __init__(self, driver):
        super().__init__(driver)
    
    def click_on_button_menu(self, menu_name):
        try:
            formated_locator = CommonLocators.button_xpath.format(menu_name)
            locator = (By.XPATH, formated_locator)
            self.driver.find_element(*locator).click()
        except Exception as e:
            print(e)
    def verify_alert_message(self, expected_message):
        WebDriverWait(self.driver,timeout=5).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        assert expected_message in alert_text, f"Mensaje de alerta inesperado: {alert_text}"

    def accept_alert(self):
        WebDriverWait(self.driver,timeout=5).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.accept()