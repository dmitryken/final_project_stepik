from .locators import ProductPageLocators
from .base_page import BasePage


class ProductPage(BasePage):
    def add_product_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        link.click()

    def should_be_correct_book_name(self):
        assert self.is_element_present(*ProductPageLocators.BOOK_NAME) == \
               self.is_element_present(*ProductPageLocators.ADDED_BOOK_NAME), "Another book's name"

    def should_be_correct_book_price(self):
        assert self.is_element_present(*ProductPageLocators.BOOK_PRICE) == \
               self.is_element_present(*ProductPageLocators.ADDED_BOOK_PRICE), "Another book's price"
