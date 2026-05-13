"""Перейти на страницу. http://www.uitestingplayground.com/loaddelay
Дождаться появления кнопки "Button Appearing After Delay".
Убедиться, что кнопка действительно появилась."""
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def driver():
    # Устанавливаем ChromeDriver через WebDriverManager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("http://www.uitestingplayground.com/loaddelay") # Открываем страницу
    yield driver
    driver.quit() # Закрываем браузер после теста

def test_wait_for_button(driver):
    wait = WebDriverWait(driver, 15) # Ожидание до 15 секунд
    # Ждём, пока кнопка появится на странице
    button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[text()='Button Appearing After Delay']")))
    # Проверяем, что кнопка действительно появилась
    assert button.is_displayed(), "Кнопка не появилась!"
