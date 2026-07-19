from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from config import (LOGIN_URL, TIMEOUT, USERNAME_LOGIN, PASSWORD_LOGIN,
                    MAIN_URL, CART_URL, PRODUCTS, CHECKOUT_URL)

# класс для страницы авторизации, который будет содержать методы
# для ввода логина и пароля, а также для нажатия кнопки входа;


class PageLogin:
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    BUTTON_LOGIN = (By.ID, "login-button")

    def __init__(self, driver):
        self.driver = driver
        self.url = LOGIN_URL
        self.wait = WebDriverWait(self.driver, TIMEOUT)

    def page_login_open(self):
        self.driver.get(self.url)

    def login(self):
        username_input = self.wait.until(EC.presence_of_element_located(
            self.USERNAME)
        )
        username_input.clear()
        username_input.send_keys(USERNAME_LOGIN)

        password_input = self.wait.until(EC.presence_of_element_located(
            self.PASSWORD)
        )
        password_input.clear()
        password_input.send_keys(PASSWORD_LOGIN)

        login_button = self.wait.until(EC.presence_of_element_located(
            self.BUTTON_LOGIN)
        )
        login_button.click()


# класс главной страницы магазина, который будет содержать методы
# для добавления товаров в корзину и перехода в корзину;
class PageMain:

    PRODUCTS_ELEMENT = (By.CLASS_NAME, "inventory_item_label")
    PRODUCT_NAME = (By.CLASS_NAME, "inventory_item_name")
    CART = (By.CLASS_NAME, "shopping_cart_link")

    ADD_BUTTONS = {
        "Sauce Labs Backpack": (
            By.XPATH,
            ".//button[@data-test='add-to-cart-sauce-labs-backpack']"),
        "Sauce Labs Bolt T-Shirt": (
            By.XPATH,
            ".//button[@data-test='add-to-cart-sauce-labs-bolt-t-shirt']"),
        "Sauce Labs Onesie": (
            By.XPATH, ".//button[@data-test='add-to-cart-sauce-labs-onesie']")
    }

    selected_products = PRODUCTS

    def __init__(self, driver):
        self.driver = driver
        self.url = MAIN_URL
        self.wait = WebDriverWait(self.driver, TIMEOUT)

    def page_main_open(self):
        self.driver.get(self.url)

    def products_get(self):
        return self.wait.until(EC.presence_of_all_elements_located(
            self.PRODUCTS_ELEMENT)
        )

    def add_selected_products(self):
        products = self.products_get()

        for product in products:
            product_name = product.find_element(*self.PRODUCT_NAME).text
            print(f" Найден товар: {product_name}")

            if product_name in self.selected_products:
                add_btn = self.wait.until(
                    EC.element_to_be_clickable((
                        self.ADD_BUTTONS[product_name]))
                )
                add_btn.click()

    def go_to_card(self):
        cart_element = self.wait.until(EC.element_to_be_clickable(
            self.CART)
        )
        cart_element.click()

# класс страницы корзины, который будет содержать методы для нажатия кнопки
# Checkout и проверки содержимого корзины;


class PageCart:
    SHOPPING_LIST = (By.CLASS_NAME, "shopping_cart_badge")
    BUTTON_CHECKOUT = (By.ID, "checkout")

    def __init__(self, driver):
        self.driver = driver
        self.url = CART_URL
        self.wait = WebDriverWait(self.driver, TIMEOUT)

    def shopping_list(self):
        list_in_cart = self.wait.until(EC.presence_of_element_located(
            self.SHOPPING_LIST)
        )
        assert int(list_in_cart.text) == len(
            PRODUCTS), "Не все товары добавлены"

    def checkout(self):
        btn_checkout = self.wait.until(
            EC.element_to_be_clickable(self.BUTTON_CHECKOUT)
        )
        btn_checkout.click()

# класс страницы оформления заказа, который будет содержать методы
# для заполнения формы данными (имя, фамилия, почтовый индекс)
# и проверки итоговой стоимости.


class PageShoppingForm:
    FIRST_NAME = (By.XPATH, ".//input[@id='first-name']")
    LAST_NAME = (By.XPATH, ".//input[@id='last-name']")
    ZIP_CODE = (By.XPATH, ".//input[@id='postal-code']")
    BUTTON_CONTINUE = (By.XPATH, ".//input[contains(@data-test, 'continue')]")
    TOTAL = (By.XPATH, ".//div[@data-test='total-label']")

    def __init__(self, driver):
        self.driver = driver
        self.url = CHECKOUT_URL
        self.wait = WebDriverWait(self.driver, TIMEOUT)

    def shopping_form(self, first_name: str, last_name: str, postal_code: int):
        field_first_name = self.wait.until(
            EC.presence_of_element_located(self.FIRST_NAME)
        )
        field_first_name.clear()
        field_first_name.send_keys(first_name)

        field_last_name = self.wait.until(
            EC.presence_of_element_located(self.LAST_NAME)
        )
        field_last_name.clear()
        field_last_name.send_keys(last_name)

        field_postal_code = self.wait.until(
            EC.presence_of_element_located(self.ZIP_CODE)
        )
        field_postal_code.clear()
        field_postal_code.send_keys(postal_code)

        return self

    def submit_form(self):
        btn_continue = self.wait.until(EC.presence_of_element_located(
                self.BUTTON_CONTINUE)
        )
        btn_continue.click()
        return self

    def expected_total(self):
        total_element = self.wait.until(
            EC.visibility_of_element_located(self.TOTAL)
        )
        return total_element.text
