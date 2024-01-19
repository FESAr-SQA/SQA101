from Base.page_base import PageBase
from Locators.locators import ChangePasswordLocators, LoginLocators

class ChangePasswordPage(PageBase):
    def __init__(self, driver):
        super().__init__(driver)

    def write_old_password(self, old_pwd: str) -> None:
        '''It writes the old password on the input field'''
        try:
            self.driver.find_element(*ChangePasswordLocators.old_password_input).send_keys(old_pwd)
        except Exception as e:
            print(e)

    def write_new_password(self, new_pwd: str) -> None:
        '''It writes the new password on the input field'''
        try:
            self.driver.find_element(*ChangePasswordLocators.new_password_input).send_keys(new_pwd)
        except Exception as e:
            print(e)

    def write_confirm_password(self, confirm_pwd: str) -> None:
        '''It writes the confirm password on the input field'''
        try:
            self.driver.find_element(*ChangePasswordLocators.confirm_password_input).send_keys(confirm_pwd)
        except Exception as e:
            print(e)

    def click_on_submit(self) -> None:
        '''It makes a click on submit button to upload all data previously filled'''
        try:
            self.driver.find_element(*ChangePasswordLocators.submit_button).click()
        except Exception as e:
            print(e)