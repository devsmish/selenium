'''Тестирование Drag & Drop (Перетаскивание изображения в корзину)
Открыть страницу Drag & Drop Demo.
Перейти по ссылке: https://www.globalsqa.com/demo-site/draganddrop/.
Выполнить следующие шаги:
Захватить первую фотографию (верхний левый элемент).
Перетащить её в область корзины (Trash).
Проверить, что после перемещения:
В корзине появилась одна фотография.
В основной области осталось 3 фотографии.
Ожидаемый результат:
Фотография успешно перемещается в корзину.
Вне корзины остаются 3 фотографии.'''
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
    yield driver
    driver.quit()


def test_drag_and_drop(driver):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.fc-cta-consent"))).click()
    wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".fc-consent-root")))
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe.demo-frame")))

    first_image = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#gallery li")))
    trash = driver.find_element(By.ID, "trash")

    actions = ActionChains(driver)
    actions.click_and_hold(first_image).move_to_element(trash).release().perform()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#trash li")))

    assert len(driver.find_elements(By.CSS_SELECTOR, "#trash li")) == 1
    assert len(driver.find_elements(By.CSS_SELECTOR, "#gallery li")) == 3
