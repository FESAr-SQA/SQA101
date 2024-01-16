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
    customer_name_input = (By.NAME, "name")
    customer_gender_input = (By.XPATH, "/html/body/table/tbody/tr/td/table/tbody/tr[5]/td[2]/input[1]")
    customer_date_birth_input =(By.CSS_SELECTOR, "#dob")
    customer_address_input = (By.XPATH, "/html/body/table/tbody/tr/td/table/tbody/tr[7]/td[2]/textarea") 
    customer_city_input = (By.XPATH,  "/html/body/table/tbody/tr/td/table/tbody/tr[8]/td[2]/input") 
    customer_state_input = (By.XPATH,"/html/body/table/tbody/tr/td/table/tbody/tr[9]/td[2]/input")
    customer_pin_input = (By.XPATH, "/html/body/table/tbody/tr/td/table/tbody/tr[10]/td[2]/input")
    customer_telephone_input = (By.XPATH, "/html/body/table/tbody/tr/td/table/tbody/tr[11]/td[2]/input")
    customer_email_input = (By.XPATH, "/html/body/table/tbody/tr/td/table/tbody/tr[12]/td[2]/input")
    submit_add_customer_button = (By.XPATH, "/html/body/table/tbody/tr/td/table/tbody/tr[13]/td[2]/input[1]")

   

    