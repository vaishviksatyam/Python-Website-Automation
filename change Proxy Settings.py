from selenium import webdriver
import time

profile=webdriver.FirefoxProfile()
profile.set_preference('network.proxy_type',1)
profile.set_preference('network.proxy.http',"124.40.251.146")
profile.set_preference('network.proxy.http_port',3128)
profile.update_preference()

driver=webdriver.Firefox(firefox_profile=profile)
driver.get('Whatever_website')
time.sleep(3)
driver.close()