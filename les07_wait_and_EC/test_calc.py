"""1. Откройте страницу Slow Calculator.
2. В поле ввода по локатору #delay введите значение 45.
3. Нажмите на кнопки (в указанном порядке):
● 7
● +
● 8
● =
4. Проверьте (assert), что в окне отображается результат 15 через 45 секунд."""
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
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    yield driver
    driver.quit()

def test_slow_calculator(driver):
    wait = WebDriverWait(driver, 50) # Ожидание результата
    # Вводим задержку 45 секунд в поле #delay
    delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay_input.clear()
    delay_input.send_keys("45")
    # Нажимаем кнопки: 7, +, 8, =
    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()
    # Ждём появления результата "15" через 45 секунд
    result_element = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))
    # Проверяем, что результат действительно 15
    assert result_element, "Ожидаемый результат '15' не отобразился!"
    