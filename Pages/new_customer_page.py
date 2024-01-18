import random
import string
from Base.page_base import PageBase
from Locators.locators import NewCustomerLocators


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
    
    def write_gender(self) -> None:
        try:
            self.driver.find_element(*NewCustomerLocators.gender_name).click()
        except Exception as e:
            print(e)


    def write_date_of_birth(self, date: str):
        try:
            self.driver.find_element(*NewCustomerLocators.date_birth_txt).send_keys(date)
        except Exception as e:
            print("Cannot write date")
            print(e)

    def write_address(self, address: str):
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

    def write_email(self) -> str:
        '''This method returns the random email as soon as it sends to the required field'''
        length = 5
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for _ in range(length))
        result_str += '@aol.com'

        try:
            self.driver.find_element(*NewCustomerLocators.email_name_txt).send_keys(result_str)
            return result_str
        except Exception as e:
            print(e)

    def write_password(self, password: str) -> None:
        try:
            self.driver.find_element(*NewCustomerLocators.password_name_txt).send_keys(password)
        except Exception as e:
            print(e)

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
            if input_name == "Password":
                self.driver.find_element(*NewCustomerLocators.password_name_txt).send_keys(info_data)
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
                element = self.driver.find_element(*NewCustomerLocators.customer_address_input)
        except Exception as e: 
                pass
        
    def getID(self) -> str:
        try:
            element = self.driver.find_element(*NewCustomerLocators.id_customer_reg_msg)
            return element.text
        except Exception as e:
            return e

    def write_email(self) -> str:

        length = 5
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for _ in range(length))
        result_str += '@gogogomail.com'

        try:
            self.driver.find_element(*NewCustomerLocators.email_name_txt).send_keys(result_str)
            return result_str
        except Exception as e:
            print(e)
            
        
