from selenium import webdriver
import re

driver=webdriver.Chrome()
driver.get("")
driver.execute_script("document.body.style_zoom='150%'")
