from Base.page_base import PageBase
from Locators.locators import ChangePasswordLocators

class ChangePasswordPage(PageBase):
    def __init__(self, driver):
        super().__init__(driver)

    def click_on_submit(self) -> None:
        '''It makes a click on submit button to upload all data previously filled'''
        try:
            self.driver.find_element(*ChangePasswordLocators.submit_button).click()
        except Exception as e:
            print(e)
    
    def verify_user_id(self, expected_id: str) -> None:
        '''
        It verifies the changed password accesing with the new password.
        It also verifies the user id
        '''
        try:
            element = ""
            current_data = ""
            element = self.driver.find_element(*ChangePasswordLocators.manager_id_data)
            current_data = element.text
            phrase = current_data.split()
            user_id = phrase[-1]

        except Exception as e:
            print(e)

        assert user_id == expected_id, f'El usuario manager es {user_id}. Se esperaba {expected_id}'
    
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
