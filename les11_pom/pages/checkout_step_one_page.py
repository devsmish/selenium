from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutStepOnePage:
    FIRST_NAME_LOCATOR = (By.ID, "first-name")
    LAST_NAME_LOCATOR = (By.ID, "last-name")
    POSTAL_CODE_LOCATOR = (By.ID, "postal-code")
    CONTINUE_BUTTON_LOCATOR = (By.ID, "continue")
    RED_ERROR_COLOR = "rgb(226, 35, 26)"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)


    def enter_first_name(self, first_name):
        field = self.wait.until(EC.presence_of_element_located(self.FIRST_NAME_LOCATOR))
        field.clear()
        field.send_keys(first_name)


    def enter_last_name(self, last_name):
        field = self.wait.until(EC.presence_of_element_located(self.LAST_NAME_LOCATOR))
        field.clear()
        field.send_keys(last_name)


    def enter_postal_code(self, postal_code):
        field = self.wait.until(EC.presence_of_element_located(self.POSTAL_CODE_LOCATOR))
        field.clear()
        field.send_keys(postal_code)


    def click_continue(self):
        self.wait.until(EC.element_to_be_clickable(self.CONTINUE_BUTTON_LOCATOR)).click()


    def verify_inputs_are_not_red(self):
        """Проверяет, что ни одно из полей ввода не подсвечено красным цветом"""
        fields_to_check = {
            "First Name": self.FIRST_NAME_LOCATOR,
            "Last Name": self.LAST_NAME_LOCATOR,
            "Postal Code": self.POSTAL_CODE_LOCATOR
        }

        for field_name, locator in fields_to_check.items():
            element = self.wait.until(EC.presence_of_element_located(locator))
            current_color = element.value_of_css_property("border-bottom-color")

            assert current_color != self.RED_ERROR_COLOR, f"The <{field_name}> field is highlighted in red!"
