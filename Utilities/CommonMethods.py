from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utilities.Logger import LogGeneration

class UtilMethods:
    logger = LogGeneration.logGen()

    def clickAnElement(self,driver,by_element,locstring):
         WebDriverWait(driver, 10).until(EC.visibility_of_element_located(by_element)).click();
         self.logger.info("clicked on\t"+locstring)

    def enterTextInAnElement(self,driver,by_element,text,locstring):
         WebDriverWait(driver, 10).until(EC.visibility_of_element_located(by_element)).send_keys(text)
         self.logger.info("Text entered\t"+text+"\ton\t" + locstring)