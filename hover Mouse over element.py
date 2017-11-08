from selenium import webdriver
import re

driver=webdriver.Chrome()
driver.get("")

element=driver.find_element_by_link_text('whatever')

hover=Actionchains(driver).move_to_element(element)
hover.perform()

