from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get("http://www.qspiders.com/")
time.sleep(2)
value=driver.find_element(By.CSS_SELECTOR,"[src='http://www.qspiders.com/sites/all/themes/bootstrap/logo.png']").is_displayed()
print(value)
time.sleep(10)
driver.find_element(By.CSS_SELECTOR,"[class='btn btn-default']").click()
value=driver.find_element(By.CSS_SELECTOR,"[src='http://www.qspiders.com/sites/all/themes/bootstrap/logo.png']").is_displayed()
print(value)