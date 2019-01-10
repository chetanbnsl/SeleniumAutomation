from selenium import  webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://fsharp.org")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,"[class='img-responsive img-rounded']").click()
driver.back()
value=driver.find_element(By.CSS_SELECTOR,"[class='img-responsive img-rounded']").is_displayed()
print(value)
