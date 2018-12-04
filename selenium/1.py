# conding:utf-8

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.implicitly_wait(10)

mouse = driver.find_element_by_link_text("设置")

ActionChains(driver).move_to_element(mouse).perform()

time.sleep(2)
driver.close()