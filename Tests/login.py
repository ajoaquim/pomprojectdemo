from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import unittest
import time


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        s = Service('C:/temp/ws-utilities/chromedriver.exe')
        cls.driver = webdriver.Chrome(service=s)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    def test_login_valid(self):
        self.driver.get('https://us.yahoo.com')
        self.driver.find_element(By.XPATH,'//*[@id="ybarAccountProfile"]/a').click()
        self.driver.find_element(By.ID, 'login-username').send_keys('ajoaquim@yahoo.com')
        self.driver.find_element(By.ID, 'login-signin').click()
        self.driver.find_element(By.ID, 'login-passwd').send_keys('MATR@676366')
        self.driver.find_element(By.ID, 'login-signin').click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, '//*[@id="ybarAccountMenuOpener"]/span').click()
        self.driver.find_element(By.XPATH, '//*[@id="profile-signout-link"]/span[2]').click()
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print('Test Completed!!')


if __name__ == '__main__':
        unittest.main()



