from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get("http://localhost/login.do")
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,"[id='username']").send_keys("admin")
driver.find_element(By.CSS_SELECTOR,"[class='textField pwdfield']").send_keys("manager")
driver.find_element(By.CSS_SELECTOR,"#loginButton").click()
time.sleep(5)


print("logged in successfully:Welcome to actitime")
#driver.close()
#driver.quit()




