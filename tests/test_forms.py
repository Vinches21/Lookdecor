import time

from pages.forms_page import CallbackForm, CooperationForm


class TestForms:
    def test_callback_form(self, driver):
        cb = CallbackForm(driver, "https://lookdecor.ru/")
        cb.open()
        cb.filling_callback_form()

    def test_cooperation_form(self, driver):
        coop = CooperationForm(driver, 'https://lookdecor.ru/partnership/')
        coop.open()
        coop.filling_cooperation_form()
        time.sleep(5)




