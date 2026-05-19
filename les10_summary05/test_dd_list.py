import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
'''Открыть страницу: https://crossbrowsertesting.github.io/hover-menu.html.
Навести курсор на Dropdown.
Навести курсор на Secondary Menu.
Кликнуть Secondary Action.
Проверить заголовок: убедиться, что он содержит Secondary Page.'''

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.get("https://crossbrowsertesting.github.io/hover-menu.html")
    yield driver
    driver.quit()


def test_hover_menu(driver):
    actions = ActionChains(driver)
    dd_btn = driver.find_element(By.CSS_SELECTOR, 'li.dropdown > a')
    actions.move_to_element(dd_btn).perform()
    sm_btn = driver.find_element(By.LINK_TEXT, 'Secondary Menu')
    actions.move_to_element(sm_btn).perform()
    sa_btn = driver.find_element(By.LINK_TEXT, 'Secondary Action')
    sa_btn.click()
    text_header = driver.find_element(By.CSS_SELECTOR, 'div.jumbotron.secondary-clicked > h1')
    assert text_header.text == 'Secondary Page'
