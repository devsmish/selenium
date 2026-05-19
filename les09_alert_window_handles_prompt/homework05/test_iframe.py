'''Проверка наличия текста в iframe
Открыть страницу
Перейти по ссылке: https://bonigarcia.dev/selenium-webdriver-java/iframes.html.
Проверить наличие текста
Найти фрейм (iframe), в котором содержится искомый текст.
Переключиться в этот iframe.
Найти элемент, содержащий текст "semper posuere integer et senectus justo curabitur.".
Убедиться, что текст отображается на странице.'''
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/iframes.html")
    yield driver
    driver.quit()

def test_iframe_text(driver):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.TAG_NAME, "iframe")))
    paragraphs = driver.find_elements(By.CSS_SELECTOR, "p.lead")
    text_found = False

    for part in paragraphs:
        if "semper posuere integer et senectus justo curabitur" in part.text:
            text_found = True
            break

    assert text_found
