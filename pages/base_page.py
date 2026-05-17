from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, driver):
        self.driver: WebDriver = driver

    def get_page_title(self) -> str:
        return self.driver.title