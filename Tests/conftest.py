import json
import pytest
import time

from Utils.driver_factory import DriverFactory

CONFIG_PATH = "config.json"
DEFAULT_WAIT_TIME = 10
SUPPORTED_BROWSERS = ["chrome","firefox", "edge"]
BASE_URL = "https://demo.guru99.com/V1/index.php"


@pytest.fixture(scope="session")
def config():
    confif_file = open(CONFIG_PATH)
    return json.load(confif_file)

@pytest.fixture(scope="session")
def browser_setup(config):
    if "browser" not in config:
        raise Exception("El archivo de configuracion no tiene definido 'browser'")
    elif config["browser"] not in SUPPORTED_BROWSERS:
        raise Exception(f'El navegador "{config["browser"]}" no tiene soporte')
    return config["browser"]

@pytest.fixture(scope="session")
def wait_time_setup(config):
    return config["wait_time"] if 'wait_time' in config else DEFAULT_WAIT_TIME


@pytest.fixture(scope="session")
def url_setup(config):
    return config["base_url"] if "base_url" in config else BASE_URL

@pytest.fixture()
def setup(request, config):
    driver = DriverFactory.get_driver(config)
    driver.implicitly_wait(config["timeout"])
    request.cls.driver = driver
    before_failed = request.session.testsfailed
    if config["browser"] == "firefox":
        driver.maximize_window()
    time.sleep(2.5)
    yield
    if request.session.testsfailed != before_failed:
        pass
        # tomar captura de pantalla
    
    driver.quit()
