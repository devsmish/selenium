import pytest
from selenium import webdriver
from les11_api_tests_with_postman.pages.inventory_page import InventoryPage
from les11_api_tests_with_postman.pages.login_page import LoginPage
from les11_api_tests_with_postman.pages.cart_page import CartPage

@pytest.mark.usefixtures("setup")
class BaseTest:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
        # Инициализация Page Objects
        self.login_page = LoginPage(self.driver)
        self.inventory_page = InventoryPage(self.driver)
        self.cart_page = CartPage(self.driver)
        yield
        self.driver.quit()
