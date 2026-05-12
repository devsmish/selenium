"""Реализовать скрипт для авторизации
http://the-internet.herokuapp.com/login
Username: tomsmith
Password: SuperSecretPassword!
Проверить, что отображаются:
● Текст “You logged into a secure area!ˮ
● Заголовок “Secure Areaˮ
● Кнопка “Logoutˮ
Нажать на кнопку Logout и убедиться, что пользователь
находится на странице авторизации."""
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

    def test_login_logout(self):
        wait = WebDriverWait(self.driver, 10)

        # Ввод имени пользователя
        username_input = wait.until(EC.visibility_of_element_located((By.ID, "username")))
        username_input.send_keys("tomsmith")

        # Ввод пароля
        password_input = self.driver.find_element(By.ID, "password")
        password_input.send_keys("SuperSecretPassword!")

        # Нажатие кнопки Login
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        # Проверка успешного входа
        success_message = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.flash.success")))
        assert "You logged into a secure area!" in success_message.text

        # Проверка заголовка
        assert self.driver.find_element(By.TAG_NAME, "h2").text == "Secure Area"

        # Проверка и нажатие Logout
        logout_button = self.driver.find_element(By.CSS_SELECTOR, "a.button.secondary.radius")
        assert logout_button.is_displayed()
        logout_button.click()

        # Проверка возврата на страницу логина
        login_page_header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h2")))
        assert login_page_header.text == "Login Page"
        assert self.driver.find_element(By.ID, "username").is_displayed()
