from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutStepTwoPage:
    def __init__(self, driver):
       self.driver = driver
       self.wait = WebDriverWait(driver, 10)

    def click_finish(self):
       self.wait.until(EC.element_to_be_clickable((By.ID, "finish"))).click()

    def get_total_price(self):
        """
        Находит элемент общей стоимости, очищает текст от 'Total: $'
        и возвращает чистую строку с ценой (например, '58.29')
        """
        raw_text = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.summary_total_label'))).text
        cleaned_price = raw_text.replace("Total: $", "").strip()
        return cleaned_price

    def verify_total_price(self, expected_price):
        """Метод проверяет, что итоговая цена на странице совпадает с ожидаемой."""
        actual_price = self.get_total_price()

        assert actual_price == str(expected_price), \
            f"Ошибка! Ожидали цену '{expected_price}', но на странице отображается '{actual_price}'"
