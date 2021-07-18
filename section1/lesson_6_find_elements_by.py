import time
from selenium import webdriver

driver = webdriver.Chrome("C:/chromedriver/chromedriver.exe")
link = "http://suninjuly.github.io/huge_form.html"

try:
    driver.get(link)
    fields = driver.find_elements_by_xpath('//input')
    for field in fields:
        field.send_keys("Text")
    driver.find_element_by_class_name("btn").click()
finally:
    time.sleep(30)
    driver.quit()