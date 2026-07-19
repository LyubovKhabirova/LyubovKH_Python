from pages.calc_page import PageCalculator
import config


def test_calculator(driver):
    calc_page = PageCalculator(driver, config.CALC_URL)

    # Открыть страницу калькулятора.
    calc_page.page_open()

    # Ввести значение 45 в поле задержки (локатор #delay).
    calc_page.set_delay(45)

    # Нажать кнопки: 7, +, 8, =.
    calc_page.click_calculation(["7", "+", "8", "="])

    # Проверить (assert), что в окне отобразится результат 15 через 45 секунд.
    calc_page.get_result("15")
    result = calc_page.get_result("15")
    assert result == "15"
