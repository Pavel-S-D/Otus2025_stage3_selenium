import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support.wait import WebDriverWait

#для запуска тестов на локальной машине поменять на http://localhost:8080
def pytest_addoption(parser):
    parser.addoption("--url", default="192.168.63.184:8084", help="OpenCart URL")


@pytest.fixture
def browser():
    options = ChromeOptions()

    options.set_capability("selenoid:options", {
        "enableVNC": True
    })

    driver = webdriver.Remote(
        command_executor="http://selenoid:4444/wd/hub",
        options=options
    )

    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture()
def base_url(request):
    return request.config.getoption("--url")


@pytest.fixture()
def wait(browser):
    return WebDriverWait(browser, 2, poll_frequency=1)


@pytest.fixture
def admin_creds():
    return {
        "login": "user",
        "password": "bitnami"
    }