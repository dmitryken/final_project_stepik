from .locators import MainPageLocators
from .base_page import BasePage


class BasketPage(BasePage):
    def basket_should_be_empty_message(self):
        assert self.is_element_present(*MainPageLocators.BASKET_MESSAGE), "Basket empty message is not displayed"

    def should_be_no_order(self):
        assert self.is_not_element_present(*MainPageLocators.BASKET_ORDER), "Basket is not empty"

