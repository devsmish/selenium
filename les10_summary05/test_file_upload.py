from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
'''Открыть страницу
Перейти по ссылке: http://suninjuly.github.io/file_input.html.
Заполнить поля формы
Ввести данные в поле "First Name".
Ввести данные в поле "Last Name".
Ввести данные в поле "Email".
Загрузить файл
Найти поле загрузки файла (input type="file").
Прикрепить файл из локальной системы с помощью send_keys().
Нажать кнопку Submit
Проверить текст в alert
Дождаться появления alert.
Проверить, что текст alert содержит "Congrats, you've passed the task!".'''

@pytest.fixture
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    driver.get("https://suninjuly.github.io/file_input.html")
    yield chrome_driver
    chrome_driver.quit()


def test_upload_file(driver):
    first_input = driver.find_element(By.CSS_SELECTOR, '[name="firstname"]')
    last_input = driver.find_element(By.CSS_SELECTOR, '[name="lastname"]')
    email_input = driver.find_element(By.CSS_SELECTOR, '[name="email"]')
    first_input.send_keys("Bogdan")
    last_input.send_keys("Puchkov")
    email_input.send_keys("bogdanicarus659@gmail.com")
    file_input = driver.find_element(By.ID, 'file')
    file_input.send_keys("C:/Users/bogda/Pictures/0786_G2uWPwMa2ys.JPG")
    submit_button = driver.find_element(By.CSS_SELECTOR, 'button')
    submit_button.click()
    sleep(5)
