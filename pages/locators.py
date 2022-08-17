from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, "span > a")
    BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")
    BASKET_ORDER = (By.CLASS_NAME, "col-sm-4 col-sm-offset-8")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REG_NAME_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    PASS_NAME_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    CONFIRM_PASS_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form > button")


class ProductPageLocators:
    BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    BOOK_NAME = (By.CSS_SELECTOR, "div.col-sm-6.product_main > h1")
    ADDED_BOOK_NAME = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    BOOK_PRICE = (By.CSS_SELECTOR, "div.col-sm-6.product_main > p.price_color:nth-child(2)")
    ADDED_BOOK_PRICE = (By.CSS_SELECTOR, "div.alertinner > p > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(1)")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")




