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


def test_login_and_check_url(driver):
    wait = WebDriverWait(driver, 10)

    # Ждем, пока поле username не появится на странице
    # Это критически важно для OrangeHRM!
    username_field = wait.until(EC.visibility_of_element_located((By.NAME, "username")))
    username_field.send_keys("Admin")

    # Для пароля тоже лучше использовать wait, чтобы быть уверенным в готовности элемента
    password_field = wait.until(EC.visibility_of_element_located((By.NAME, "password")))
    password_field.send_keys("admin123")

    # Кнопка может быть видна, но не кликабельна (перекрыта спиннером загрузки)
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
    login_button.click()

    # Ожидаем, пока URL изменится на нужный
    wait.until(EC.url_contains("dashboard"))

    # Финальная проверка
    assert "dashboard" in driver.current_url, f"Ожидаемый URL не содержит 'dashboard': {driver.current_url}"
