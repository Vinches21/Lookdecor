from pages.base_page import BasePage


def test_form(driver):
    bp = BasePage(driver, 'https://lookdecor.ru/')
    bp.open()
