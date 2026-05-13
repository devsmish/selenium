"""Проверка изменения текста кнопки
Тестируемый сайт:
http://uitestingplayground.com/textinput
Шаги теста:
Перейдите на сайт Text Input.
Введите в поле ввода текст "ITCH".
Нажмите на синюю кнопку.
Проверьте, что текст кнопки изменился на "ITCH"."""
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.get("http://uitestingplayground.com/textinput")
    yield driver
    driver.quit()

new_btn_name = "ITCH"

def test_rename_button(driver):
    wait = WebDriverWait(driver, 5)
    input_field = wait.until(EC.visibility_of_element_located((By.ID, 'newButtonName')))
    input_field.send_keys(new_btn_name)
    btn = wait.until(EC.element_to_be_clickable((By.ID, 'updatingButton')))
    btn.click()

    assert wait.until(EC.text_to_be_present_in_element((By.ID, 'updatingButton'), new_btn_name))
