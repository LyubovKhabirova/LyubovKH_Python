import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import TIMEOUT, TIMEOUT_LONG


class PageCalculator:
    """
    Этот класс представляет страницу-объект "Калькулятор".
    Предоставляет методы для выполнения математических операций:
    сложение, вычитание, деление, умножение
    с целыми и дробными числами.
    """
    FIELD_DELAY = (By.ID, "delay")
    RESULT_ELEMENT = (By.CSS_SELECTOR, 'div[class="screen"]')

    def __init__(self, driver: WebDriver, url: str):
        """
        Конструктор класса PageCalculator

        :param driver: WebDriver — объект драйвера Selenium.
        :param url: str - URL страницы калькулятора.
        """
        self.driver = driver
        self.url = url

        self.wait = WebDriverWait(self.driver, TIMEOUT)

    @allure.step("Открытие страницы калькулятора")
    def page_open(self):
        """
        Открывает страницу калькулятора
        """
        self.driver.get(self.url)

    @allure.step("Установка задержки {seconds} секунд")
    def set_delay(self, seconds: int):
        """
        Устанавливает задержку для выполнения операций на калькуляторе.

        :param seconds: int - время задержки в секундах.
        """
        field = self.wait.until(
            EC.presence_of_element_located(self.FIELD_DELAY))
        field.clear()
        field.send_keys(str(seconds))

    @allure.step("Нажатие кнопок {keys}")
    def click_calculation(self, keys: list):
        """
        Нажимает на несколько кнопок калькулятора по очереди из списка.

        :param keys: list[str] - список текстов на кнопках,
        которые нужно нажать.
        """

        for key in keys:
            button = self.wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, f"//div[@class='keys']//span[text()='{key}']")
                )
            )
            button.click()

    def get_result(self, expected_result: str) -> str:
        """
        Ожидает появления ожидаемого результата на экране калькулятора.

        :param expected_result: str - ожидаемый результат
        """
        WebDriverWait(self.driver, TIMEOUT_LONG).until(
            EC.text_to_be_present_in_element(
                self.RESULT_ELEMENT, expected_result)
        )
        return self.driver.find_element(*self.RESULT_ELEMENT).text
