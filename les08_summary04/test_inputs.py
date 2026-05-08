import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')
    yield driver
    driver.quit()


def test_inputs_button(driver):
    wait = WebDriverWait(driver, 5)
    first_name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[name="first-name"]')))
    first_name.send_keys("Sergey")
    last_name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[name="last-name"]')))
    last_name.send_keys("Sergey")
    btn_submit = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[type="submit"]')))
    btn_submit.click()
    id_first_name = wait.until(EC.visibility_of_element_located((By.ID, 'first-name')))
    classes_first = id_first_name.get_attribute("class").split()
    id_last_name = wait.until(EC.visibility_of_element_located((By.ID, 'last-name')))
    classes_last = id_last_name.get_attribute("class").split()

    assert 'alert-success' in classes_first
    assert 'alert-success' in classes_last
    assert 'alert-danger' not in classes_first
    assert 'alert-danger' not in classes_last

    # if "alert-success" in classes_first:
    #     print("Element has the success class!")
    # else:
    #     print("Class not found.")
    #
    # if "alert-success" in classes_last:
    #     print("Element has the success class!")
    # else:
    #     print("Class not found.")
