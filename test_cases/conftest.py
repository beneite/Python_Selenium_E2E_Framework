import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Provide browser name")
    parser.addoption("--env", action="store", default="qa", help="Provide environment name")

@pytest.fixture(scope = "function")
def driver_initialization(request):
    browser_name = request.config.getoption("browser").lower()

    if browser_name == "chrome":
        service: Service = Service(ChromeDriverManager().install())
        driver: WebDriver = webdriver.Chrome(service=service)
    elif browser_name == "firefox":
        service: Service = Service(GeckoDriverManager().install())
        driver: WebDriver = webdriver.Firefox(service=service)
    else:
        raise ValueError(f"Browser not supported, Value passed: {browser_name}")

    driver.implicitly_wait(4)
    driver.maximize_window()
    yield driver
    driver.quit()