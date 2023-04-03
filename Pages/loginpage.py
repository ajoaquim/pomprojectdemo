from selenium.webdriver.common.by import By
from Locators.locators import Locators

class LoginPage:

    def __init__(self, driver):
        self.driver = driver

        self.sigin_button_xpath = Locators.sigin_button_xpath
        self.loginUsername_textbox_id = Locators.loginUsername_textbox_id
        self.loginSignin_button_id = Locators.loginSignin_button_id
        self.loginPasswd_textbox_id = Locators.loginPasswd_textbox_id
        self.verifyPassword_button_name = Locators.verifyPassword_button_name


    def click_sigin(self):
        self.driver.find_element(By.XPATH, self.sigin_button_xpath).click()

    def enter_username(self, username):
        self.driver.find_element(By.ID, self.loginUsername_textbox_id).clear()
        self.driver.find_element(By.ID, self.loginUsername_textbox_id).send_keys(username)

    def click_login(self):
        self.driver.find_element(By.ID, self.loginSignin_button_id).click()

    def enter_passwd(self, pswd):
        self.driver.find_element(By.ID, self.loginPasswd_textbox_id).clear()
        self.driver.find_element(By.ID, self.loginPasswd_textbox_id).send_keys(pswd)

    def click_confirm_login(self):
        self.driver.find_element(By.ID, self.loginSignin_button_id).click()




