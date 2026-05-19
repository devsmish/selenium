import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/windows")
    yield driver
    driver.quit()

def test_windows(driver):
    button = driver.find_element(By.CSS_SELECTOR, "#content a")
    button.click()
    sleep(2)
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    text_element = driver.find_element(By.CSS_SELECTOR, 'h3')
    assert text_element.text == 'New Window'
