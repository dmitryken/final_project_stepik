from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(By.CSS_SELECTOR, "#login_link"), "Login link is not presented"

    def should_be_login_url(self):
        link = "http://selenium1py.pythonanywhere.com/accounts/login/"

    def should_be_login_form(self):
        assert self.is_element_present(By.CSS_SELECTOR, "#login_form"), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(By.CSS_SELECTOR, "#register_form"), "Register form is not presented"

