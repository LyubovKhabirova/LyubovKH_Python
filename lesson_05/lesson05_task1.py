# Открыть браузер Google Chrome.
# Перейти на страницу: http://uitestingplayground.com/classattr.
# Кликнуть на синюю кнопку.

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.get("http://uitestingplayground.com/classattr")

button = wait.until(EC.element_to_be_clickable((
    By.CSS_SELECTOR, 'button.btn-primary')))
button.click()

sleep(5)

driver.quit()
