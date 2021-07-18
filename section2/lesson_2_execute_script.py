import time, math
from selenium import webdriver


driver = webdriver.Chrome("C:/chromedriver/chromedriver.exe")
link = "http://suninjuly.github.io/execute_script.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    driver.get(link)
    x = driver.find_element_by_id('input_value').text
    driver.find_element_by_id('answer').send_keys(calc(x))
    button = driver.find_element_by_class_name('btn')
    driver.execute_script("return arguments[0].scrollIntoView(true);", button)
    driver.find_element_by_id('robotCheckbox').click()
    driver.find_element_by_id('robotsRule').click()
    button.click()
finally:
    time.sleep(5)
    driver.quit()