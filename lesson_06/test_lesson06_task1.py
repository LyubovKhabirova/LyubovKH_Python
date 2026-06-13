from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

    # 2. Найдите и нажмите на кнопку "Start"
    start_btn = driver.find_element(By.CSS_SELECTOR, "#start button")
    start_btn.click()

    # 3. Дождитесь появления текста "Hello World!"
    hello_text = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//h4[text()='Hello World!']")))

    # 4. Сделайте скриншот страницы
    driver.save_screenshot(
        "C:/Users/chu4h/LyubovKH_Python/lesson_06/scrin_page.png")

    # 5. Проверьте, что появившийся текст равен "Hello World!"
    hello_text_js = driver.execute_script(
        "return arguments[0].textContent;", hello_text)

    expected_text = "Hello World!"
    assert hello_text_js == expected_text, \
        f"Текст через JavaScript не 'Hello World!', а '{hello_text_js}'"

    print(f"Мы ожидаем текст: {hello_text_js}")

    driver.quit()
