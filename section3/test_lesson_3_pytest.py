from selenium import webdriver


def fill_form(link):
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    driver.get(link)
    driver.find_element_by_xpath(
        '//div[@class="first_block"]/div/input[contains(@class, "first")]').send_keys(
        "First name")
    driver.find_element_by_xpath(
        '//div[@class="first_block"]/div/input[contains(@class, "second")]').send_keys(
        "Last name")
    driver.find_element_by_xpath(
        '//div[@class="first_block"]/div/input[contains(@class, "third")]').send_keys(
        "email")
    driver.find_element_by_class_name("btn").click()
    return driver.find_element_by_tag_name("h1").text


def test_registration1():
    assert fill_form("http://suninjuly.github.io/registration1.html"), \
        "Congratulations! You have successfully registered!"


def test_registration2():
    assert fill_form("http://suninjuly.github.io/registration2.html"), \
            "Congratulations! You have successfully registered!"
