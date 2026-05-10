# Открыть браузер Google Chrome.
# Перейти на страницу: http://uitestingplayground.com/dynamicid.
# Кликнуть на синюю кнопку.

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
# wait = WebDriverWait(driver, 10)
driver.get("http://uitestingplayground.com/dynamicid")

# button = wait.until(EC.element_to_be_clickable((
#     By.XPATH, '//button[contains(text(), "Button with Dynamic ID")]')))
# button.click()
button = driver.find_element(
    By.XPATH, '//button[contains(text(), "Button with Dynamic ID")]')
button.send_keys(Keys.ENTER)

sleep(5)

driver.quit()
