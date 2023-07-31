from locators.forms_locators import FooterLocators
from pages.base_page import BasePage



class MainPage(BasePage):
    locators = FooterLocators()

    def checking_pages_in_the_footer(self):
        self.elements_is_visible(self.locators.ABOT_THE_COMPANY).click()
        text = self.elements_is_present(self.locators.TEXT_COMPANY).text
        assert text == "О КОМПАНИИ", "The text doesn't match"
        self.driver.back()
