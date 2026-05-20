import pytest
from selenium import webdriver
from les11_pom.pages.inventory_page import InventoryPage
from les11_pom.pages.login_page import LoginPage
from les11_pom.pages.cart_page import CartPage
from les11_pom.pages.checkout_step_one_page import CheckoutStepOnePage
from les11_pom.pages.checkout_step_two_page import CheckoutStepTwoPage
from les11_pom.pages.checkout_complete_page import CheckoutCompletePage

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
        self.checkout_step_one_page = CheckoutStepOnePage(self.driver)
        self.checkout_step_two_page = CheckoutStepTwoPage(self.driver)
        self.checkout_complete_page = CheckoutCompletePage(self.driver)
        yield
        self.driver.quit()
