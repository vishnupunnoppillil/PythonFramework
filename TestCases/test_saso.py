
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from Pages.Login import Login
from HTMLTestRunner.runner import HTMLTestRunner
import pytest

def setup_module(module):
        global driver
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://opensource-demo.orangehrmlive.com/")
        driver.maximize_window()

def teardown_module(module):
        driver.close()

def test_Log():
        element_present = EC.presence_of_element_located((By.NAME, 'username'))
        WebDriverWait(driver, 30).until(element_present)
        login=Login(driver)
        login.enterUsername()
        login.enterPassword()
        login.clickLogin()

def test_Log1():
        element_present = EC.presence_of_element_located((By.NAME, 'username'))
        WebDriverWait(driver, 30).until(element_present)
        login=Login(driver)
        login.enterUsername()
        login.enterPassword()
        login.clickLogin()




