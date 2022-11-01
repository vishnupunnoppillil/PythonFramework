
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from Pages.Login import Login
from HTMLTestRunner.runner import HTMLTestRunner
import pytest
class Test_Selenium():
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://opensource-demo.orangehrmlive.com/")
        driver.maximize_window()
        yield
        driver.close()

    def test_Log(self,test_setup):
        element_present = EC.presence_of_element_located((By.NAME, 'username'))
        WebDriverWait(driver, 30).until(element_present)
        login=Login(driver)
        login.enterUsername()
        login.enterPassword()
        login.clickLogin()

    def test_Log1(self,test_setup):
        element_present = EC.presence_of_element_located((By.NAME, 'username'))
        WebDriverWait(driver, 30).until(element_present)
        login=Login(driver)
        login.enterUsername()
        login.enterPassword()
        login.clickLogin()

    # def test_tearDownClass():
    #     driver.close()


