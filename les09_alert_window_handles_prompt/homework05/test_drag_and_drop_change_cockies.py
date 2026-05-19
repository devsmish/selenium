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

    cookie_fccdcf = {
        "name": "FCCDCF",
        "value": """%5Bnull%2Cnull%2Cnull%2C%5B%22CQkdJAAQkdJAAEsACBUKCfFoAP_gAEPgABBoK3oB_C7EbCFCiDJ3IKMEMAhHABBAYsAw
        AAYAAgAADBIQIAQCgkEYBASAFCACCAAAKASBAAAgCAAAAUAAIAAFAABAAAwAIBAIIAAAgAAAAEAAAAAACIAAEQCAAAAEAEAAkAgAAAIASEAAAA
        AAAACBAAAAAAAAAAAAAAAABAEAAQAAQAAAAAAAiAAAAAAAABAIAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAABAAAAAAAQgsIgH8LsRsIUKIMFcg
        owQwCFcAEABiwDAABgACAAAMEhAgBAKSQRIEAIAQIAAIAAAgBAEAACgICAAAQAAAABUAAEAADAAgEAgAQACAAABAQAAAAAAIgAARAIAAAAQAQA
        CACAAAAgBIQAAAAAAAAIEAAAAAAAAAAAAAAAAAAQAAIADAAAAAAACIAAAAAAAAEAgQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAA
        QAA.ILCIB_C7EbCFCiDJ3IKMEMAhXABBAYsAwAAYAAgAADBIQIAQCkkEaBASAFCACCAAAKASBAAAoCAgAAUAAIAAVAABAAAwAIBAIIEAAgAAAQ
        EAAAAAACIAAEQCAAAAEAEAAkAgAAAIASEAAAAAAAACBAAAAAAAAAAAAAAAABAEAASAAwAAAAAAAiAAAAAAAABAIEAAAAAAAAAAAAAAAAAAAAAg
        AAAAAAAAAABAAAAAAAQgAAE%22%2C%222~61.89.122.161.184.196.230.314.340.442.445.494.550.576.827.1025.1029.1033.104
        6.1047.1051.1097.1126.1166.1301.1342.1415.1725.1765.1942.1958.1987.2068.2072.2074.2107.2213.2219.2223.2224.232
        8.2331.2416.2501.2567.2568.2575.2657.2686.2778.2869.2878.2908.2920.2963.3005.3023.3126.3234.3235.3253.3309.373
        1.6931.8931.13731.15731.33931~dv.%22%2C%221CF2F5CE-A490-447D-A388-D24C2C2A133A%22%5D%2Cnull%2Cnull%2C%5B%5B32%
        2C%22%5B%5C%222bdf0b9c-9fb3-462c-99df-0aad3e3d307f%5C%22%2C%5B1779221255%2C371000000%5D%5D%22%5D%5D%5D
        """.replace("\n", "").replace(" ", ""),
        "domain": ".globalsqa.com",
        "path": "/"
    }

    cookie_fcnec = {
        "name": "FCNEC",
        "value": """%5B%5B%22AKsRol_F-Q5IbIvVqq1ZshISTKTZGQILX1A7f-jMy7dQV9qVYC_If38rh4Qd8lvmka6UE_0U1pJ93WYCLYljCZkQeu
        SeIBo6aoSDWFZLzx6QWqNa7GXguD2_UwLc-nNOXBZ-3a4zJAfc5s3TABNsyH4QMHlDjtwmJg%3D%3D%22%5D%5D
        """.replace("\n", "").replace(" ", ""),
        "domain": ".globalsqa.com",
        "path": "/"
    }

    try:
        driver.add_cookie(cookie_fccdcf)
        driver.add_cookie(cookie_fcnec)
        driver.refresh()
    except Exception as e:
        print(f"Не удалось установить куки: {e}")

    yield driver
    driver.quit()


def test_drag_and_drop(driver):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe.demo-frame")))

    first_image = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#gallery li")))
    trash = driver.find_element(By.ID, "trash")

    actions = ActionChains(driver)
    actions.click_and_hold(first_image).move_to_element(trash).release().perform()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#trash li")))

    assert len(driver.find_elements(By.CSS_SELECTOR, "#trash li")) == 1
    assert len(driver.find_elements(By.CSS_SELECTOR, "#gallery li")) == 3
