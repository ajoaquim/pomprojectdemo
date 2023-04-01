from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

s = Service('C:/temp/ws-utilities/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get('https://us.yahoo.com')


driver.find_element(By.XPATH,'//*[@id="ybarAccountProfile"]/a').click()
driver.find_element(By.ID, 'login-username').send_keys('ajoaquim@yahoo.com')
driver.find_element(By.ID, 'login-signin').click()

driver.find_element(By.ID, 'login-passwd').send_keys('MATR@676366')
driver.find_element(By.ID, 'login-signin').click()
driver.implicitly_wait(10)
driver.find_element(By.XPATH, '//*[@id="ybarAccountMenuOpener"]/span').click()
driver.find_element(By.XPATH, '//*[@id="profile-signout-link"]/span[2]').click()
driver.implicitly_wait(10)
driver.quit()

