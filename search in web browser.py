from selenium import webdriver

browser=webdriver.Firefox()
browser.get('link')

try:
	assert 'Google' in browser.title
	print("pass")
except Exception as e:
	print('failed',format (e))
browser.close()