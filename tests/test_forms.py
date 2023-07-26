from pages.forms_page import CallbackForm


class TestForms:
    def test_callback_form(self, driver):
        cb = CallbackForm(driver, "https://lookdecor.ru/")
        cb.open()
        cb.filling_callback_form()




