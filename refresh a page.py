import time
from selenium import webdriver
from selenium.common.keys import keys

driver =webdriver.Firefox()
driver.get('')

time.sleep(3)
driver.refresh()
time.sleep(2)
driver.close()