from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import pytest, time



@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_first_cat_card_is_displayed(driver):
    driver.get('https://suninjuly.github.io/cats.html')
    wait = WebDriverWait(driver, 5)  # Ожидание до 5 секунд
    first_cat_card = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".col-sm-4:nth-child(6)")))
    assert first_cat_card.is_displayed()