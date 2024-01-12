from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from Helpers.webdriver_listener import WebDriverListener
from Extensions.webdriver_extensions import WebDriverExtended
from selenium.webdriver.chrome.service import Service

class DriverFactory:
    @staticmethod
    def get_driver(config) -> WebDriverExtended:
        if config["browser"] == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("start-maximized")
            if config["headless_mode"] is True:
                options.add_argument("--headless")

            service = Service(ChromeDriverManager().install())
            driver = WebDriverExtended(
                webdriver.Chrome(service=service, options=options),
                WebDriverListener(), config
            )

            return driver
        elif config["browser"] == "firefox":
            options = webdriver.FirefoxOptions()
            if config["headless_mode"] is True:
                options.headless = True
            driver = WebDriverExtended(
                #webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options),
                webdriver.Firefox(options=options),
                WebDriverListener(), config
            )
            return driver
        raise Exception("Provide valid driver name")
