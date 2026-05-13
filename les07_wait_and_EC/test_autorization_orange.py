"""Открыть сайт OrangeHRM.
Ввести "Admin" в поле Username.
Ввести "admin123" в поле Password.
Нажать кнопку Login.
Проверить, что авторизация прошла успешно."""
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
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") # Открываем страницу
    yield driver
    driver.quit() # Закрываем браузер после


def test_login_to_orangehrm(driver):
    wait = WebDriverWait(driver, 10)

    # 1. Ждем появления поля Username (вместо обычного find_element)
    username_field = wait.until(EC.visibility_of_element_located((By.NAME, "username")))
    username_field.send_keys("Admin")

    # 2. Ждем и вводим пароль
    password_field = wait.until(EC.visibility_of_element_located((By.NAME, "password")))
    password_field.send_keys("admin123")

    # 3. Кликаем кнопку
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
    login_button.click()

    # 4. Проверяем успешный вход по заголовку
    # Ждем, пока в элементе h6 появится текст "Dashboard"
    success = wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, "h6"), "Dashboard"))

    assert success, "Авторизация не удалась: заголовок 'Dashboard' не найден."

    # Дополнительно: можно проверить URL
    assert "dashboard" in driver.current_url.lower()
