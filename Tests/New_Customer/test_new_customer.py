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
        newCustomer.write_gender()
        newCustomer.write_date_of_birth("02072000")
        newCustomer.write_address("Baker Street 221B")
        newCustomer.write_city("London")
        newCustomer.write_state("London")
        newCustomer.write_pin("548320")
        newCustomer.write_phone("5")
        email = newCustomer.write_email()
        newCustomer.write_password("YjAnEtU")
        newCustomer.click_on_submit()
        time.sleep(3)
        id_data = newCustomer.getID()

        common.click_on_button_menu("Edit Customer")
        time.sleep(2)

        editCustomer = EditCustomerPage(self.driver)
        editCustomer.write_id(id_data)
        editCustomer.loginID()
        time.sleep(5)
        editCustomer.verify_data_by_field("Customer Name", "Holmes")
        editCustomer.verify_data_by_field("Gender", "male")
        editCustomer.verify_data_by_field("Birth", "2000-02-07")
        editCustomer.verify_data_by_field("Address", "Baker Street 221B")
        editCustomer.verify_data_by_field("City", "London")
        editCustomer.verify_data_by_field("State", "London")
        editCustomer.verify_data_by_field("PIN", "548320")
        editCustomer.verify_data_by_field("Phone", "5")
        editCustomer.verify_data_by_field("Email", email)

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
        


        
        
        

