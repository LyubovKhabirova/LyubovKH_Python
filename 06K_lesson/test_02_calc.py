# Откройте страницу:
# https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html
# в Google Chrome.
# В поле ввода по локатору # #delay  введите значение 45.
# Нажмите на кнопки:
# 7
# +
# 8
# =
# Проверьте (assert), что в окне отобразится результат 15  через 45 секунд.

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 15)


def test_purchase(driver, wait):
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    field = wait.until(EC.presence_of_element_located((By.ID, "delay")))
    field.clear()
    field.send_keys("45")

    calculation = ["7", "+", "8", "="]

    for key in calculation:
        button = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//div[@class='keys']//span[text()='{key}']"))
        )
        button.click()

    result = WebDriverWait(driver, 45).until(
        EC.visibility_of_element_located((By.XPATH, ".//div[text()='15']")))

    print(f'Результат вычислений равен: {result.text}')
