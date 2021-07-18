import time, math
from selenium import webdriver


driver = webdriver.Chrome("C:/chromedriver/chromedriver.exe")
link = "http://suninjuly.github.io/redirect_accept.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    driver.get(link)
    driver.find_element_by_class_name('btn').click()
    driver.switch_to.window(driver.window_handles[1])
    x = driver.find_element_by_id('input_value').text
    driver.find_element_by_id('answer').send_keys(calc(x))
    driver.find_element_by_class_name('btn').click()
finally:
    time.sleep(5)
    driver.quit()