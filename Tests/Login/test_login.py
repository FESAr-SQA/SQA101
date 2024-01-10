from Pages.login_page import LoginPage
import pytest


@pytest.mark.usefixtures("setup")
class TestLogin:
    def test_login_positive(self):
        login = LoginPage(self.driver)
        login.open()
        login.write_username("mngr547360")
        import time
        time.sleep(5)
