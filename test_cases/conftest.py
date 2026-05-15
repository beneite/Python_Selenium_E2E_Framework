import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver_initialization():
    service: Service = Service(ChromeDriverManager().install())
    driver: WebDriver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()