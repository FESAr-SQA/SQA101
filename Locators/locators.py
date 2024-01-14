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