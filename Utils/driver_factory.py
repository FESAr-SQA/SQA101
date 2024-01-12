from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from Helpers.webdriver_listener import WebDriverListener
from Extensions.webdriver_extensions import WebDriverExtended
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

class DriverFactory:
    @staticmethod
    def get_driver(config) -> WebDriverExtended:
        if config["browser"] == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("start-maximized")
            options.add_extension("Extensions//chrome_extensions//ublock.crx")
            if config["headless_mode"] is True:
                options.add_argument("--headless")

            service = ChromeService(ChromeDriverManager().install())
            driver = WebDriverExtended(
                webdriver.Chrome(service=service, options=options),
                WebDriverListener(), config
            )

            return driver
        elif config["browser"] == "firefox":
            options = webdriver.FirefoxOptions()
            #TODO: Investigar como añadir extensiones al webdriver de Firefox 
            if config["headless_mode"] is True:
                options.headless = True
            service = FirefoxService(GeckoDriverManager().install())
            driver = WebDriverExtended(
                webdriver.Firefox(service=service, options=options),
                WebDriverListener(), config
            )
            return driver
        raise Exception("Provide valid driver name")