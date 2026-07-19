from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import TIMEOUT, TIMEOUT_LONG


class PageCalculator:
    FIELD_DELAY = (By.ID, "delay")
    RESULT_ELEMENT = (By.CSS_SELECTOR, 'div[class="screen"]')

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(self.driver, TIMEOUT)

    def page_open(self):
        self.driver.get(self.url)

    def set_delay(self, seconds: int):
        field = self.wait.until(
            EC.presence_of_element_located(self.FIELD_DELAY))
        field.clear()
        field.send_keys(str(seconds))

    def click_calculation(self, keys: list):

        for key in keys:
            button = self.wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, f"//div[@class='keys']//span[text()='{key}']")
                )
            )
            button.click()

    def get_result(self, expected_result: str):
        WebDriverWait(self.driver, TIMEOUT_LONG).until(
            EC.text_to_be_present_in_element(
                self.RESULT_ELEMENT, expected_result)
        )
        return self.driver.find_element(*self.RESULT_ELEMENT).text
