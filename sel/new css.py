from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#use of contains function
driver=webdriver.Chrome()
driver.get("file:///C:/Users/hp/Desktop/Practise.html")
#driver.find_element(By.CSS_SELECTOR,"a[id^='lo']").click()
driver.find_element(By.XPATH,"//*[contains(text() ,'Open Window')]").click()
value=driver.find_element(By.XPATH,"//*[contains(text(),'Multiple Select Example')]").is_displayed()
print(value)
