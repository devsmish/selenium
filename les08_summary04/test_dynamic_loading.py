import pytest, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
    yield driver
    driver.quit()


def test_text(driver):
    wait = WebDriverWait(driver, 5)
    button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#start > button")))
    button.click()
    text = wait.until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#finish > h4"), "Hello World!"))
    assert text
