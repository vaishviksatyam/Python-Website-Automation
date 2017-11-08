from selenium import webdriver
from selenium.webdriver.common.keys import keys

browser=webdriver.Firefox()
browser.get("link")

elm=browser.find_element_by_link_text('about')
browser.implicitly_wait(5)
elm.click()
time.sleep(3)
broswer.back()