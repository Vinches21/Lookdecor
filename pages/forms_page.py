import random
from pages.base_page import BasePage
from locators.forms_locators import CallbackLocators, CooperationLocators


class CallbackForm(BasePage):
    locators = CallbackLocators()

    def filling_callback_form(self):
        self.elements_is_visible(self.locators.BUTTON_ORDER_A_CALL).click()
        self.elements_is_visible(self.locators.NAME).send_keys("Иванов Тест")
        self.elements_is_visible(self.locators.PHONE).click()
        self.elements_is_visible(self.locators.PHONE).send_keys(random.randint(9000000000, 9999999999))
        self.elements_is_visible(self.locators.TIME).send_keys(random.randint(9, 21))
        lst = [self.elements_is_visible(self.locators.DEPARTAMENT_WALLPAPER),
               self.elements_is_visible(self.locators.DEPARTAMENT_PLATE)]
        random.choice(lst).click()
        # self.element_is_visible(self.locators.BUTTON_CALL_ME_BACK).click()

class CooperationForm(BasePage):
    locators = CooperationLocators()

    def filling_cooperation_form(self):
        self.elements_is_visible(self.locators.NAME).send_keys("Иванов")
        self.elements_is_visible(self.locators.EMAIL).send_keys(f"test{random.randint(1000, 9000)}@yandex.ru")
        self.elements_is_clickable(self.locators.NUMBER).click()
        self.elements_is_visible(self.locators.NUMBER).send_keys(random.randint(9000000000, 9999999999))
        self.elements_is_visible(self.locators.TEXT).send_keys("Какой-то текст")
        # self.elements_is_clickable(self.locators.BUTTON_ME).click()




