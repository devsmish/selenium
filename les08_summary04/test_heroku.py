import pytest, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/entry_ad")
    yield driver
    driver.quit()


def test_close_modal(driver):
    wait = WebDriverWait(driver, 5)
    btn_close = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div.modal-footer > p"))
    )
    btn_close.click()
    time.sleep(5)


def test_item_dropdown_menu(driver):
    btn_enabled = driver.find_element(By.CSS_SELECTOR, "#ui-id-3 > a")
    btn_enabled.click()
    time.sleep(1)
    btn_downloads = driver.find_element(By.CSS_SELECTOR, "#ui-id-4 > a")
    btn_downloads.click()
    time.sleep(1)
    btn_pdf = driver.find_element(By.CSS_SELECTOR, "#ui-id-5 > a")
    btn_pdf.is_displayed()
