import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def driver_yandex():
    options = webdriver.ChromeOptions()
    service = Service(executable_path=fr"C:\Users\Фантомас\PycharmProjects\Lookdecor\resource\yandexdriver.exe")
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()