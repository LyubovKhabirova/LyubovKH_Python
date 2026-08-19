import pytest
from driver_factory import create_driver


def pytest_addoption(parser):

    """
    Добавляет пользовательские аргументы командной строки для pytest.

    Позволяет выбирать браузер и
    режим запуска через консоль при выполнении тестов.

    Args:
        parser: Объект парсера pytest (тип: pytest.Parser)
        Используется для регистрации аргументов.

    Аргументы командной строки:
        --browser (str): Имя браузера (chrome, firefox, safari, edge).
                         По умолчанию: chrome.
        --headless (bool): Флаг запуска браузера без GUI.
                           По умолчанию: False.

    Пример: pytest tests/test_02_shop.py --browser=firefox --headless
    """
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Выберите браузер для тестов: chrome, firefox, safari, edge"
    )

    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Запуск в headless режиме (без графического интерфейса)"
    )


@pytest.fixture(scope="session")
def driver(request):

    """
    Фикстура для инициализации и завершения работы драйвера.
    """
    browser_name = request.config.getoption("--browser")
    headless_mode = request.config.getoption("--headless")

    driver = create_driver(browser_name, headless=headless_mode)

    if not headless_mode:
        driver.maximize_window()

    yield driver
    driver.quit()
