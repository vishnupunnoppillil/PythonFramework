import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from TestCases.conftest import test_setup
from Utilities.readProperties import ReadConfig
from Utilities.Logger import LogGeneration
from Utilities import ExcelUtils

from Pages.Login import Login


class Test_Selenium():
    logger = LogGeneration.logGen()
    path = "../TestData//TestData.xlsx"
    @pytest.mark.sanity
    def test_ToVerifyLoginThroughConfigFile(self, test_setup):

        self.driver=test_setup
        self.logger.info("Testcase 1")
        login=Login(self.driver)
        login.enterUsername(ReadConfig.getUsername())
        login.enterPassword(ReadConfig.getPassword())
        login.clickLogin()
        if(self.driver.title!="sasi"):
            self.driver.save_screenshot("../Screenshots//"+"testsasi.png")

    @pytest.mark.regression
    def test_ToVerifyLoginThroughHardCoding(self,test_setup):
        self.driver = test_setup
        self.logger.info("Testcase 2")
        login=Login(self.driver)
        login.enterUsername("Admin")
        login.enterPassword("admin123")
        login.clickLogin()

    @pytest.mark.smoke
    def test_ToVerifyLoginThroughExcelSheet(self, test_setup):
        self.rows=ExcelUtils.getRowCount(self.path,'Sheet1')
        self.driver = test_setup
        self.logger.info("Testcase 3")
        login = Login(self.driver)
        login.enterUsername(ExcelUtils.readData(self.path,'Sheet1',2,1))
        login.enterPassword(ExcelUtils.readData(self.path,'Sheet1',2,1))
        login.clickLogin()

