import time
import pytest
from Pages.change_password_page import ChangePasswordPage
from Pages.fund_transfer_page import FundTransferPage
from Pages.common_page import CommonPage
from Pages.login_page import LoginPage


@pytest.mark.usefixtures("setup")
class TestChangePassword:

    def test_BSA_33_AC(self) -> None:
        '''Test for change password and validate the functionality'''

        login = LoginPage(self.driver)
        login.open()
        login.write_username("mngr547360")
        login.write_password("YjAnEtU")
        login.click_on_login()
        time.sleep(2)
        common = CommonPage(self.driver)
        common.click_on_button_menu("Change Password")
        time.sleep(3)
        # * Move to Change Password tab

        change_password = ChangePasswordPage()
        change_password.write_old_password("zEvysAq")
        change_password.write_new_password("Qwerty@1")
        change_password.write_confirm_password("Qwerty@1")
        change_password.click_on_submit()
        time.sleep(2)
        common.click_ok_on_alert()
        time.sleep(2)

        # * Verify the login

        login = LoginPage(self.driver)
        login.open()
        login.write_username("mngr547360")
        login.write_password("YjAnEtU")
        login.click_on_login()
        time.sleep(2)
