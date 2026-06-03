import allure
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import pytest

@pytest.fixture
def driver():
    # service = Service("/Users/romansurkov/Documents/chromedriver-mac-arm64/chromedriver")
    # options = Options()
    # driver = webdriver.Chrome(service=service, options=options)
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/login")
    yield driver
    driver.quit()

def test_correct_data(driver):
    # driver.get("https://the-internet.herokuapp.com/login")
    header_text = driver.find_element(By.TAG_NAME, "h4")
    print(header_text.text)
    username_input = driver.find_element(By.ID, "username")
    username_input.click()
    username_input.send_keys("tomsmith")
    password_input = driver.find_element(By.ID, "password")




    # element = driver.find_element(By.CSS_SELECTOR, ".col-sm-4:nth-child(6) small")
    # assert element.text == '9 mins'








    password_input.click()
    password_input.send_keys("SuperSecretPassword!")
    submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()
    sleep(0.5)
    assert "secure" in driver.current_url
    message = driver.find_element(By.ID, "flash")
    assert "You logged into a secure area!" in message.text

def test_wrong_username(driver):
    submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()
    sleep(0.5)

    assert "/login" in driver.current_url
    allure.attach("Лог выполнения теста", name="Execution log", attachment_type=allure.attachment_type.TEXT)

    try:
        # Attempt to find the flash message element
        message = driver.find_element(By.ID, "2flash")
    except NoSuchElementException:
        # Dynamic screenshot: take it directly from the driver if the element is missing
        screenshot = driver.get_screenshot_as_png()
        allure.attach(
            screenshot,
            name="Missing Element Error Screenshot",
            attachment_type=allure.attachment_type.PNG
        )
        raise  # Re-raise the exception to mark the test as failed

    # If the element is found, proceed with the assertion
    assert "Your username is invalid!" in message.text