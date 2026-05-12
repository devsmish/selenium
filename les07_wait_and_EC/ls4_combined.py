import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(15)  # Устанавливаем неявное ожидание
    yield driver
    driver.quit()


def test_example(driver):
    driver.get('https://suninjuly.github.io/cats.html')

    wait = WebDriverWait(driver, 20)
    element = wait.until(EC.visibility_of_element_located((By.ID, "some_id")))

    assert element.is_displayed(), "Элемент не найден!"

