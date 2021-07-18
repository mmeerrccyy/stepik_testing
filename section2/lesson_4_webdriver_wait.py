import time, math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome("C:/chromedriver/chromedriver.exe")
link = "http://suninjuly.github.io/explicit_wait2.html"
driver.implicitly_wait(5)


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    driver.get(link)
    price = WebDriverWait(driver, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    driver.find_element_by_id('book').click()
    x = driver.find_element_by_id('input_value').text
    driver.find_element_by_id('answer').send_keys(calc(x))
    driver.find_element_by_id('solve').click()
finally:
    time.sleep(5)
    driver.quit()