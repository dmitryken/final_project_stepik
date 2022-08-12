from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):

        self.should_be_login_url()
        assert '/login' in link, f"expected '/link' to be substring of '{link}'"

        self.should_be_login_form()
        self.should_be_register_form()

