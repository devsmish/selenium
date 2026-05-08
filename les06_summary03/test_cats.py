import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://suninjuly.github.io/cats.html")
    yield driver
    driver.quit()


def test_check_headline(driver):
    # headline = driver.find_element(By.CSS_SELECTOR, '.jumbotron-heading').text
    # headline = driver.find_element(By.CSS_SELECTOR, '[value="Cat memes"]').text
    headline = driver.find_element(By.TAG_NAME, "h1").text
    assert headline == "Cat memes"


def test_check_card_min(driver):
    card = driver.find_element(By.CSS_SELECTOR, ".col-sm-4:nth-child(1) small").text
    assert card == "9 mins"


def test_check_first_img(driver):
    first_card = driver.find_element(By.CSS_SELECTOR, ".col-sm-4:nth-child(1)")
    assert first_card.is_displayed()


def test_check_all_img(driver):
    all_card = driver.find_elements(By.CSS_SELECTOR, ".col-sm-4")
    assert len(all_card) == 6
