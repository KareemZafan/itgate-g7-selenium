import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

"""
Happy Scenario
"""
driver = webdriver.Chrome()


@pytest.fixture(autouse=True)
def set_up():
    driver.get("https://demo.guru99.com/test/drag_drop.html")
    driver.maximize_window()


def test_drag_drop():
    account_locator = driver.find_element(By.ID, "credit2")
    account_place = driver.find_element(By.ID, "bank")

    sales_locator = driver.find_element(By.ID, "credit1")
    account2_locator = driver.find_element(By.ID, "loan")

    amount_locator = driver.find_element(By.ID, "amt7")
    amount2_locator = driver.find_element(By.ID, "amt8")

    amount = driver.find_element(By.ID, "fourth")
    action = ActionChains(driver)

    action.drag_and_drop(account_locator, account_place).perform()
    time.sleep(2)
    action.drag_and_drop(sales_locator, account2_locator).perform()
    time.sleep(2)
    action.drag_and_drop(amount, amount_locator).perform()
    time.sleep(2)
    action.drag_and_drop(amount, amount2_locator).perform()
    time.sleep(2)
    result = driver.find_element(By.ID, "equal").text  # Perfect!

    assert result == "Perfect!"
