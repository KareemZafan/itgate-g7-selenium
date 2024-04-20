import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

"""
Happy Scenario
"""
driver = webdriver.Chrome()


@pytest.fixture(autouse=True)
def set_up():
    driver.get("https://the-internet.herokuapp.com/login")
    driver.maximize_window()


def test_login_with_valid_credentials():
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    time.sleep(3)
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button.radius").click()

    time.sleep(3)

    login_text = driver.find_element(By.ID, "flash-messages").text
    time.sleep(3)
    assert login_text.__contains__("You logged into a secure area!")


list_login_data = [("tomsmith", "123409", "Your password is invalid!"),
                   ("ahmed123", "SuperSecretPassword!", "Your username is invalid!"),
                   ("ahmed123", "t1234", "Your username is invalid!"),
                   ("", "", "Your username is invalid!"),
                   ("tomsmith", "", "Your password is invalid!"),
                   (" ", "SuperSecretPassword!", "Your username is invalid!")
                   ]


@pytest.mark.parametrize("uname,passw,expected_message", list_login_data)
def test_invalid_scenarios(uname, passw, expected_message):
    driver.find_element(By.ID, "username").send_keys(uname)
    time.sleep(3)
    driver.find_element(By.ID, "password").send_keys(passw)
    driver.find_element(By.CSS_SELECTOR, "button.radius").click()

    time.sleep(3)

    login_text = driver.find_element(By.ID, "flash-messages").text
    time.sleep(3)
    assert login_text.__contains__(expected_message)
