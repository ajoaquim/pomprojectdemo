from selenium.webdriver.common.by import By
from Locators.locators import Locators

class HomePage:

    def __init__(self, driver):
        self.driver = driver

        self.presentation_clickableLabel_xpath = Locators.presentation_clickableLabel_xpath
        self.logout_clickablelabel_xpath = Locators.logout_clickablelabel_xpath


    def click_label_showuser(self):
        self.driver.find_element(By.XPATH, self.presentation_clickableLabel_xpath).click()

    def click_label_logout(self):
        self.driver.find_element(By.XPATH, self.logout_clickablelabel_xpath).click()
