from pages.calc_page import PageCalculator
import config
import allure
# Запускать в headless режиме: pytest tests/test_01_calc.py --headless

"""
Тест проверяет работу калькулятора с задержкой
"""


@allure.title("Тестирование калькулятора")
@allure.description("Операция сложения при задержке '45'")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_calculator(driver):
    """
    Тест проверяет корректность работу калькулятора с задержкой времени.
    :param driver: WebDriver — объект драйвера, переданный фикстурой.
    """

    calc_page = PageCalculator(driver, config.CALC_URL)

    # Открыть страницу калькулятора.
    calc_page.page_open()

    # Ввести значение 45 в поле задержки (локатор #delay).
    calc_page.set_delay(45)

    # Нажать кнопки: 7, +, 8, =.
    calc_page.click_calculation(["7", "+", "8", "="])

    # Проверить (assert), что в окне отобразится результат 15 через 45 секунд.
    with allure.step("Ожидание результата '15"):
        calc_page.get_result("15")
    with allure.step("Получение результата '15"):
        result = calc_page.get_result("15")
    with allure.step("Проверка, что результат соответствует ожидаемому"):
        assert result == "15", f"Ожидалось '15', а получено '{result}'"
