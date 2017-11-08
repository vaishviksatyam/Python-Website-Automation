from selenium import webdriver
import re

driver=webdriver.Chrome()
driver.get("")
driver.execute_script("window.alart('this is an alart');")
time.sleep(4)

alart=driver.switch_to_alart()
alart.accept()