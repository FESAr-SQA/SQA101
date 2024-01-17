from Pages.login_page import LoginPage
from Pages.home_page import HomePage
from Pages.common_page import CommonPage
from Pages.new_customer_page import NewCustomerPage
import pytest
import time
from Pages.edit_customer import EditCustomerPage


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
        addCustomer.write_on_input("Customer Name","Holmes")
        addCustomer.write_on_input("Gender","de mujerst")
        addCustomer.write_on_input("Date birth","01032002")
        addCustomer.write_on_input("Address", "Calle Bosques de Mexico 32")
        addCustomer.write_on_input("City","CiudaddeMexico")
        addCustomer.write_on_input("State","CDMX")
        addCustomer.write_on_input("Pin","548320")
        addCustomer.write_on_input("Phone","5599345690")
        email = addCustomer.write_email()
        addCustomer.write_on_input("Password","Bodoque")
        addCustomer.click_on_submit()
        id_data = addCustomer.getID()
        time.sleep(3)
        id_data = addCustomer.getID()
        time.sleep(1)
        common.click_on_button_menu("Edit Customer")
        time.sleep(2)

        editCustomer = EditCustomerPage(self.driver)
        editCustomer.write_id(id_data)
        editCustomer.click_on_login()
        time.sleep(5)
        editCustomer.verify_data_by_field("Customer Name", "Holmes")
        editCustomer.verify_data_by_field("Gender","de mujerst")
        editCustomer.verify_data_by_field("Date birth","01032002")
        editCustomer.verify_data_by_field("Address", "Calle Bosques de Mexico 32")
        editCustomer.verify_data_by_field("City","CiudaddeMexico")
        editCustomer.verify_data_by_field("State","CDMX")
        editCustomer.verify_data_by_field("Pin","548320")
        editCustomer.verify_data_by_field("Phone","5599345690")
        
    
        
        
        

