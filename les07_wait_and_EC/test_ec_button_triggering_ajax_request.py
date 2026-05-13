"""Нажать на кнопку "Button Triggering AJAX Request".
Дождаться, пока текст "Data loaded with AJAX get request." появится в
элементе <p> с классом bg-success.
Проверить, что текст действительно загрузился."""
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("http://www.uitestingplayground.com/ajax") # Замените на реальный URL страницы
    yield driver
    driver.quit()

def test_ajax_request(driver):
    wait = WebDriverWait(driver, 15) # Ожидание до 15 секунд
    # Нажимаем на кнопку, которая запускает AJAX-запрос
    ajax_button = driver.find_element(By.ID, "ajaxButton")
    ajax_button.click()
    # Ожидаем, пока появится элемент с классом "bg-success" и нужным текстом
    ajax_text = wait.until(
        EC.text_to_be_present_in_element(
            (By.CLASS_NAME, "bg-success"), "Data loaded with AJAX get request."))
    # Проверяем, что текст появился
    assert ajax_text, "Текст 'Data loaded with AJAX get request.' не появился!"
