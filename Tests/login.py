from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time
import sys
import os
from Pages.homepage import HomePage
from Pages.loginpage import LoginPage
import HtmlTestRunner

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='C:/temp/ws-utilities/chromedriver.exe')
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    def test_login_valid(self):
        driver = self.driver
        driver.get('https://us.yahoo.com')

        login = LoginPage(driver)
        login.click_sigin()
        login.enter_username("ajoaquim@yahoo.com")
        login.click_login()
        login.enter_passwd("MATR@676366")
        login.click_confirm_login()

        home = HomePage(driver)
        home.click_label_showuser()
        home.click_label_logout()

        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print('Test Completed!!')


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/temp/ws-pycharm/POMProjectDemo/Reports'))



