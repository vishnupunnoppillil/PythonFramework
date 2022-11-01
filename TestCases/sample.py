
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from Pages.Login import Login
import  HTMLTestRunner.runner
from HTMLTestRunner.runner import HTMLTestRunner

class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        cls.driver.get("https://opensource-demo.orangehrmlive.com/")
        cls.driver.maximize_window()

    def test_Log(self):
# drive = webdriver.Chrome(executable_path='../driver/chromedriver')
            driver=self.driver
            # config=Config()
            element_present = EC.presence_of_element_located((By.NAME, 'username'))
            WebDriverWait(driver, 30).until(element_present)
            login=Login(driver)
            login.enterUsername()
            login.enterPassword()
            login.clickLogin()

            # driver.find_element(By.NAME, 'username').send_keys('Admin')
            # driver.find_element(By.NAME, 'password').send_keys('admin123')
            # driver.find_element(By.XPATH, "//button[@type='submit']").click()
            print("hello")
    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()

if __name__ == "__main__":
    suite = unittest.TestSuite()
    runner = HTMLTestRunner(
        title='My unit test', open_in_browser=True)
    runner.run(suite)


