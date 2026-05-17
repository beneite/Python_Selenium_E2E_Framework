import json
from pathlib import Path

import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from pages.home_page import HomePage
from pages.login_page import LoginPage

test_data_path = Path(__file__).parent.parent / "test_data" / "login_test.json"

with open(test_data_path) as test_data_json:
    test_data = json.load(test_data_json)
    data_set_list = test_data["data"]

@pytest.mark.smoke
@pytest.mark.parametrize("data_set", data_set_list)
def test_login_success(driver_initialization, data_set):
    driver: WebDriver = driver_initialization
    #TODO: move this to a configuration or properties file
    driver.get("https://sauce-demo.myshopify.com/account/login")

    # 1. login in using username and password
    login_page_obj = LoginPage(driver)
    print("title:", login_page_obj.get_page_title())
    #TODO: add data class for fetching value
    login_page_obj.enter_customer_email(data_set["userEmail"])
    login_page_obj.enter_customer_password(data_set["userPassword"])
    login_page_obj.click_sign_in()

    # 2. adding a product to cart
    home_page_obj = HomePage(driver)
    print("title:", home_page_obj.get_page_title())
    home_page_obj.click_catalog()
    home_page_obj.click_product(data_set["productName"])
    home_page_obj.click_add_to_cart()