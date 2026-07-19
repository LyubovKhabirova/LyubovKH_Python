import pytest
from driver_factory import create_driver


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Выберите браузер для тестов: chrome, firefox, safari, edge"
    )
    # Например, запуск в Firefox
    # pytest tests/test_01_calc.py --browser=firefox
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Запуск в headless режиме (без графического интерфейса)"
    )


@pytest.fixture(scope="session")
def driver(request):
    browser_name = request.config.getoption("--browser")
    headless_mode = request.config.getoption("--headless")

    driver = create_driver(browser_name, headless=headless_mode)

    if not headless_mode:
        driver.maximize_window()

    yield driver
    driver.quit()
