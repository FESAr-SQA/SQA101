from Pages.login_page import LoginPage
from Pages.common_page import CommonPage
from Pages.new_customer_page import NewCustomerPage
import pytest
import time

@pytest.mark.usefixtures("setup")
class TestNewCustomer:

    @pytest.mark.parametrize("expected message", [("Customer Name,", "Customer name must not be blank"), ("City", "Customer name must not be blank"), ("State", "Customer name must not be blank"), ("PIN", "Customer name must not be blank"), ("phone_number", "Customer name must not be blank"), ("email", "Customer name must not be blank")])
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
        newCustomer.click_on_input("Customer Name")
        newCustomer.click_on_input("Customer Name")
        newCustomer.click_on_input("Customer Name")
        newCustomer.click_on_input("Customer Name")
        newCustomer.click_on_input("Customer Name")
        newCustomer.click_on_input("Customer Name")
        newCustomer.click_on_input("Customer Name")
        newCustomer.click_on_input("Customer Name")
        newCustomer.click_on_input("Customer Name")
        newCustomer.click_on_input("Address")
        newCustomer.verify_message_by_input_name(*expected_message)

