import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

"""
Happy Scenario
"""
driver = webdriver.Chrome()


@pytest.fixture(autouse=True)
def set_up():
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    driver.maximize_window()


def test_alerts():
    time.sleep(2)
    alert = Alert(driver)
    driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
    assert alert.text.__contains__("Confirm")
    time.sleep(2)
    alert.accept()
    time.sleep(2)
    assert driver.find_element(By.ID, "result").text.__contains__("Ok")
