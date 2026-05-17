from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):

    catalog_link = (By.XPATH, "//a[text()='Catalog']")
    product_link = "//a[contains(@id, 'product')]//h3[text()='{}']"
    add_to_cart_button = (By.XPATH, "//input[@value='Add to Cart']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_catalog(self):
        self.driver.find_element(By.XPATH, "//a[text()='Catalog']").click()

    def click_product(self, product_name):
        product_xpath = self.product_link.format(product_name)
        self.driver.find_element(By.XPATH, product_xpath).click()

    def click_add_to_cart(self):
        self.driver.find_element(*self.add_to_cart_button).click()