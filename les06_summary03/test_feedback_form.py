import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class TestITCareerHub:
    @pytest.fixture(scope="function", autouse=True)
    def setup_and_teardown(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        self.driver.get("https://itcareerhub.de/ru")
        yield
        self.driver.quit()

    def test_elements_displayed(self):
        wait = WebDriverWait(self.driver, 10)

        elements_to_check = [
            (By.CSS_SELECTOR, "img[alt='ITCareerHub']"),
            (By.LINK_TEXT, "Программы"),
            (By.LINK_TEXT, "Способы оплаты"),
            (By.LINK_TEXT, "Новости"),
            (By.LINK_TEXT, "О нас"),
            (By.LINK_TEXT, "Отзывы"),
            (By.CSS_SELECTOR, "button[lang='ru']"),
            (By.CSS_SELECTOR, "button[lang='de']")
        ]

        for locator in elements_to_check:
            assert wait.until(EC.visibility_of_element_located(locator)).is_displayed()

    def test_click_phone_icon_and_check_text(self):
        wait = WebDriverWait(self.driver, 10)

        phone_icon = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".phone-icon")))
        phone_icon.click()

        expected_text = "Если вы не дозвонились, заполните форму на сайте.Мы свяжемся с вами"

        assert wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, "body"), expected_text))
