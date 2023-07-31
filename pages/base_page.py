import random

from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage():
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url


    def open(self):
        self.driver.get(self.url)

    """Методы для поиска видимого элемента или нескольких эелементов"""
    def elements_is_visible(self, locator, timeout=20):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=20):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    """Методы для поиска элементов или нескольких элементов из дом-дерева"""

    def elements_is_present(self, locator, timeout=20):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def elements_are_present(self, locator, timeout=20):
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    """Проверка на кликабельность"""

    def elements_is_clickable(self, locator, timeout=20):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    """Скроллинг до нужного места"""

    def go_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    """Методы по имитации нажатия мыши"""

    def action_double_click(self, element):
        action = ActionChains(self.driver)
        action.double_click(element)
        action.perform()

    def action_right_click(self, element):
        action = ActionChains(self.driver)
        action.context_click(element)
        action.perform()

    """Метод который выдаёт корректный(нынешний) url"""

    def current_url(self):
        get_url = self.driver.current_url
        print(f"current url {get_url}")

    """Метод по проверке url"""

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result, "url не совпадают"

    """Метод для сохранения скриншота"""

    def get_screen(self):
        name = f"screenshot{random.randint(1, 1000)}.png"
        self.driver.save_screenshot(fr"C:\Users\Фантомас\PycharmProjects\Lookdecor\{name}")

    """Метод по клику скрытого элемента"""

    def click_hidden_element(self, element):
        self.driver.execute_script("$(arguments[0]).click();", element)
