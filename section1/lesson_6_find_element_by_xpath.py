import time
from selenium import webdriver

driver = webdriver.Chrome("C:/chromedriver/chromedriver.exe")
link = "http://suninjuly.github.io/find_xpath_form"

try:
    driver.get(link)
    driver.implicitly_wait(15)
    driver.find_element_by_name("first_name").send_keys("Ivan")
    driver.find_element_by_name("last_name").send_keys("Petrov")
    driver.find_element_by_name("last_name").send_keys("Petrov")
    driver.find_element_by_class_name("city").send_keys("Smolensk")
    driver.find_element_by_id("country").send_keys("Russia")
    driver.find_element_by_xpath('//button[text()="Submit"]').click()
finally:
    time.sleep(5)
    driver.quit()
