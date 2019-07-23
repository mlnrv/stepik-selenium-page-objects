from pages.base_page import BasePage
from pages.locators import CartPageLocators


class CartPage(BasePage):

    def check_cart_is_empty_cart_msg(self):
        msg_empty_cart = self.browser.find_element(*CartPageLocators.MSG_EMPTY_CART).text
        assert "Your basket is empty." in msg_empty_cart, "cart is not empty"

    def check_no_products_in_cart(self):
        no_cart_items = self.is_not_element_present(*CartPageLocators.CART_ITEMS)
        assert no_cart_items, "cart items are present in cart"
