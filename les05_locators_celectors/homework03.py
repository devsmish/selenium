"""Написать автотест с использованием Python и Pytest, который:
1. Открывает https://itcareerhub.de/ru
2. Проверяет, что на странице отображаются:
Логотип ITCareerHub
Ссылка “Программы”
Ссылка “Способы оплаты”
Ссылка “О нас”
Ссылка “Контакты”
Ссылка “Отзывы”
Ссылка “Блог”
Кнопки переключения языка (ru и de)
3. Кликнуть по разделу “Контакты”
4. Кликнуть по кнопке “Обратный звонок”
5. Проверить что текст “Запишитесь на бесплатную карьерную консультацию” отображается во всплывающем окне."""

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get('https://itcareerhub.de/ru')
    yield driver
    driver.quit()


def test_homepage(driver):
    logo = driver.find_element(By.CSS_SELECTOR, 'img[alt="IT Career Hub"]')
    assert logo.is_displayed()


def test_menu_prog(driver):
    prog_button = driver.find_element(By.CSS_SELECTOR, 'a.tn-atom[href="#submenu:more"]')
    assert prog_button.is_displayed()
    assert prog_button.text == 'Программы'


def test_menu_payment(driver):
    payment_methods = driver.find_element(By.CSS_SELECTOR, 'a.tn-atom[href="#rec1921734713"]')
    assert payment_methods.is_displayed()
    assert payment_methods.text == 'Способы оплаты'


def find_about(driver):
    about = driver.find_element(By.CSS_SELECTOR, 'a.tn-atom[href="#submenu:more2"]')
    return about

def test_menu_about(driver):
    about = find_about(driver)
    assert about.is_displayed()
    assert about.text == 'О нас'


def find_contacts(driver):
    find_about(driver).click()
    contacts = driver.find_element(By.CSS_SELECTOR, 'a[href="/ru/contact-us"]')
    return contacts


def test_menu_contacts(driver):
    contacts = find_contacts(driver)
    assert contacts.is_displayed()
    assert contacts.text == 'Контакты'


def test_menu_reviews(driver):
    reviews = driver.find_element(By.CSS_SELECTOR, 'a.tn-atom[href="/reviews"]')
    assert reviews.is_displayed()
    assert reviews.text == 'Отзывы'


def test_menu_blog(driver):
    blog = driver.find_element(By.CSS_SELECTOR, 'a.tn-atom[href="https://blog.itcareerhub.de/"]')
    assert blog.is_displayed()
    assert blog.text == 'Блог'


def test_button_callback(driver):
    find_contacts(driver).click()
    buttons = driver.find_elements(By.CSS_SELECTOR,'a[href="#popup:form-tr"]')
    visible_button = None
    for button in buttons:
        if button.is_displayed():
            visible_button = button
            break
    visible_button.click()
    time.sleep(2)
    popup_title = driver.find_element(By.CSS_SELECTOR, 'div[field="tn_text_175871291756015470"]')
    assert "Запишитесь на бесплатную" in popup_title.get_attribute('textContent')


def test_language_switch_to_de_to_ru(driver):
    lang_de_btn = driver.find_element(By.CSS_SELECTOR, 'a[href="/"][style*="color: inherit"]')

    lang_de_btn.click()
    time.sleep(3)

    assert "/ru" not in driver.current_url

    lang_ru_btn = driver.find_element(By.CSS_SELECTOR, 'a[href="/ru"][style*="color: inherit"]')

    lang_ru_btn.click()

    time.sleep(3)

    assert "/ru" in driver.current_url
