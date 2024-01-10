from selenium.webdriver.chrome.webdriver import WebDriver

class PageBase:
    def __init__(self, driver:WebDriver):
        self.driver = driver

    def open(self):
        self.driver.open()