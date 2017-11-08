from selenium import webdriver

driver=webdriver.Firefox()
driver.get("link")

try:
	driver.find_element_by_id('id')
	print("test pass")
except Exception as e:
	print("exception found",Format(e))
	
driver.close()