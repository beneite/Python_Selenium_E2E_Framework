from selenium.webdriver.remote.webdriver import WebDriver


def test_login_success(driver_initialization):
    driver: WebDriver = driver_initialization