import time
from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert '/login' in self.browser.current_url, f"expected '/login' to be substring of " \
                                                     f"'{self.browser.current_url}'"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is absent"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is absent"

    def register_new_user(self):
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time()) + "check_me"
        self.browser.find_element(*LoginPageLocators.REG_NAME_FIELD).send_keys(email)
        self.browser.find_element(*LoginPageLocators.PASS_NAME_FIELD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.CONFIRM_PASS_FIELD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()

