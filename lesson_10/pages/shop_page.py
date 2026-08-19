import allure
from typing import Self
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from config import (LOGIN_URL, TIMEOUT, USERNAME_LOGIN, PASSWORD_LOGIN,
                    MAIN_URL, CART_URL, PRODUCTS, CHECKOUT_URL)


class PageLogin:
    """
    Этот класс для страницы авторизации, который будет содержать методы
    для ввода логина и пароля, а также для нажатия кнопки входа;
    """
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    BUTTON_LOGIN = (By.ID, "login-button")

    def __init__(self, driver: WebDriver):
        """
        Конструктор класса PageLogin

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.url = LOGIN_URL
        self.wait = WebDriverWait(self.driver, TIMEOUT)

    @allure.step("Открытие страницы авторизации")
    def page_login_open(self):
        self.driver.get(self.url)

    @allure.step("Авторизация пользователя")
    def login(self):
        username_input = self.wait.until(EC.presence_of_element_located(
            self.USERNAME)
        )
        with allure.step("Очистить поле ввода"):
            username_input.clear()
        with allure.step("Ввести логин пользователя"):
            username_input.send_keys(USERNAME_LOGIN)

        password_input = self.wait.until(EC.presence_of_element_located(
            self.PASSWORD)
        )
        with allure.step("Очистить поле ввода"):
            password_input.clear()
        with allure.step("Ввести пароль пользователя"):
            password_input.send_keys(PASSWORD_LOGIN)

        with allure.step("Нажать кнопку авторизации"):
            login_button = self.wait.until(EC.presence_of_element_located(
                self.BUTTON_LOGIN)
            )
            login_button.click()


class PageMain:

    """
    "Это класс главной страницы магазина, который будет содержать методы
    для добавления товаров в корзину и перехода в корзину;
    """

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

        """
        Конструктор класса PageMain

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.url = MAIN_URL
        self.wait = WebDriverWait(self.driver, TIMEOUT)

    @allure.step("Открытие главной страницы магазина")
    def page_main_open(self):
        self.driver.get(self.url)

    def products_get(self) -> list[WebElement]:
        return self.wait.until(EC.presence_of_all_elements_located(
            self.PRODUCTS_ELEMENT)
        )

    @allure.step("Добавление товаров в корзину")
    def add_selected_products(self):
        products = self.products_get()

        for product in products:
            with allure.step("Поиск товара по его названию"):
                product_name = product.find_element(*self.PRODUCT_NAME).text
                print(f" Найден товар: {product_name}")

            if product_name in self.selected_products:
                with allure.step("Добавление товара из списка в корзину"):
                    add_btn = self.wait.until(
                        EC.element_to_be_clickable((
                            self.ADD_BUTTONS[product_name]))
                    )
                    add_btn.click()

    @allure.step("Переход на страницу корзины")
    def go_to_card(self):
        cart_element = self.wait.until(EC.element_to_be_clickable(
            self.CART)
        )
        cart_element.click()


class PageCart:
    """
    "Это класс страницы корзины, который будет содержать методы для нажатия
    кнопки Checkout и проверки содержимого корзины;
    """
    SHOPPING_LIST = (By.CLASS_NAME, "shopping_cart_badge")
    BUTTON_CHECKOUT = (By.ID, "checkout")

    def __init__(self, driver):
        """
        Конструктор класса PageCard

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.url = CART_URL
        self.wait = WebDriverWait(self.driver, TIMEOUT)

    @allure.step("Получение списка товаров в корзине")
    def shopping_list(self):
        list_in_cart = self.wait.until(EC.presence_of_element_located(
            self.SHOPPING_LIST)
        )
        with allure.step("Проверка количества добавленных товаров в корзину"):
            assert int(list_in_cart.text) == len(
                PRODUCTS), "Не все товары добавлены"

    @allure.step("Переход по кнопке на страницу оформления заказа")
    def checkout(self):
        btn_checkout = self.wait.until(
            EC.element_to_be_clickable(self.BUTTON_CHECKOUT)
        )
        btn_checkout.click()


class PageShoppingForm:
    """
    Это класс страницы оформления заказа, который будет содержать методы
    для заполнения формы данными (имя, фамилия, почтовый индекс)
    и проверки итоговой стоимости.
    """
    FIRST_NAME = (By.XPATH, ".//input[@id='first-name']")
    LAST_NAME = (By.XPATH, ".//input[@id='last-name']")
    ZIP_CODE = (By.XPATH, ".//input[@id='postal-code']")
    BUTTON_CONTINUE = (By.XPATH, ".//input[contains(@data-test, 'continue')]")
    TOTAL = (By.XPATH, ".//div[@data-test='total-label']")

    def __init__(self, driver):
        """
        Конструктор класса PageShoppingForm

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.url = CHECKOUT_URL
        self.wait = WebDriverWait(self.driver, TIMEOUT)

    @allure.step("Заполнение формы оформления заказа")
    def shopping_form(
            self, first_name: str, last_name: str, postal_code: int) -> Self:
        field_first_name = self.wait.until(
            EC.presence_of_element_located(self.FIRST_NAME)
        )
        with allure.step("Очистить поле 'Имя'"):
            field_first_name.clear()
        with allure.step("Ввести значение в поле 'Имя'"):
            field_first_name.send_keys(first_name)

        field_last_name = self.wait.until(
            EC.presence_of_element_located(self.LAST_NAME)
        )
        with allure.step("Очистить поле 'Фамилия'"):
            field_last_name.clear()
        with allure.step("Ввести значение в поле 'Фамилия'"):
            field_last_name.send_keys(last_name)

        field_postal_code = self.wait.until(
            EC.presence_of_element_located(self.ZIP_CODE)
        )
        with allure.step("Очистить поле 'Почтовый индекс'"):
            field_postal_code.clear()
        with allure.step("Ввести значение в поле 'Почтовый индекс'"):
            field_postal_code.send_keys(postal_code)

        return self

    @allure.step("Отправка формы кликом по кнопке")
    def submit_form(self):
        btn_continue = self.wait.until(EC.presence_of_element_located(
                self.BUTTON_CONTINUE)
        )
        btn_continue.click()
        return self

    def order_amount(self) -> str:
        total_element = self.wait.until(
            EC.visibility_of_element_located(self.TOTAL)
        )
        return total_element.text
