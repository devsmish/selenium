import allure
import pytest
from les11_pom.tests.constants import *


@pytest.mark.usefixtures("setup")
@allure.epic("Purchase")
class TestPurchase:

    @allure.id("id3_many_items")
    @allure.severity("critical")
    def test_successful_purchase_of_third_item(self):
        """Тест-кейс: Успешная покупка трех товаров"""

        self.login_page.success_login(LOGIN, PASSWORD)
        for product in PRODUCTS_LIST:
            self.inventory_page.add_item_to_cart(product)
        self.inventory_page.go_to_cart()

        self.cart_page.proceed_to_checkout()

        self.checkout_step_one.enter_first_name(FIRST_NAME)
        self.checkout_step_one.enter_last_name(LAST_NAME)
        self.checkout_step_one.enter_postal_code(POSTAL_CODE)

        self.checkout_step_one.click_continue()
        self.checkout_step_two.verify_total_price("58.29")
