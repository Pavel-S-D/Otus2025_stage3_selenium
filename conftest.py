import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--url", default="http://localhost:8080/")


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("--browser")

    driver = None

    if browser_name == "chrome":
        options = ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        options = FirefoxOptions()
        options.add_argument("--headless")
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Firefox(options=options)

    elif browser_name == "edge":
        options = EdgeOptions()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Edge(options=options)

    else:
        raise ValueError(f"Driver for {browser_name} not supported")

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
