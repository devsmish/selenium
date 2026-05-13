import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
     driver = webdriver.Chrome()
     driver.implicitly_wait(15) # Глобальное неявное ожидание до 15 секунд
     driver.get("http://www.uitestingplayground.com/ajax") # Замените на реальный URL
     yield driver
     driver.quit()

def test_ajax_request_implicit(driver):
     # Нажимаем на кнопку AJAX-запроса
     ajax_button = driver.find_element(By.ID, "ajaxButton")
     ajax_button.click()
     # Ищем появившийся элемент (Selenium будет ждать до 15 секунд)
     ajax_text_element = driver.find_element(By.CLASS_NAME, "bg-success")

     # Проверяем, что текст внутри элемента соответствует ожидаемому
     assert "Data loaded with AJAX get request." in ajax_text_element.text, "Текст не загрузился!"
