import pytest, time
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

def test_first_cat_card_is_displayed(driver):
    driver.get('https://the-internet.herokuapp.com/entry_ad')
    menu_1 = driver.find_element(By.CSS_SELECTOR, "#modal > div.modal > div.modal-footer > p")
    menu_1.click()