from selenium.webdriver.common.by import By
from Utilities.CommonMethods import UtilMethods

class Login():

    def __init__(self,driver):
        self.driver=driver
        global utils
        utils=UtilMethods()

        self.txt_Username_name = (By.NAME, 'username')
        self.txt_Password_name = (By.NAME, 'password')
        self.btn_Login_xpath = (By.XPATH,"//button[@type='submit']")

    def enterUsername(self,username):
        utils.enterTextInAnElement(self.driver,self.txt_Username_name,username,"username TextBox")
    def enterPassword(self,password):
        utils.enterTextInAnElement(self.driver, self.txt_Password_name,password,"password TextBox")
    def clickLogin(self):
        utils.clickAnElement(self.driver,self.btn_Login_xpath,"login button")

