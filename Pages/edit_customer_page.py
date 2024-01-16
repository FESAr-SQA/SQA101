from selenium.webdriver.chrome.webdriver import WebDriver
from Base.page_base import PageBase
from Locators.locators import EditCustomerLocators, EditCustomerLoginLocators


class EditCustomerPage(PageBase):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
    
    def click_on_login(self):
        try:
            self.driver.find_element(*EditCustomerLoginLocators.submit_button).click()
        except Exception as e:
            print(e)

    def write_id(self, id_data: str):
        try:
            self.driver.find_element(*EditCustomerLoginLocators.customer_id_input).send_keys(id_data)
        except Exception as e:
            print(e)
    
    def verify_data_by_field(self, input_name, expected_data):
        try:
            element = ""
            current_data = ""
            if input_name == "Customer Name":
                element = self.driver.find_element(*EditCustomerLocators.customer_name_value)
            elif input_name == "PIN":
                element = self.driver.find_element(*EditCustomerLocators.pin_value)
            
            current_data = element.get_attribute("value")
        except Exception as e:
            print(e)

        assert current_data == expected_data, f'El mensaje en el campo {input_name} es {current_data}. Se esperaba {expected_data}'
    