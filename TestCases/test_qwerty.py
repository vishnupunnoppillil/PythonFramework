import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Utilities.readProperties import ReadConfig
from Utilities.Logger import LogGeneration
from Utilities import ExcelUtils

from Pages.Login import Login


class Test_Selenium():
    logger = LogGeneration.logGen()
    path = "../TestData//TestData.xlsx"

    @pytest.mark.sanity
    def test_Test001(self, test_setup):

        self.driver=test_setup
        self.logger.info("Testcase 1")
        element_present = EC.presence_of_element_located((By.NAME, 'username'))
        WebDriverWait(self.driver, 30).until(element_present)
        login=Login(self.driver)
        login.enterUsername(ReadConfig.getUsername())
        self.logger.info("username entered")
        login.enterPassword(ReadConfig.getPassword())
        self.logger.info("password entered")
        login.clickLogin()
        self.logger.info("clicked on login")
        if(self.driver.title!="sasi"):
            self.driver.save_screenshot("../Screenshots//"+"testsasi.png")
        self.driver.close()

    @pytest.mark.regression
    def test_Test002(self,test_setup):
        self.driver = test_setup
        self.logger.info("Testcase 2")
        element_present = EC.presence_of_element_located((By.NAME, 'username'))
        WebDriverWait(self.driver, 30).until(element_present)
        login=Login(self.driver)
        login.enterUsername(ReadConfig.getUsername())
        self.logger.info("username entered")
        login.enterPassword(ReadConfig.getPassword())
        self.logger.info("password entered")
        login.clickLogin()
        self.logger.info("clicked on login")
        self.driver.close()

    @pytest.mark.smoke
    def test_Test003(self, test_setup):
        self.rows=ExcelUtils.getRowCount(self.path,'Sheet1')
        print("Number of rows",self.rows)
        self.driver = test_setup
        self.logger.info("Testcase 2")
        element_present = EC.presence_of_element_located((By.NAME, 'username'))
        WebDriverWait(self.driver, 30).until(element_present)
        login = Login(self.driver)
        login.enterUsername(ExcelUtils.readData(self.path,'Sheet1',2,1))
        self.logger.info("username entered")
        login.enterPassword(ExcelUtils.readData(self.path,'Sheet1',2,1))
        self.logger.info("password entered")
        login.clickLogin()
        self.logger.info("clicked on login")
        self.driver.close()

    # def test_tearDownClass():
    #     driver.close()


