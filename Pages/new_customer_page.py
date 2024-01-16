from Base.page_base import PageBase
from Locators.locators import NewCustomerLocators
# from selenium.webdriver.common.by import By
# import time

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
            elif  input_name == "City":
                element = self.driver.find_element(*NewCustomerLocators.city_name_txt)
            elif  input_name == "State":
                element = self.driver.find_element(*NewCustomerLocators.state_name_txt)
            elif  input_name == "PIN":
                element = self.driver.find_element(*NewCustomerLocators.pin_name_txt)
            elif  input_name == "Phone_number":
                element = self.driver.find_element(*NewCustomerLocators.phone_name_txt)
            elif  input_name == "Email":
                element = self.driver.find_element(*NewCustomerLocators.email_name_txt)

            element.click()
        except Exception as e:
            print(e)
    
    def click_on_submit(self):
        try:
            self.driver.find_element(*NewCustomerLocators.submit_button).click()
        except Exception as e:
            print(e)

    def verify_message_by_input_name(self, input_name, expected_message):
        try:
            element = ""
            actual_message = ""
            if input_name == "Customer Name":
                element = self.driver.find_element(*NewCustomerLocators.customer_input_message)
            elif  input_name == "City":
                element = self.driver.find_element(*NewCustomerLocators.city_input_message)
            elif  input_name == "State":
                element = self.driver.find_element(*NewCustomerLocators.state_input_message)
            elif  input_name == "PIN":
                element = self.driver.find_element(*NewCustomerLocators.pin_input_message)
            elif  input_name == "Phone_number":
                element = self.driver.find_element(*NewCustomerLocators.phone_number_input_message)
            elif  input_name == "Email":
                element = self.driver.find_element(*NewCustomerLocators.email_input_message)
            elif  input_name == "Address":
                pass
            #TODO: needs to implement message on address

            actual_message = element.text
        except Exception as e:
            print(e)

        assert actual_message == expected_message, f'El mensaje en el campo {input_name} es {actual_message}. Se esperaba {expected_message}'
    
    def getID(self) -> str:
        try:
            element = self.driver.find_element(*NewCustomerLocators.id_customer_reg_msg)
            return element.text
        except Exception as e:
            return e
    
    def write_customer_name(self, customer: str) -> None:
        try:
            self.driver.find_element(*NewCustomerLocators.customer_name_txt).send_keys(customer)
        except Exception as e:
            print(e)

    def write_date_of_birth(self, date):
        try:
            self.driver.find_element(*NewCustomerLocators.date_birth_txt).send_keys(date)
        except Exception as e:
            print("Cannot write date")
            print(e)

    def write_address(self, address):
        try:
            self.driver.find_element(*NewCustomerLocators.address_txt).send_keys(address)
        except Exception as e:
            print(e)

    def write_city(self, city: str) -> None:
        try:
            self.driver.find_element(*NewCustomerLocators.city_name_txt).send_keys(city)
        except Exception as e:
            print(e)

    def write_state(self, state: str) -> None:
        try:
            self.driver.find_element(*NewCustomerLocators.state_name_txt).send_keys(state)
        except Exception as e:
            print(e)

    def write_pin(self, pin: str) -> None:
        try:
            self.driver.find_element(*NewCustomerLocators.pin_name_txt).send_keys(pin)
        except Exception as e:
            print(e)

    def write_phone(self, phone: str) -> None:
        try:
            self.driver.find_element(*NewCustomerLocators.phone_name_txt).send_keys(phone)
        except Exception as e:
            print(e)

    def write_email(self, email: str) -> None:
        try:
            self.driver.find_element(*NewCustomerLocators.email_name_txt).send_keys(email)
        except Exception as e:
            print(e)

    def write_password(self, password: str) -> None:
        try:
            self.driver.find_element(*NewCustomerLocators.password_name_txt).send_keys(password)
        except Exception as e:
            print(e)
