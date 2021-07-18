import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome("C:/chromedriver/chromedriver.exe")
link = "http://suninjuly.github.io/selects1.html"

try:
    driver.get(link)
    num1 = int(driver.find_element_by_id("num1").text)
    num2 = int(driver.find_element_by_id("num2").text)
    Select(driver.find_element_by_tag_name('select')).select_by_value(str(num1+num2))
    driver.find_element_by_class_name("btn").click()
finally:
    time.sleep(5)
    driver.quit()