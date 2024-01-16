from Base.page_base import PageBase
from Locators.locators import NewCustomerLocators
from selenium.webdriver.common.by import By
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

    def write_on_input(self, input_name, info_data):
        try:
            if input_name == "Customer Name":
                self.driver.find_element(*NewCustomerLocators.customer_name_input).send_keys(info_data)
            if input_name == "Gender":
                gender_selector = '/html/body/table/tbody/tr/td/table/tbody/tr[5]/td[2]/input[{}]'
                if info_data == "male":
                    self.driver.find_element(By.XPATH, gender_selector.format(1)).click()
                elif info_data == "de mujerst":
                    self.driver.find_element(By.XPATH, gender_selector.format(2)).click()
            if input_name == "Date birth":
                self.driver.find_element(*NewCustomerLocators.customer_date_birth_input).send_keys(info_data)
            if input_name == "Address":
                self.driver.find_element(*NewCustomerLocators.customer_address_input).send_keys(info_data)
            if input_name == "City":
                self.driver.find_element(*NewCustomerLocators.customer_city_input).send_keys(info_data)
            if input_name == "State":
                self.driver.find_element(*NewCustomerLocators.customer_state_input).send_keys(info_data)
            if input_name == "Pin":
                self.driver.find_element(*NewCustomerLocators.customer_pin_input).send_keys(info_data)
            if input_name == "Phone":
                self.driver.find_element(*NewCustomerLocators.customer_telephone_input).send_keys(info_data)
            if input_name == "email":
                self.driver.find_element(*NewCustomerLocators.customer_email_input).send_keys(info_data)
            if input_name == "Submit":
                self.driver.find_element(*NewCustomerLocators.submit_add_customer_button).click()
        except Exception as e:
            print(e)
            
        
        
