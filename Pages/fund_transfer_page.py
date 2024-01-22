from Base.page_base import PageBase
from Locators.locators import FundTransferLocators


class FundTransferPage(PageBase):
    def __init__(self, driver):
        super().__init__(driver)
    
    def click_on_submit(self) -> None:
        '''It makes a click on submit button to upload all data previously filled'''
        try:
            self.driver.find_element(*FundTransferLocators.submit_button).click()
        except Exception as e:
            print(e)
    
    def verify_data_by_field(self, input_field: str, expected_field: str) -> None:
        '''Verify the input data with the expected data'''
        try:
            element = ""
            current_data = ""
            if input_field == "From":
                element = self.driver.find_element(*FundTransferLocators.payers_account_field)
            elif input_field == "To":
                element = self.driver.find_element(*FundTransferLocators.payees_account_field)
            elif input_field == "Amount":
                element = self.driver.find_element(*FundTransferLocators.amount_field)
            elif input_field == "Description":
                element = self.driver.find_element(*FundTransferLocators.description_field)


            current_data = element.text
        except Exception as e:
            print(e)

        assert current_data == expected_field, f'El dato en el campo {input_field} es {current_data}. Se esperaba {expected_field}'
    
    
    def write_payers_account(self, account: str) -> None:
        '''It writes the payers account number'''
        try:
            self.driver.find_element(*FundTransferLocators.payers_account_input).send_keys(account)
        except Exception as e:
            print(e)

    def write_payees_account(self, account: str) -> None:
        '''It writes the payees account number'''
        try:
            self.driver.find_element(*FundTransferLocators.payers_account_input2).send_keys(account)
        except Exception as e:
            print(e)

    def write_amount(self, amount: str) -> None:
        '''It writes the amount'''
        try:
            self.driver.find_element(*FundTransferLocators.amount_input).send_keys(amount)
        except Exception as e:
            print(e)

    def write_description(self, description: str) -> None:
        '''It writes the description'''
        try:
            self.driver.find_element(*FundTransferLocators.description_input).send_keys(description)
        except Exception as e:
            print(e)