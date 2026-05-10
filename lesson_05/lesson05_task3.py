# Открыть браузер FireFox
# Перейти на страницу: http://the-internet.herokuapp.com/inputs.
# Ввести в поле текст 12345
# Очистить это поле (метод clear()).
# Ввести в поле текст 54321
# Закрыть браузер (метод quit())

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
driver.get('http://the-internet.herokuapp.com/inputs')

input_number = driver.find_element(
    By.CSS_SELECTOR, '[type="number"]')
input_number.send_keys('12345')

input_number.clear()

input_number.send_keys('54321')

actual_value = input_number.get_attribute('value')

print(f'В поле было введено: {actual_value}')

# Для проверки, что значение совпадает с ожидаемым
expected_value = '54321'
if actual_value == expected_value:
    print('Успех! Значение совпадает.')
else:
    print(f'Ошибка! Ожидалось {expected_value}, получено {
        actual_value}')

driver.quit()
