import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


def pytest_addoption(parser):
    parser.addoption("--browser", default="ch")
    parser.addoption("--url", default="http://localhost:8080/")


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("--browser")

    driver = None

    if browser_name == "ch":
        driver = webdriver.Chrome()
    elif browser_name == "ff":
        driver = webdriver.Firefox()
    elif browser_name == "ed":
        driver = webdriver.Edge()
    else:
        raise ValueError(f"Driver for {browser_name} not supported")

    yield driver

    driver.close()


@pytest.fixture()
def base_url(request):
    return request.config.getoption("--url")

@pytest.fixture()
def wait(browser):
    return WebDriverWait(browser, 5, poll_frequency=1)

@pytest.fixture
def admin_creds():
    return {
        "login": "user",
        "password": "bitnami"
    }
