import time
import pytest
from Pages.fund_transfer_page import FundTranser
from Pages.common_page import CommonPage
from Pages.login_page import LoginPage


@pytest.mark.usefixtures("setup")
class TestFundTranser:

    def test_BSA_28_AC(self):
        login = LoginPage(self.driver)
        login.open()
        login.write_username("mngr547360")
        login.write_password("YjAnEtU")
        login.click_on_login()
        time.sleep(2)
        common = CommonPage(self.driver)
        common.click_on_button_menu("Fund Transfer")
        time.sleep(3)

        fund_transfer = FundTranser(self.driver)
        fund_transfer.write_payers_account("131294")
        fund_transfer.write_payees_account("131295")
        fund_transfer.write_amount("500")
        fund_transfer.write_description("nonas")
        fund_transfer.click_on_submit()
        time.sleep(5)
        fund_transfer.verify_data_by_field("From", "131294")
        fund_transfer.verify_data_by_field("To", "131295")
        fund_transfer.verify_data_by_field("Amount", "500")
        fund_transfer.verify_data_by_field("Description", "nonas")

        time.sleep(3)
        common.click_on_button_menu("Fund Transfer")
        fund_transfer.write_payers_account("131295")
        fund_transfer.write_payees_account("131294")
        fund_transfer.write_amount("500")
        fund_transfer.write_description("nonas")
        fund_transfer.click_on_submit()
        time.sleep(3)