import random
from pages.base_page import BasePage
from locators.forms_locators import CallbackLocators



class CallbackForm(BasePage):
    locators = CallbackLocators()

    def filling_callback_form(self):
        self.element_is_visible(self.locators.BUTTON_ORDER_A_CALL).click()
        self.element_is_visible(self.locators.NAME).send_keys("Иванов Тест")
        self.element_is_visible(self.locators.PHONE).click()
        self.element_is_visible(self.locators.PHONE).send_keys(random.randint(9000000000, 9999999999))
        self.element_is_visible(self.locators.TIME).send_keys(random.randint(9, 21))
        lst = [self.element_is_visible(self.locators.DEPARTAMENT_WALLPAPER),
               self.element_is_visible(self.locators.DEPARTAMENT_PLATE)]
        random.choice(lst).click()
        # self.element_is_visible(self.locators.BUTTON_CALL_ME_BACK).click()



