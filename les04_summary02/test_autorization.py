'''Написать скрипт, который:
Переходит на https://the-internet.herokuapp.com/login
Вводит email
Вводит password

Закончить предыдущий тест:
Совершить клик на кнопку Submit
Проверить изменение в URL
Проверить наличие текста "You logged into a secure area!"'''
from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

password = 'SuperSecretPassword!'
login = 'tomsmith'
bad_login = 'wrong_login'

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://the-internet.herokuapp.com/login')
    yield driver
    driver.quit()

def processing(driver):
    password_input = driver.find_element(By.CSS_SELECTOR, '#password')
    password_input.send_keys(password)
    sleep(2)
    btn_login = driver.find_element(By.CSS_SELECTOR, '#login > button > i')
    btn_login.click()
    sleep(1)
    text = driver.find_element(By.CSS_SELECTOR, '#flash').text
    return text

def test_authorization(driver):
    login_text = 'You logged into a secure area!'
    email_input = driver.find_element(By.CSS_SELECTOR, '#username')
    email_input.send_keys(login)
    sleep(1)
    text = processing(driver)
    assert '/secure' in driver.current_url
    assert login_text in text

"""Написать новый авто-тест со следующими условиями:
Проверить неправильно введенный username"""

def test_failed_login(driver):
    wrong_text = 'Your username is invalid!'
    email_input = driver.find_element(By.CSS_SELECTOR, '#username')
    email_input.send_keys(bad_login)
    sleep(1)
    text = processing(driver)
    assert wrong_text in text
