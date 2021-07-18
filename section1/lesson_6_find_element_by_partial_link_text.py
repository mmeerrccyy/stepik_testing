import math
import time
from selenium import webdriver

link = "http://suninjuly.github.io/find_link_text"
driver = webdriver.Chrome("C:/chromedriver/chromedriver.exe")

try:
    driver.get(link)
    driver.implicitly_wait(15)
    driver.find_element_by_link_text(str(math.ceil(math.pow(math.pi, math.e) * 10000))).click()
    driver.implicitly_wait(15)
    driver.find_element_by_name("first_name").send_keys("Ivan")
    driver.find_element_by_name("last_name").send_keys("Petrov")
    driver.find_element_by_name("last_name").send_keys("Petrov")
    driver.find_element_by_class_name("city").send_keys("Smolensk")
    driver.find_element_by_id("country").send_keys("Russia")
    driver.find_element_by_class_name("btn").click()
finally:
    time.sleep(30)
    driver.quit()
