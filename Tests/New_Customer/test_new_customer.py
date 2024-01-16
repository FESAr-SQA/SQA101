from Pages.edit_customer_page import EditCustomerPage
from Pages.login_page import LoginPage
from Pages.common_page import CommonPage
from Pages.new_customer_page import NewCustomerPage
import pytest
import time

@pytest.mark.usefixtures("setup")
class TestNewCustomer:

    @pytest.mark.parametrize("expected_message", [("Customer Name", "Customer name must not be blank"), ("City", "City Field must be not blank"), ("State", "State must not be blank"), ("PIN", "PIN Code must not be blank"), ("Phone_number", "Telephone no must not be blank"), ("Email", "Email-ID must not be blank")])
    def test_new_customer_input_message(self, expected_message):
        login = LoginPage(self.driver)
        login.open()
        login.write_username("mngr547360")
        login.write_password("YjAnEtU")
        login.click_on_login()
        time.sleep(2)
        common = CommonPage(self.driver)
        common.click_on_button_menu("New Customer")

        newCustomer = NewCustomerPage(self.driver)
        newCustomer.click_on_input("Customer Name")
        time.sleep(2)
        newCustomer.click_on_input("City")
        time.sleep(2)
        newCustomer.click_on_input("State")
        time.sleep(2)
        newCustomer.click_on_input("PIN")
        time.sleep(2)
        newCustomer.click_on_input("Phone_number")
        time.sleep(2)
        newCustomer.click_on_input("Email")
        time.sleep(2)
        newCustomer.click_on_input("Address")
        newCustomer.verify_message_by_input_name(*expected_message)
    
    def test_BSA_3_AC(self):
        login = LoginPage(self.driver)
        login.open()
        login.write_username("mngr547360")
        login.write_password("YjAnEtU")
        login.click_on_login()
        time.sleep(2)
        common = CommonPage(self.driver)
        common.click_on_button_menu("New Customer")

        newCustomer = NewCustomerPage(self.driver)
        newCustomer.write_customer_name("Holmes")
        time.sleep(1)
        newCustomer.write_date_of_birth("2072000")
        time.sleep(1)
        newCustomer.write_address("Baker Street 221B")
        time.sleep(1)
        newCustomer.write_city("London")
        time.sleep(1)
        newCustomer.write_state("London")
        time.sleep(1)
        newCustomer.write_pin("548320")
        time.sleep(1)
        newCustomer.write_phone("5")
        time.sleep(1)
        newCustomer.write_email("planosd@aol.com")
        time.sleep(1)
        newCustomer.write_password("YjAnEtU")
        time.sleep(1)
        newCustomer.click_on_submit()
        time.sleep(3)
        id_data = newCustomer.getID()
        time.sleep(1)

        common.click_on_button_menu("Edit Customer")
        time.sleep(2)

        editCustomer = EditCustomerPage(self.driver)
        editCustomer.write_id(id_data)
        editCustomer.click_on_login()
        time.sleep(3)
        editCustomer.verify_data_by_field("PIN", "548320")
        editCustomer.verify_data_by_field("Customer Name", "Holmes")

