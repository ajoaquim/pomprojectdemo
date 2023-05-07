import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

#set chromodriver.exe path
driver = webdriver.Chrome(executable_path="C:/Users/ajoaquim/Devops/chromedriver")
driver.implicitly_wait(0.5)
driver.implicitly_wait(0.5)
#launch URL
driver.get("C:/Users/ajoaquim/PycharmProjects/pomprojectdemo/Tests/tempo.html")



#object of ActionChains
a = ActionChains(driver)
#identify element
m = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/button')
#hover over element
a.move_to_element(m).perform()
#identify sub menu element
n = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/a[3]')

# hover over element and click
time.sleep(5)
a.move_to_element(n).click().perform()

print("Page title: " + driver.title)
#close browser
driver.close()