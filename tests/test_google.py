from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def test_google_search():

    driver = webdriver.Chrome()

    driver.get("https://www.google.com/")
    driver.maximize_window()
    driver.find_element(By.ID, "APjFqb").send_keys("Hello Selenium", Keys.ENTER)
    search_result_text = driver.find_element(By.CSS_SELECTOR, "div#result-stats").text
    print(search_result_text)

    # Assertions

    assert search_result_text != " "
