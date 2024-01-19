from selenium.webdriver.chrome.webdriver import WebDriver
from Base.page_base import PageBase
from Locators.locators import EditCustomerLocators, EditCustomerLoginLocators


class EditCustomerPage(PageBase):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
    
    def loginID(self):
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
            elif input_name == "Gender":
                element = self.driver.find_element(*EditCustomerLocators.gender_value)
            elif input_name == "Birth":
                element = self.driver.find_element(*EditCustomerLocators.birthdate)
            elif input_name == "Address":
                element = self.driver.find_element(*EditCustomerLocators.address_value)
            elif input_name == "City":
                element = self.driver.find_element(*EditCustomerLocators.city_value)
            elif input_name == "State":
                element = self.driver.find_element(*EditCustomerLocators.state_value)
            elif input_name == "PIN":
                element = self.driver.find_element(*EditCustomerLocators.pin_value)
            elif input_name == "Phone":
                element = self.driver.find_element(*EditCustomerLocators.mobile_value)
            elif input_name == "Email":
                element = self.driver.find_element(*EditCustomerLocators.email_value)


            current_data = element.get_attribute("value")
            if current_data == "m" and input_name == "Gender":
                current_data = "male"
        except Exception as e:
            print(e)

        assert current_data == expected_data, f'El dato en el campo {input_name} es {current_data}. Se esperaba {expected_data}'
    