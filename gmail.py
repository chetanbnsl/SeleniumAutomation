from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get(url="https://mail.google.com/mail/u/0/#inbox")
driver.find_element(By.CSS_SELECTOR,"#identifierId").click()
driver.find_element(By.CSS_SELECTOR,"#identifierId").send_keys("chetanbnsl@gmail.com")
driver.find_element(By.CSS_SELECTOR,"#identifierNext").click()
driver.find_element(By.CSS_SELECTOR,"[class='whsOnd zHQkBf']").click()
driver.find_element(By.CSS_SELECTOR,"[class='whsOnd zHQkBf']").send_keys("Jaishreeram@123")


