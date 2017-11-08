import time
from selenium import webdriver

driver=webdriver.Chrome()
driver.get("link")
print (driver.title)
time.sleep(5)
driver.quit()