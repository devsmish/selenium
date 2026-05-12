"""Для http://the-internet.herokuapp.com/login
Реализовать отдельными тестами проверку авторизации
с невалидными данными
Your username is invalid! """
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class TestLoginLogout:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()

        self.driver.get("http://the-internet.herokuapp.com/login")
        yield
        self.driver.quit()

    def test_invalid_username(self):
        # Ввод неверного имени пользователя
        username_input = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID, "username")))
        username_input.send_keys("wronguser")

        # Ввод пароля
        password_input = self.driver.find_element(By.ID,"password")
        password_input.send_keys("SuperSecretPassword!")

        # Нажатие кнопки Login
        login_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login_button.click()

        # Проверка сообщения об ошибке
        error_message = WebDriverWait(self.driver,
                                10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.flash.error")))
        assert "Your username is invalid!" in error_message.text

    def test_invalid_password(self):

        # Ввод имени пользователя
        username_input = WebDriverWait(self.driver,
                                   10).until(EC.presence_of_element_located((By.ID, "username")))
        username_input.send_keys("tomsmith")

        # Ввод неверного пароля
        password_input = self.driver.find_element(By.ID,"password")
        password_input.send_keys("WrongPassword!")

        # Нажатие кнопки Login
        login_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login_button.click()

        # Проверка сообщения об ошибке
        error_message = WebDriverWait(self.driver,
                                10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.flash.error")))
        assert "Your password is invalid!" in error_message.text

    def test_invalid_username_and_password(self):

        # Ввод неверного имени пользователя
        username_input = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID, "username")))
        username_input.send_keys("wronguser")

        # Ввод неверного пароля
        password_input = self.driver.find_element(By.ID,"password")
        password_input.send_keys("WrongPassword!")

        # Нажатие кнопки Login
        login_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login_button.click()

        # Проверка сообщения об ошибке
        error_message = WebDriverWait(self.driver,
                                10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.flash.error")))
        assert "Your username is invalid!" in error_message.text
