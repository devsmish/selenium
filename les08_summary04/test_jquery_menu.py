import pytest, time
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/jqueryui/menu#")
    yield driver
    driver.quit()


def test_item_dropdown_menu(driver):
    btn_enabled = driver.find_element(By.CSS_SELECTOR, "#ui-id-3 > a")
    btn_enabled.click()
    time.sleep(1)
    btn_downloads = driver.find_element(By.CSS_SELECTOR, "#ui-id-4 > a")
    btn_downloads.click()
    time.sleep(1)
    btn_pdf = driver.find_element(By.CSS_SELECTOR, "#ui-id-5 > a")
    btn_pdf.is_displayed()
