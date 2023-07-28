from pages.mainpage import MainPage


class TestFooter:

    def test_open_footer_pages(self, driver):
        company = MainPage(driver, "https://lookdecor.ru/")
        company.open()
        company.checking_pages_in_the_footer()