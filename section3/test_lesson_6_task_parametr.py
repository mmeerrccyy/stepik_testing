import pytest
import math
import time

from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    # options = webdriver.ChromeOptions()
    # options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # browser = webdriver.Chrome(options=options)
    browser = webdriver.Firefox()
    yield browser
    browser.quit()


class TestMainPage1:
    @pytest.mark.parametrize('link', ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1",
                                      "https://stepik.org/lesson/236897/step/1",
                                      "https://stepik.org/lesson/236898/step/1", "https://stepik.org/lesson/236899/step/1",
                                      "https://stepik.org/lesson/236903/step/1",
                                      "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"])
    def test_check_answers(self, browser, link):
        answer = str(math.log(int(time.time())))
        browser.get(link)
        browser.implicitly_wait(5)
        browser.find_element_by_xpath('//textarea').send_keys(answer)
        browser.find_element_by_class_name('submit-submission').click()
        check_text = browser.find_element_by_xpath('//div[@class="attempt__message"]/div/pre').text
        assert check_text == "Correct!"
