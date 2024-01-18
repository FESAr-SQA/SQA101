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
            elif  input_name == "City":
                element = self.driver.find_element(*EditCustomerLocators.city_value)
            elif  input_name == "State":
                element = self.driver.find_element(*EditCustomerLocators.state_value)
            elif  input_name == "PIN":
                element = self.driver.find_element(*EditCustomerLocators.pin_value)
            elif  input_name == "Phone_number":
                element = self.driver.find_element(*EditCustomerLocators.mobile_value)
            elif  input_name == "Email":
                element = self.driver.find_element(*EditCustomerLocators.email_value)
            elif  input_name == "Address":
                element = self.driver.find_element(*EditCustomerLocators.a)

            current_data = element.get_attribute("value")
        except Exception as e:
            print(e)