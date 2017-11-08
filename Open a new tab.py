from selenium import webdriver
from selenium.webdriver.common.keys import keys
import time

driver=webdriver.Firefox()

driver.get('')

elm=driver.find_element_by_tag_name('body').send_keys(keys.CONTROL +'t')
