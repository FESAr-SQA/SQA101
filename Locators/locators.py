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
    customer_name_txt = (By.CSS_SELECTOR, "body > table > tbody > tr > td > table > tbody > tr:nth-child(4) > td:nth-child(2) > input[type=text]")
    customer_input_message = (By.ID, "message")
    address_txt = (By.CSS_SELECTOR, "body > table > tbody > tr > td > table > tbody > tr:nth-child(7) > td:nth-child(2) > textarea")
    city_txt = (By.CSS_SELECTOR, "body > table > tbody > tr > td > table > tbody > tr:nth-child(8) > td:nth-child(2) > input[type=text]")
    city_input_message =  (By.ID, "message4")