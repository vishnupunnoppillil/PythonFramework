from  selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from Utilities.readProperties import ReadConfig

@pytest.fixture()
def test_setup(browser):
    global driver
    if browser=='chrome':
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        print("launching chrome")
    elif browser=='safari':
        print("launching safari")
        driver = webdriver.Safari()
    driver.get(ReadConfig.getApplicationURL())
    driver.maximize_window()
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

def pytest_configure(config):
        config._metadata['Project Name']='Orange HRM'
        config._metadata['Module Name'] = 'Learn'
        config._metadata['Tester'] = 'Vishnu Vijayan'

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Pluggins", None)
