# Автоматизация тестирования с помощью Selenium и Python

Это репозиторий с тестами для курса "Автоматизация тестирования с помощью Selenium и Python" на [Stepik](https://stepik.org/course/575).

## Клонирование репозитория

```bash
git clone https://github.com/mmeerrccyy/stepik_testing.git
```

### После этого можете перейти в папку репозитория

```bash
cd stepik_testing
```

## Установка

Для начала установите [Python](https://www.python.org/) и Selenium WebDriver для своего браузера.

Далее создайте виртуальное окружение:
```bash
python -m venv venv
```

Активируйте виртуальное окружение:
```bash
source venv/bin/activate
```

Установите нужные пакеты из requirements.txt:

```bash
pip install -r requirements.txt
```

Поздравляю! Все готово для запуска тестов!

Деактивация виртуального окружения:

```bash
deactivate
```

## FAQ

Q: Ошибка
```
selenium.common.exceptions.WebDriverException: Message: 'chromedriver' executable needs to be in PATH. Please see https://sites.google.com/a/chromium.org/chromedriver/home
```
A: Похоже webdriver не видит драйвер для браузера Chrome. Можно заменить код (если Вы пишете авто-тесты для Chrome)
```python
driver = webdriver.Chrome()
```
на
```python
driver = webdriver.Chrome("C:/chromedriver/chromedriver.exe")
```
Вместо ```C:/chromedriver/chromedriver.exe``` укажите путь к вебдрайверу.

Либо укажите тот драйвер, которым Вы пользуетесь. Пример для Firefox:
```python
driver = webdriver.Firefox()
```
или
```python
driver = webdriver.Firefox("/путь/к/драйверу/geckodriver.exe")
```