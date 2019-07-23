import pytest
from pages.cart_page import CartPage
from pages.product_page import ProductPage
from utils.solve_quiz import solve_quiz_and_get_code


link_product = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
links_promo = [f"{link_product}?promo=offer{num}" for num in range(10)]


@pytest.mark.parametrize('link', links_promo)
def test_guest_can_add_product_to_cart(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_cart()
    solve_quiz_and_get_code(product_page)
    product_page.is_product_added_to_cart()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_not_be_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


def test_guest_cant_see_product_in_cart_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_cart_page()
    page = CartPage(browser, link)
    page.check_cart_is_empty_cart_msg()

