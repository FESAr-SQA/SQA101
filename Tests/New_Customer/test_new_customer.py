from Pages.login_page import LoginPage
from Pages.home_page import HomePage
from Pages.common_page import CommonPage
from Pages.new_customer_page import NewCustomerPage
import pytest
import time

@pytest.mark.usefixtures("setup")
class TestNewCustomer:

    def test_new_customer_input_message(self):
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
        newCustomer.click_on_input("Address")
        newCustomer.verify_message_by_input_name("Customer Name", "Customer name must not be blank")

    def test_BSA_1_GLA(self):

        login = LoginPage(self.driver)
        login.open()
        login.write_username("mngr547360")
        login.write_password("YjAnEtU")
        login.click_on_login()

        common = CommonPage(self.driver)
        common.click_on_button_menu("New Customer")

        addCustomer = NewCustomerPage(self.driver)
        time.sleep(2)
        addCustomer.write_on_input("Customer Name","Benito camelo")
        addCustomer.write_on_input("Gender","de mujerst")
        addCustomer.write_on_input("Date birth","01032002")
        addCustomer.write_on_input("Address", "Calle Bosques de Mexico 32")
        addCustomer.write_on_input("City","Ciudad de Mexico")
        addCustomer.write_on_input("State","CDMX")
        addCustomer.write_on_input("Pin","57170")
        addCustomer.write_on_input("Phone","5599345690")
        addCustomer.write_on_input("email","Hola@test.com")
        addCustomer.click_on_input("Submit")
        


        
        
        

