import json
import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from pageObjectts.checkout_confirmation import Checkout_Confirmation
from pageObjectts.login import LoginPage
from pageObjectts.shop import ShopPage
test_data_path = '../data/test_e2eTestFramework.json'
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

@pytest.mark.smoke
@pytest.mark.parametrize("test_list_item", test_list)
def test_e2e(browserInstance, test_list_item):
    driver = browserInstance
    loginPage = LoginPage(driver)
    print(loginPage.getTitle())
    shopPage = loginPage.login(test_list_item["userEmail"], test_list_item["userPassword"])
    shopPage.add_product_to_cart(test_list_item["productName"])
    print(shopPage.getTitle())
    checkout_confirmation = shopPage.go_to_cart()
    checkout_confirmation.checkout()
    checkout_confirmation.enter_delivery_address("Ind")
    checkout_confirmation.validate_order()
    print(checkout_confirmation.getTitle())





