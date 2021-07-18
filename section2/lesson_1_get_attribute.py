import time, math
from selenium import webdriver

driver = webdriver.Chrome("C:/chromedriver/chromedriver.exe")
link = "http://suninjuly.github.io/get_attribute.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    driver.get(link)
    res = calc(int(driver.find_element_by_id('treasure').get_attribute('valuex')))
    driver.find_element_by_id('answer').send_keys(res)
    driver.find_element_by_id('robotCheckbox').click()
    driver.find_element_by_id('robotsRule').click()
    driver.find_element_by_class_name('btn').click()
finally:
    time.sleep(5)
    driver.quit()