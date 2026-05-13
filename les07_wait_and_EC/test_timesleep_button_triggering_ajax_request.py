import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("http://www.uitestingplayground.com/ajax") # Замените на реальный URL
    yield driver
    driver.quit()

def test_ajax_request_sleep(driver):
    # Нажимаем на кнопку AJAX-запроса
    ajax_button = driver.find_element(By.ID, "ajaxButton")
    ajax_button.click()
    # Жёсткое ожидание 15 секунд (плохая практика)
    time.sleep(15)
    # Находим элемент после ожидания
    ajax_text_element = driver.find_element(By.CLASS_NAME, "bg-success")

    # Проверяем, что текст внутри элемента соответствует ожидаемому
    assert "Data loaded with AJAX get request." in ajax_text_element.text, "Текст не загрузился!"
