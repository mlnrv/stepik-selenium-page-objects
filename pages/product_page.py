from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    
    def add_product_to_cart(self):
        btn_add_to_cart = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        btn_add_to_cart.click()

    def get_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        return product_name

    def get_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        return product_price

    def is_product_added_to_cart(self):
        product_name = self.get_product_name()
        msg_added_to_cart = self.browser.find_element(*ProductPageLocators.MSG_SUCCESS_ADDED_TO_CART).text
        product_name_in_cart = self.browser.find_element(*ProductPageLocators.MSG_PRODUCT_IN_CART).text
        
        assert product_name == product_name_in_cart, \
            f"product names are different: {product_name} != {product_name_in_cart}"

        assert product_name + " has been added to your basket." == msg_added_to_cart, \
            f"product {product_name} has not been added to cart"

    def should_not_be_success_message(self):
        msg_is_not_present = self.is_not_element_present(*ProductPageLocators.MSG_SUCCESS_ADDED_TO_CART)
        assert msg_is_not_present, "success message is present"

    def should_be_disappeared_success_message(self):
        msg_is_disappeared = self.is_disappeared(*ProductPageLocators.MSG_SUCCESS_ADDED_TO_CART)
        assert msg_is_disappeared, "success message is not disappeared"
