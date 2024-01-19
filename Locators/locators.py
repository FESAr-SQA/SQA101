from selenium.webdriver.common.by import By


class CommonLocators:
    button_xpath = '//li/a[contains(text(),"{}")]'

class LoginLocators:
    # username = (By.XPATH, "/html/body/form/table/tbody/tr[1]/td[2]/input")
    # username = (By.CSS_SELECTOR, "body > form:nth-child(20) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > input:nth-child(1)")
    username = (By.NAME, "uid")
    password = (By.NAME, "password")
    login_button = (By.NAME, "btnLogin")
    reset_button = (By.NAME, "btnReset")


class HomeLocators:
    welcome_message = (By.CLASS_NAME, "heading3")

class NewCustomerLocators:
    customer_name_txt = (By.NAME, "name")
    customer_input_message = (By.ID, "message")
    gender_name = (By.XPATH, "/html/body/table/tbody/tr/td/table/tbody/tr[5]/td[2]/input[{}]".format(1))
    date_birth_txt = (By.NAME, "dob")
    address_txt = (By.NAME, "addr")
    city_name_txt = (By.NAME, "city")
    city_input_message = (By.ID, "message4")
    state_name_txt = (By.NAME, "state")
    state_input_message = (By.ID, "message5")
    pin_name_txt = (By.NAME, "pinno")
    pin_input_message = (By.ID, "message6")
    phone_name_txt = (By.NAME, "telephoneno")
    phone_number_input_message = (By.ID, "message7")
    email_name_txt = (By.NAME, "emailid")
    email_input_message = (By.ID, "message9")
    password_name_txt = (By.NAME, "password")
    submit_button = (By.NAME, "sub")
    id_customer_reg_msg = (By.XPATH, '//*[@id="customer"]/tbody/tr[4]/td[2]')

class EditCustomerLoginLocators:
    customer_id_input = (By.NAME, "cusid")
    # * LogIn button to edit
    submit_button = (By.NAME, "AccSubmit")

class EditCustomerLocators:
    customer_name_value = (By.NAME, "name")
    gender_value = (By.NAME, "gender")
    birthdate = (By.NAME, "dob")
    address_value = (By.NAME, "addr")
    city_value = (By.NAME, "city")
    state_value = (By.NAME, "state")
    pin_value = (By.NAME, "pinno")
    mobile_value = (By.NAME, "telephoneno")
    email_value = (By.NAME, "emailid")

class FundTransferLocators:
    payers_account_input = (By.NAME, "payersaccount")
    payers_account_input2 = (By.NAME, "payeeaccount")
    amount_input = (By.NAME, "ammount")
    description_input = (By.NAME, "desc")
    submit_button = (By.NAME, "AccSubmit")
    # * From now on these are the locators for the filled fields
    payers_account_field = (By.XPATH, "/html/body/table/tbody/tr[2]/td/table/tbody/tr[1]/td[2]")
    payees_account_field = (By.XPATH, "/html/body/table/tbody/tr[2]/td/table/tbody/tr[2]/td[2]")
    amount_field = (By.XPATH, "/html/body/table/tbody/tr[2]/td/table/tbody/tr[3]/td[2]")
    description_field = (By.XPATH, "/html/body/table/tbody/tr[2]/td/table/tbody/tr[4]/td[2]")