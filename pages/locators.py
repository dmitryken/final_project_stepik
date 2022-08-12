from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    BOOK_NAME = (By.CSS_SELECTOR, "div.col-sm-6.product_main > h1")
    ADDED_BOOK_NAME = (By.CSS_SELECTOR, "div.alertinner > strong:nth-child(1)")
    BOOK_PRICE = (By.CSS_SELECTOR, "div.col-sm-6.product_main > p.price_color:nth-child(2)")
    ADDED_BOOK_PRICE = (By.CSS_SELECTOR, "div.alertinner > p > strong")



