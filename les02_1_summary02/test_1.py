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


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://the-internet.herokuapp.com/login')
    yield driver
    driver.quit()

def test_authorization(driver):
    email_input = driver.find_element(By.CSS_SELECTOR,'#username')
    email_input.send_keys('tomsmith')
    sleep(2)
    password_input = driver.find_element(By.CSS_SELECTOR,'#password')
    password_input.send_keys('SuperSecretPassword!')
    sleep(2)
    btn_login = driver.find_element(By.CSS_SELECTOR,'#login > button > i')
    btn_login.click()
    sleep(2)
    text = driver.find_element(By.CSS_SELECTOR,'#flash').text
    assert 'https://the-internet.herokuapp.com/secure' in driver.current_url
    assert 'You logged into a secure area!' in text

'''Написать новый авто-тест со следующими условиями:
Проверить неправильно введенный username'''
def test_invalid_username(driver):
    email_input = driver.find_element(By.CSS_SELECTOR, '#username')
    email_input.send_keys('tomsmit')
    sleep(2)
    password_input = driver.find_element(By.CSS_SELECTOR, '#password')
    password_input.send_keys('SuperSecretPassword!')
    sleep(2)
    btn_login = driver.find_element(By.CSS_SELECTOR, '#login > button > i')
    btn_login.click()
    sleep(2)
    text = driver.find_element(By.CSS_SELECTOR, '#flash').text
    assert 'Your username is invalid!' in text
