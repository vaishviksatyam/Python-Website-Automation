from selenium import webdriver
from selenium.webdriver.common.keys import keys
import time

driver=webdriver.Firefox()

driver.get('')

element =driver.find_element_by_id('polo')

actionchains =Actionchains(driver)
actionchains.double_click(element).perform()