from Pages.login_page import LoginPage
from Pages.home_page import HomePage
import pytest
import time

@pytest.mark.usefixtures("setup")
class TestLogin:

    def test_login_positive(self):
        login = LoginPage(self.driver)
        login.open()
        login.write_username("mngr547360")
        login.write_password("YjAnEtU")
        login.click_on_login()
        time.sleep(2)
        home = HomePage(self.driver)

        # actual_welcome_message = home.get_welcome_message()
        expected_welcome_message = "BIENVENIDO"
        # assert actual_welcome_message == expected_welcome_message, "Algo fallo xd"
        home.verify_welcome_message(expected_welcome_message)
