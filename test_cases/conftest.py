from datetime import datetime
from pathlib import Path

import pytest
from pytest_html import extras
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Provide browser name")
    #TODO: need to add env as launch option, use vercel.com qa, staging website
    parser.addoption("--env", action="store", default="qa", help="Provide environment name")
    #TODO: integrate with git lab

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
    driver.delete_all_cookies()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):

    outcome = yield
    report = outcome.get_result()

    report.extras = getattr(report, "extras", [])

    #TODO: add functionality to take screenshot on function call also
    if report.when == "call" and report.failed:

        driver = item.funcargs.get(
            "driver_initialization"
        )

        if driver:

            screenshots_dir = Path(
                "reports/screenshots"
            )

            screenshots_dir.mkdir(
                parents=True,
                exist_ok=True
            )

            timestamp = datetime.now().strftime(
                "%Y%m%d_%H%M%S"
            )

            screenshot_file = (
                screenshots_dir /
                f"{item.name}_{timestamp}.png"
            )

            driver.save_screenshot(
                str(screenshot_file)
            )

            relative_path = screenshot_file.relative_to(
                Path("reports")
            )

            report.extras.append(
                extras.image(str(relative_path))
            )