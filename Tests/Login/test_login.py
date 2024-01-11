from Pages.login_page import LoginPage
import time
import pytest


@pytest.mark.usefixtures("setup")
class TestLogin:
    def test_login_positive(self):
        login = LoginPage(self.driver)
        login.open()
        login.write_username("mngr547360")
        time.sleep(5)
        login.write_password("YjAnEtU")
        time.sleep(5)
