import pytest
import allure
from selenium import webdriver


@pytest.fixture(scope="function")
def driver():
    print("\nЗапуск браузера...")
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless") # запуск без окна
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(10)

    yield browser

    print("\nЗакрытие браузера...")
    browser.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Этот хук выполняется на каждом этапе выполнения теста (setup, call, teardown)
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        try:
            if "driver" in item.fixturenames:
                web_driver = item.funcargs["driver"]

                allure.attach(
                    web_driver.get_screenshot_as_png(),
                    name="Скриншот при падении",
                    attachment_type=allure.attachment_type.PNG
                )

                allure.attach(
                    web_driver.page_source,
                    name="HTML-код страницы",
                    attachment_type=allure.attachment_type.HTML
                )
        except Exception as e:
            print(f"Не удалось сделать скриншот: {e}")
