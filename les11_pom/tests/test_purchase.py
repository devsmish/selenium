import pytest
from les11_pom.tests.constants import *


@pytest.mark.usefixtures("setup")
class TestPurchase:

    def test_successful_purchase_of_one_item(self):
        """Тест-кейс: Успешная покупка одного товара"""

        self.login_page.success_login(LOGIN, PASSWORD)
        self.inventory_page.add_item_to_cart(PRODUCT_NAME)
        self.inventory_page.go_to_cart()
        assert "cart.html" in self.driver.current_url, "User not in trash page"

        self.cart_page.proceed_to_checkout()
        assert "checkout-step-one.html" in self.driver.current_url, "Not transition on /checkout-step-one.html"

        self.checkout_step_one.enter_first_name(FIRST_NAME)
        self.checkout_step_one.enter_last_name(LAST_NAME)
        self.checkout_step_one.enter_postal_code(POSTAL_CODE)
        self.checkout_step_one.verify_inputs_are_not_red()

        self.checkout_step_one.click_continue()
        assert "checkout-step-two.html" in self.driver.current_url, "Not transition on /checkout-step-two.html"

        self.checkout_step_two.click_finish()
        assert "checkout-complete.html" in self.driver.current_url, "Not transition on thank you page"

        self.checkout_complete.click_back_home()
        assert "inventory.html" in self.driver.current_url, "Not transition on homepage"
