from Pages.login_page import LoginPage
from Pages.common_page import CommonPage
from Pages.new_customer_page import NewCustomerPage
import pytest
import time

@pytest.mark.usefixtures("setup")
class TestNewCustomer:

    # @pytest.mark.parametrize("expected_message", [("Customer Name,", "Customer name must not be blank")])
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

