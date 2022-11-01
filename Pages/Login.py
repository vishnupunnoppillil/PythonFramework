from selenium.webdriver.common.by import By


class Login():

    def __init__(self,driver):
        self.driver=driver

        self.txt_Username_name = "username"
        self.txt_Password_name = "password"
        self.btn_Login_xpath = "//button[@type='submit']"

    def enterUsername(self,username):
        self.driver.find_element(By.NAME, self.txt_Username_name).send_keys(username)
    def enterPassword(self,password):
        self.driver.find_element(By.NAME, self.txt_Password_name).send_keys(password)
    def clickLogin(self):
        self.driver.find_element(By.NAME, self.txt_Password_name).click()

