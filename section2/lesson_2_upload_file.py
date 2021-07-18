import time, os
from selenium import webdriver


driver = webdriver.Chrome("C:/chromedriver/chromedriver.exe")

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'files/test.txt')

link = "http://suninjuly.github.io/file_input.html"


try:
    driver.get(link)
    driver.find_element_by_name('firstname').send_keys('First name')
    driver.find_element_by_name('lastname').send_keys('Last name')
    driver.find_element_by_name('email').send_keys('Email')
    driver.find_element_by_name('file').send_keys(file_path)
    driver.find_element_by_class_name('btn').click()
finally:
    time.sleep(5)
    driver.quit()
