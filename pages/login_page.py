from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from pages.base_page import BasePage

class LoginPage(BasePage):

    customer_email_input = (By.XPATH, "//input[@id = 'customer_email']")
    customer_password_input = (By.XPATH, "//input[@id = 'customer_password']")
    sign_in_button = (By.XPATH, "//input[@value = 'Sign In']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def enter_customer_email(self, customer_email):
        element: WebElement = self.driver.find_element(*self.customer_email_input)
        element.clear()
        element.send_keys(customer_email)
        print("useremail:", element.get_attribute("value"))

    def enter_customer_password(self, customer_password):
        element: WebElement = self.driver.find_element(*self.customer_password_input)
        element.clear()
        element.send_keys(customer_password)

    def click_sign_in(self):
        element: WebElement = self.driver.find_element(*self.sign_in_button)
        element.click()