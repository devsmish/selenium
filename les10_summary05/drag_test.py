import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
'''Открыть страницу
Перейти по ссылке: https://crossbrowsertesting.github.io/drag-and-drop.html.
Перетащить элемент draggable в droppable
Найти элемент с id="draggable".
Найти целевую область с id="droppable".
Использовать drag_and_drop() для перетаскивания элемента.
Убедиться, что текст изменился на "Dropped!"
После выполнения drag_and_drop() проверить, что внутри droppable отображается текст "Dropped!".'''

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://crossbrowsertesting.github.io/drag-and-drop.html")
    yield driver
    driver.quit()


def test_dragging(driver):

    # Находим элементы
    source = driver.find_element(By.ID, "draggable")  # Что перетаскиваем
    target = driver.find_element(By.ID, "droppable")  # Куда перетаскиваем

    # Выполняем перетаскивание
    actions = ActionChains(driver)
    actions.drag_and_drop(source, target).perform()

    text_element = driver.find_element(By.CSS_SELECTOR, "#droppable > p")

    assert text_element.text == "Dropped!"
