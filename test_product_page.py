import pytest
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
