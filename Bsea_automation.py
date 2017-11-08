import time
from selenium import webdriver
import xlrd
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



book = xlrd.open_workbook("Links.xls")
sheet= book.sheet_by_index(0)
link = sheet.cell(1,0).value
print (link)
driver=webdriver.Chrome()
driver.get(link)

RMI=WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div/div[3]/div/div/div/div[1]/div[1]/div/div/div/p[2]/a")))
RMI.click()
driver.switch_to_window(driver.window_handles[1])
Submit = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div[3]/div/div/div[1]/div/div[3]/div/form/div[20]/button[1]")))

co=driver.find_element_by_name('co')
co.send_keys('company')
co.send_keys(Keys.TAB)

contact=driver.find_element_by_name('contact')
contact.send_keys('contact')
contact.send_keys(Keys.TAB)

email=driver.find_element_by_name('email')
email.send_keys('a@b.c')
email.send_keys(Keys.TAB)

phone=driver.find_element_by_name('phone')
phone.send_keys('123456789')
phone.send_keys(Keys.TAB)

addr1=driver.find_element_by_name('addr1')
addr1.send_keys('address')
addr1.send_keys(Keys.TAB)

city=driver.find_element_by_name('city')
city.send_keys('city')
city.send_keys(Keys.TAB)

state=driver.find_element_by_name('st')
state.send_keys('state')
state.send_keys(Keys.TAB)

post=driver.find_element_by_name('post')
post.send_keys('12345')

state.send_keys(Keys.TAB)
state.send_keys(Keys.TAB)
state.send_keys(Keys.TAB)
state.send_keys(Keys.TAB)
state.send_keys(Keys.TAB)
state.send_keys(Keys.TAB)
state.send_keys(Keys.TAB)
state.send_keys(Keys.TAB)
state.send_keys(Keys.TAB)
state.send_keys(Keys.TAB)

submit=driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div[1]/div/div[3]/div/form/div[20]/button[1]')
Submit.click()
print (" got till here")
time.sleep(10)
driver.quit()
