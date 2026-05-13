import pytest, time, math
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
import os

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_with_tabs(driver):
    # sleep(3)
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    driver.execute_script("window.open('https://the-internet.herokuapp.com/javascript_alerts', '_blank');")
    driver.execute_script("window.open('https://google.com', '_blank');")
    # Получаем список всех вкладок
    tabs = driver.window_handles
    print("Идентификаторы вкладок:", tabs)
    # Переключаемся на вторую вкладку (Google)
    sleep(2)
    driver.switch_to.window(tabs[0])
    sleep(2)
    print("Текущая вкладка:", driver.current_window_handle)
    driver.close()
    sleep(2)
    tabs = driver.window_handles
    driver.switch_to.window(tabs[0])
    print("Текущая вкладка:", driver.current_window_handle)
    sleep(2)

def test_with_hover(driver):
    url = "https://the-internet.herokuapp.com/hovers"
    driver.get(url)
    element_to_hover = driver.find_element(By.CSS_SELECTOR, "#content > div > div:nth-child(5)")
    actions = ActionChains(driver)
    actions.move_to_element(element_to_hover).perform()
    sleep(5)

def test_dragging(driver):
    driver.get("https://jqueryui.com/droppable/")
    # Переключаемся в iframe, если drag-and-drop внутри фрейма
    driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))

    # Находим элементы
    source = driver.find_element(By.ID, "draggable")  # Что перетаскиваем
    target = driver.find_element(By.ID, "droppable")  # Куда перетаскиваем

    # Выполняем перетаскивание
    actions = ActionChains(driver)
    actions.drag_and_drop(source, target).perform()
    sleep(5)

def test_upload(driver):
    url = "https://the-internet.herokuapp.com/upload"
    driver.get(url)

    # Находим input-элемент
    file_input = driver.find_element(By.ID, "file-upload")

    # Указываем путь к файлу
    file_path = "C:/Users/user/Downloads/c8hf38tafgwfwcknhtzx.jpg"  # Укажите путь к файлу на своем компьютере
    file_input.send_keys(file_path)
    sleep(3)

    # Отправляем форму (если требуется)
    upload_button = driver.find_element(By.ID, "file-submit")
    upload_button.click()
    sleep(3)
