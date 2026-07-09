import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 15)


def test_purchase(driver, wait):
    driver.get(
        "https://www.saucedemo.com/")

    username_input = wait.until(EC.presence_of_element_located(
        (By.ID, "user-name")
    ))
    username_input.clear()
    username_input.send_keys("standard_user")

    password_input = wait.until(EC.presence_of_element_located(
        (By.ID, "password")
    ))
    password_input.clear()
    password_input.send_keys("secret_sauce")

    login_button = wait.until(EC.presence_of_element_located(
        (By.ID, "login-button")))
    login_button.click()

    products_locators = {
        "Sauce Labs Backpack": "add-to-cart-sauce-labs-backpack",
        "Sauce Labs Bolt T-Shirt": "add-to-cart-sauce-labs-bolt-t-shirt",
        "Sauce Labs Onesie": "add-to-cart-sauce-labs-onesie"
    }

    selected_products = ["Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt",
                         "Sauce Labs Onesie"]

    products = wait.until(EC.presence_of_all_elements_located(
        (By.CLASS_NAME, "inventory_item_label")))

    for product in products:
        name_element = product.find_element(By.CLASS_NAME,
                                            "inventory_item_name")
        product_name = name_element.text
        print(f" Найден товар: {product_name}")

        if product_name in selected_products:
            locator_part = products_locators[product_name]

            add_btn = wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, f".//button[contains(@data-test, \
                    '{locator_part}')]"))
            )
            add_btn.click()

    basket_shop = wait.until(EC.element_to_be_clickable(
        (By.CLASS_NAME, "shopping_cart_link"))
    )
    basket_shop.click()

    cart_badge = wait.until(EC.presence_of_element_located(
        (By.CLASS_NAME, "shopping_cart_badge")))
    assert int(cart_badge.text) == len(
        selected_products), "Не все товары добавлены"

    btn_checkout = wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
    btn_checkout.click()

    field_first_name = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, ".//input[@id='first-name']")
        )
    )
    field_first_name.clear()
    field_first_name.send_keys("Имя")

    field_last_name = wait.until(
        EC.presence_of_element_located((By.XPATH, ".//input[@id='last-name']"))
    )
    field_last_name.clear()
    field_last_name.send_keys("Фамилия")

    field_postal_code = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, ".//input[@id='postal-code']")
        )
    )

    field_postal_code.clear()
    field_postal_code.send_keys("123456")

    btn_continue = wait.until(EC.presence_of_element_located(
            (By.XPATH, ".//input[contains(@data-test, 'continue')]")
    ))
    btn_continue.click()

    total = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, ".//div[@data-test='total-label']")))

    assert total.text == "Total: $58.29"
    print(f'Итоговая сумма равна: {total.text}')
