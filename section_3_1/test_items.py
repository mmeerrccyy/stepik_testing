link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_add_to_basked_button_available(browser):
    browser.get(link)
    browser.implicitly_wait(5)
    button = browser.find_elements_by_class_name('btn-add-to-basket')
    assert len(button) > 0, "Кнопка не найдена!"
