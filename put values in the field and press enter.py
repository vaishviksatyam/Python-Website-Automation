import time
from selenium import webdriver
from selenium.webdriver.common.keys import keys

browser=webdriver.Firefox()
browser.get("link")

search=browser.find_element_by_id('')
search.send_keys('anything you want to put')
searc.send_keys(keys.RETURN) #TO PRESS ENTER
time.sleep(5)
search.clear()
time.sleep()
broser.close()