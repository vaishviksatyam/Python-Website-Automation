from selenium import webdriver

browser=webdriver.Firefox()
browser.get('link')
body=driver.find_element_by_tag_name('body').send_keys(Keys.Control+'t')
driver.get('secondlink')
time.sleep(3)

driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL+Keys.Page_UP)
Time.sleep(2)

driver.find_element_by_tag_name(body).send_keys(Keys.CONTROL+'w')
