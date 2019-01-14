from selenium import webdriver
from selenium.webdriver.common.by import By
import  time
driver=webdriver.Chrome()
driver.get("https://www.facebook.com")
value=driver.find_elements(By.CSS_SELECTOR,"[href]")
print(len(value))

#driver.close()

