from Base.page_base import PageBase
from Locators.locators import NewCustomerLocators
import time

class NewCustomerPage(PageBase):
    def __init__(self, driver):
        super().__init__(driver)

    def click_on_input(self, input_name):
        try:
            element = ""
            if input_name == "Customer Name":
                element = self.driver.find_element(*NewCustomerLocators.customer_name_txt)
            elif  input_name == "Address":
                element = self.driver.find_element(*NewCustomerLocators.address_txt)
            
            element.click()
        except Exception as e:
            print(e)

    def verify_message_by_input_name(self, input_name, expected_message):
        try:
            element = ""
            if input_name == "Customer Name":
                element = self.driver.find_element(*NewCustomerLocators.customer_input_message)
            elif  input_name == "Address":
                pass
            #TODO: needs to implement message on address
            
            actual_message = element.text
        except Exception as e:
            print(e)

        assert actual_message == expected_message, f'El mensaje en el campo {input_name} es {actual_message}. Se esperaba {expected_message}'
        