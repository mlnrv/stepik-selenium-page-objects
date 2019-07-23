from selenium.webdriver.common.by import By


class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.XPATH, '//span/a')


class CartPageLocators(object):
    CART_ITEMS = (By.ID, "basket-items")
    MSG_EMPTY_CART = (By.ID, "content_inner")


class MainPageLocators(object):
    pass


class LoginPageLocators(object):
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators(object):
    ADD_TO_BASKET = (By.CLASS_NAME, "add-to-basket")
    MSG_SUCCESS_ADDED_TO_CART = (By.CLASS_NAME, "alertinner")
    MSG_PRODUCT_IN_CART = (By.CLASS_NAME, "alertinner > strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.col-sm-6.product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.col-sm-6.product_main > p")
