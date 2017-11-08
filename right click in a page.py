from selenium import webdriver
import re

driver=webdriver.Chrome()
driver.get("")

element=driver.find_element_by_link_text('whatever')

actionChains =ActionChains(driver)

actionChains.context_click(element).perform()
