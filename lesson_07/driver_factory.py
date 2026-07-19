from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.safari.options import Options as SafariOptions



def create_driver(browser="chrome", headless=False):
    if browser == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless")
            return webdriver.Chrome(options=options)

        elif browser == "firefox":
            options = FirefoxOptions()
            if headless:
                options.add_argument("--headless")
            return webdriver.Firefox(options=options)

    elif browser == "safari":
        # Safari не поддерживает headless режим через аргументы
        if headless:
            print("Предупреждение: Safari не поддерживает headless режим")
            options = SafariOptions()
        return webdriver.Safari(options=options)

    elif browser == "edge":
        options = EdgeOptions()
        if headless:
            options.add_argument("--headless")
        return webdriver.Edge(options=options)
    else:
        raise ValueError(f"Браузер {browser} не поддерживается")
