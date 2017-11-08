from selenium import webdriver
import re

driver=webdriver.Chrome()
driver.get("")
driver.execute_script("window.alart('this is an alart');")
