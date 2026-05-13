"""Проверка загрузки изображений
Тестируемый сайт:
https://bonigarcia.dev/selenium-webdriver-java/loading-images.html
Шаги теста:
Перейдите на сайт Loading Images.
Дождитесь загрузки всех изображений.
Получите значение атрибута alt у третьего изображения.
Убедитесь, что значение атрибута alt равно "award"."""
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
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
    yield driver
    driver.quit()

attr_alt = "award"

def test_rename_button(driver):
    wait = WebDriverWait(driver, 15)
    wait.until(EC.text_to_be_present_in_element((By.ID, "text"), "Done!"))
    third_picture = wait.until(EC.visibility_of_element_located((By.ID, "award")))
    attr_value = third_picture.get_attribute("alt")
    assert attr_alt == attr_value
