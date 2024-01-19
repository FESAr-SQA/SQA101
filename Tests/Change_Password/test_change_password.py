import time
import pytest
from Pages.change_password_page import ChangePasswordPage
from Pages.common_page import CommonPage
from Pages.login_page import LoginPage


@pytest.mark.usefixtures("setup")
class TestChangePassword:

    def test_BSA_33_AC(self) -> None:
        '''Test for change password and validate the functionality'''
        login = LoginPage(self.driver)
        login.open()
        login.write_username("mngr547360")
        login.write_password("Qwerty@1")
        login.click_on_login()
        time.sleep(2)
        common = CommonPage(self.driver)
        common.click_on_button_menu("Change Password")
        time.sleep(3)

        # * Move to Change Password tab and fill data
        change_password = ChangePasswordPage(self.driver)
        change_password.write_old_password("Qwerty@1")
        change_password.write_new_password("Qwerty@2")
        change_password.write_confirm_password("Qwerty@2")
        change_password.click_on_submit()
        time.sleep(3)
        common.accept_alert()
        time.sleep(3)

        login.open()
        login.write_username("mngr547360")
        login.write_password("Qwerty@2")
        login.click_on_login()
        time.sleep(2)

        # * Verify the login
        change_password.verify_user_id("mngr547360")

        # * Restoring the original password
        common.click_on_button_menu("Change Password")
        time.sleep(3)
        change_password.write_old_password("Qwerty@2")
        change_password.write_new_password("Qwerty@1")
        change_password.write_confirm_password("Qwerty@1")
        change_password.click_on_submit()
        time.sleep(3)
        common.accept_alert()
        time.sleep(2)