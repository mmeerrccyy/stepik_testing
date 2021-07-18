import time
from selenium import webdriver

driver = webdriver.Chrome("C:/chromedriver/chromedriver.exe")  # !!!Возможно здесь нужно стереть!!!
link = "http://suninjuly.github.io/registration2.html"

try:
    driver.get(link)
    # First name* field
    driver.find_element_by_xpath('//div[@class="first_block"]/div/input[contains(@class, "first")]').send_keys(
        "First name")
    # Last name* field
    driver.find_element_by_xpath('//div[@class="first_block"]/div/input[contains(@class, "second")]').send_keys(
        "Last name")
    # Email* field
    driver.find_element_by_xpath('//div[@class="first_block"]/div/input[contains(@class, "third")]').send_keys(
        "email")
    time.sleep(1)
    driver.find_element_by_class_name("btn").click()
    time.sleep(1)
    assert "Congratulations! You have successfully registered!" == driver.find_element_by_tag_name("h1").text
finally:
    time.sleep(30)
    driver.quit()
