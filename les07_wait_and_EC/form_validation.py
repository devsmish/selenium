"""Проверка валидации формы на странице
Тестируемый сайт: https://bonigarcia.dev/selenium-webdriver-java/data-types.html
Цель теста: Проверить корректную валидацию полей формы после отправки данных.
Перейти на страницу Data Types Form.
Заполнить форму следующими значениями
Нажать кнопку Submit.
Проверить, что:
● Поле Zip code подсвечено красным (ошибка валидации).
● Остальные поля подсвечены зелёным (валидный ввод)."""
"""Form:Поле: Значение
First-name: Hans
Last-name: Schmidt
Address: Berliner Straße, 55/3
E-mail: test@itch.de
Phone number: +4917623456789
Zip code: (оставить пустым)
City: Berlin
Country: Deutschland
Job-position: QA
Company: ITCH"""
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
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    yield driver
    driver.quit()

def test_form_validation(driver):
    wait = WebDriverWait(driver, 10)

    # Словарь данных для заполнения (селектор по имени : значение)
    form_data = {
        "first-name": "Hans",
        "last-name": "Schmidt",
        "address": "Berliner Straße, 55-3",
        "e-mail": "test@itch.de",
        "phone": "+4917623456789",
        "city": "Berlin",
        "country": "Deutschland",
        "job-position": "QA",
        "company": "ITCH"
    }

    # Заполняем все поля, кроме Zip code
    for name, value in form_data.items():
        field = driver.find_element(By.NAME, name)
        field.send_keys(value)

    # Нажимаем кнопку Submit
    # Используем CSS-селектор для кнопки
    submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
    submit_button.click()

    # 1. Проверяем, что поле Zip code подсвечено красным
    # На этом сайте ошибка валидации подсвечивается классом 'alert-danger'
    zip_code = wait.until(EC.visibility_of_element_located((By.ID, "zip-code")))
    assert "alert-danger" in zip_code.get_attribute("class"), "Zip code должен быть подсвечен красным"

    # 2. Проверяем, что остальные поля подсвечены зеленым ('alert-success')
    green_fields_ids = [
        "first-name", "last-name", "address", "e-mail",
        "phone", "city", "country", "job-position", "company"
    ]

    for field_id in green_fields_ids:
        element = driver.find_element(By.ID, field_id)
        assert "alert-success" in element.get_attribute("class"), f"Поле {field_id} должно быть зеленым"
