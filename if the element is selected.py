from selenium import webdriver
from selenium.webdriver.common.keys import keys
import time

driver=webdriver.Firefox()

driver.get('')

element=driver.find_element_by_id('btn')
print(element.is_displayed())