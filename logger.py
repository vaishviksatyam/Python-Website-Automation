import logging
from selenium import webdriver

LOG_FILENAME='example.log'
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)

driver=webdriver.Chrome()
logging.debug('chrome instance started')

print(driver.capabilities['version'])
logging.debug('Browser version printed')
