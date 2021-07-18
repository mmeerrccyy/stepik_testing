import time, math
from selenium import webdriver

driver = webdriver.Opera()
link = "http://suninjuly.github.io/math.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    driver.get(link)
    x = driver.find_element_by_id('input_value').text
    driver.find_element_by_id('answer').send_keys(calc(x))
    driver.find_element_by_id('robotCheckbox').click()
    driver.find_element_by_id('robotsRule').click()
    driver.find_element_by_class_name('btn').click()
finally:
    time.sleep(5)
    driver.quit()
