import allure
from pages.shop_page import PageLogin, PageMain, PageCart, PageShoppingForm
from faker import Faker

fake = Faker()
first_name = fake.first_name()
last_name = fake.last_name()
postal_code = fake.pyint(min_value=99, max_value=9999)

# Запускать в firefox: pytest tests/test_02_shop.py -v --browser=firefox
# Запускать в headless режиме:
# pytest tests/test_02_shop.py --browser=firefox --headless


@allure.title("Покупка в интернет-магазине")
@allure.description("Чтобы купить товар пользователь должен авторизоваться,"
                    "положить товары в корзину, заполнить форму заказа")
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_shopping(driver):
    """
    Тест проверяет пользоватьский путь покупателя интернет-магазина до момента
    оплаты товара. В корзине длжны отображаться выбранные товары, итоговая
    стоимость заказа должна соответствовать сумме товаров в корзине и налога.

    :param driver: WebDriver — объект драйвера, переданный фикстурой.
    """
    login_page = PageLogin(driver)
    login_page.page_login_open()
    login_page.login()

    main_login = PageMain(driver)
    main_login.page_main_open()
    with allure.step("Получение списка товаров"):
        main_login.products_get()
    main_login.add_selected_products()
    main_login.go_to_card()

    cart_page = PageCart(driver)
    cart_page.shopping_list()
    cart_page.checkout()

    form_page = PageShoppingForm(driver)
    form_page.shopping_form(first_name, last_name, postal_code)
    form_page.submit_form()
    with allure.step("Получение стоимости заказа"):
        form_page.order_amount()

    get_order_amount = form_page.order_amount()
    expected_total = "Total: $58.29"
    with allure.step(f"Сравнение ожидаемой суммы заказа {expected_total}"
                     f"с фактической суммой заказа {get_order_amount}"):
        assert get_order_amount == expected_total
        allure.attach(
            f"Сумма заказа: {get_order_amount}",
            name="Результат проверки суммы",
            attachment_type=allure.attachment_type.TEXT
        )
