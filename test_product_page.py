from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import pytest


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = LoginPage(browser, link)
        page.open()
        page.go_to_login_page()
        page.register_new_user()
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.should_be_correct_book_name()
        page.should_be_correct_book_price()


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_be_correct_book_name()
    page.should_be_correct_book_price()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "https://selenium1py.pythonanywhere.com/catalogue/the-robot-novels_25/"
    page = BasketPage(browser, link)
    page.open()
    page.open_link_on_empty_basket()
    page.basket_should_be_empty_message()
    page.should_be_no_order()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = LoginPage(browser, link)
    page.open()
    page.go_to_login_page()


def test_user_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


def test_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8"
    page = ProductPage(browser, link, 4)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()
    page.success_message_should_be_disappear()


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link, 0)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()


def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link, 0)
    page.open()
    page.add_product_to_basket()
    page.success_message_should_be_disappear()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()



