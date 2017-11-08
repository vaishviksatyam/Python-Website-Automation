from selenium import webdriver
import time

driver=webdriver.Firefox()
driver.get('link')
element=driver.find_element_by_css_selector('body')
time.sleep(3)
element.send_keys('\uE035')