import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from les11_pom.pages.login_page import LoginPage
from les11_pom.pages.inventory_page import InventoryPage
from les11_pom.pages.cart_page import CartPage

from les11_pom.pages.checkout_step_one_page import CheckoutStepOnePage
from les11_pom.pages.checkout_step_two_page import CheckoutStepTwoPage
from les11_pom.pages.checkout_complete_page import CheckoutCompletePage


@pytest.fixture(scope="class")
def setup(request):
    chrome_options = Options()

    chrome_prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False  # Отключает именно это всплывающее окно
    }
    chrome_options.add_experimental_option("prefs", chrome_prefs)

    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    request.cls.driver = driver
    request.cls.login_page = LoginPage(driver)
    request.cls.inventory_page = InventoryPage(driver)
    request.cls.cart_page = CartPage(driver)

    request.cls.checkout_step_one = CheckoutStepOnePage(driver)
    request.cls.checkout_step_two = CheckoutStepTwoPage(driver)
    request.cls.checkout_complete = CheckoutCompletePage(driver)

    yield
    driver.quit()
