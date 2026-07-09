# Откройте страницу:
# https://bonigarcia.dev/selenium-webdriver-java/data-types.html
# в Edge или Safari.
# Заполните форму значениями:
# First name Иван
# Last name Петров
# Address Ленина, 55-3
# Email test@skypro.com
# Phone number +7985899998787
# Zip code *оставить пустым
# City Москва
# Country Россия
# Job position QA
# Company SkyPro
# Нажмите кнопку Submit.
# Проверьте (assert), что поле Zip code  подсвечено красным.
# Проверьте (assert), что остальные поля подсвечены зеленым.

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Edge()
    yield driver
    driver.quit()


@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 15)


def test_registration_form(driver, wait):
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    expected_fields = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro"
    }

    for field_name, value in expected_fields.items():
        field = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, f".//input[@name='{field_name}']"))
        )
        field.clear()
        field.send_keys(value)

    btn_submit = wait.until(EC.presence_of_element_located(
        (By.XPATH, ".//button[@type='submit']"))
    )

    driver.execute_script("arguments[0].click();", btn_submit)

    field_zip = wait.until(
        EC.visibility_of_element_located((By.ID, "zip-code")))

    bg_color = field_zip.value_of_css_property('background-color')
    assert bg_color == "rgba(248, 215, 218, 1)"
    print(f'Незаполненное поле окрасилось в: {bg_color}')

    field_green = [
        "first-name",
        "last-name",
        "address",
        "e-mail",
        "phone",
        "city",
        "country",
        "job-position",
        "company"]

    for field_name in field_green:
        field = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, f".//div[@id='{field_name}']"))
        )
        bg_color = field.value_of_css_property('background-color')
        assert bg_color == "rgba(209, 231, 221, 1)", \
            f"Поле '{field_name}' должно быть зеленым"

        print(f"Поле '{field_name}' окрасилось в: {bg_color}")
