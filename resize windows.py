import time
from selenium import webdriver
from selenium.common.keys import keys

driver =webdriver.Firefox()
driver.get('')

time.sleep(3)
browser.set_window_size(1024,768)
time.sleep(3)
time.sleep(3)
print(browser.get_window_size())
browser.maximum_window_size()
browser.close()