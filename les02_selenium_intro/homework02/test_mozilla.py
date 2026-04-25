import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_payment_section_screenshot(driver):
    save_dir = os.path.join(os.getcwd(), "E:\REPO\qa\selenium\les02_selenium_intro\homework02")
    os.makedirs(save_dir, exist_ok=True)
    file_path = os.path.join(save_dir, "payment_section.png")

    driver.get("https://itcareerhub.de/ru")
    time.sleep(3)

    driver.find_element(By.LINK_TEXT, "Способы оплаты").click()
    time.sleep(3)

    payment_section = driver.find_element(
        By.CSS_SELECTOR,
        "#rec1921734713 > div:nth-child(2) > div:nth-child(1) > div:nth-child(2)"
    )
    payment_section.screenshot(file_path)
