# Открыть браузер FireFox.
# Перейти на страницу http://the-internet.herokuapp.com/login.
# В поле username ввести значение tomsmith.
# В поле password ввести значение SuperSecretPassword!.
# Нажать кнопку Login.
# Вывести текст с зеленой плашки в консоль.
# Закрыть браузер (метод quit()).

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
driver.get('http://the-internet.herokuapp.com/login')

field_username = driver.find_element(
    By.CSS_SELECTOR, '#username')
field_username.send_keys('tomsmith')

field_password = driver.find_element(
    By.CSS_SELECTOR, '#password')
field_password.send_keys('SuperSecretPassword!')

button_login = driver.find_element(
    By.CSS_SELECTOR, 'button[type="submit"]')
button_login.click()

message = driver.find_element(
    By.CSS_SELECTOR, '#flash').text.replace('×', '').strip()
# .replace('×', '') строка.replace(что_меняем, на_что_меняем)
# .strip() обрезаем пробелы и переносы строк
# или .split('\n') — разбивает текст по символу переноса строки
# на части, а [0] — берёт первую часть (до переноса)
# или text).strip() даляет ВСЁ, начиная с первого встреченного символа

print(f'Получено сообщение: {message}')

driver.quit()
