from pages.shop_page import PageLogin, PageMain, PageCart, PageShoppingForm
import config
from faker import Faker

fake = Faker()
first_name = fake.first_name()
last_name = fake.last_name()
postal_code = fake.pyint(min_value=99, max_value=9999)


def test_shopping(driver):
    login_page = PageLogin(driver)
    login_page.page_login_open()
    login_page.login()

    main_login = PageMain(driver)
    main_login.page_main_open()
    main_login.products_get()
    main_login.add_selected_products()
    main_login.go_to_card()

    cart_page = PageCart(driver)
    cart_page.shopping_list()
    cart_page.checkout()

    form_page = PageShoppingForm(driver)
    form_page.shopping_form(first_name, last_name, postal_code)
    form_page.submit_form()
    form_page.expected_total()

    order_amount = form_page.expected_total()
    assert order_amount == "Total: $58.29"
    print(f'Итоговая сумма равна: {order_amount}')
