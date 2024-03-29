from Pages.login_page import LoginPage
from Pages.home_page import HomePage
import pytest
import time
from Pages.common_page import CommonPage


@pytest.mark.usefixtures("setup")
class TestLogin:

    @pytest.mark.parametrize("expected_message", [("Welcome To Manager's Page of GTPL Bank"), ("BIENVENIDO"), ("ñksadjfañsldkjfalsdkfj")])
    def test_login_positive(self, expected_message):
        login = LoginPage(self.driver)
        login.open()
        login.write_username("mngr547360")
        login.write_password("Qwerty@1")
        login.click_on_login()
        time.sleep(2)
        home = HomePage(self.driver)

        # actual_welcome_message = home.get_welcome_message()
        # expected_welcome_message = "BIENVENIDO"
        # assert actual_welcome_message == expected_welcome_message, "Algo fallo xd"
        # home.verify_welcome_message(expected_welcome_message)
        home.verify_welcome_message(expected_message)
    
    # @pytest.mark.parametrize("number_1, number_2, expected_result", 
    #                           [(1,2,3),
    #                            (5,5,10),
    #                            (9,3,12),
    #                            (23,52,10)]
    #                         )
    # def test_sums(self, number_1, number_2, expected_result):
    #     assert number_1 + number_2 == expected_result
    def test_BSA_37(self):
        login = LoginPage(self.driver)
        login.open()
        login.write_username("username")
        login.write_password("password")
        login.click_on_login()
        alert = CommonPage(self.driver)
        alert.verify_alert_message("User or Password is not valid")
    