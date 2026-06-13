from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


def test_session_storage_auth():

    driver = webdriver.Chrome()
    WebDriverWait(driver, 10)
    driver.get("https://gitflic.ru/")

    driver.add_cookie({
        "name": "SESSION",
        "value": "NmZlNzg0NzUtZmMyZC00YmJhLWFhNzUtMjczYTVhZjY5Njdh",
        "domain": "gitflic.ru",
    })

    driver.add_cookie({
        "name": "cookiesAccepted",
        "value": "true",
        "domain": "gitflic.ru"
    })

    driver.refresh()

    driver.get("https://gitflic.ru/user/tst345sky")
    saved_url_1 = driver.current_url
    print(f"Сохранённый URL user_1: {saved_url_1}")

    driver.delete_cookie("SESSION")

    driver.add_cookie({
        "name": "SESSION",
        "value": "NDk0MTc4YzktYzNmMi00NjcwLWI4NjMtNDY1Y2FlNDQ4MTdi",
        "domain": "gitflic.ru",
    })

    driver.add_cookie({
        "name": "cookiesAccepted",
        "value": "true",
        "domain": "gitflic.ru"
    })

    driver.refresh()

    driver.get("https://gitflic.ru/user/test12_06")
    saved_url_2 = driver.current_url
    print(f"Сохранённый URL user_2: {saved_url_2}")

    assert saved_url_1 != saved_url_2

    driver.quit()
