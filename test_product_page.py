import pytest
from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators
import time

links = [
     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
     pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7"
                  , marks=pytest.mark.xfail),
     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
]

test_link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'


def go_to_login_page(browser):
    link = browser.find_element_by_css_selector("#login_link")
    link.click()


# @pytest.mark.skip
@pytest.mark.parametrize('link', links)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    # Test case before add in basket
    page.should_be_before_add_in_basket()
    # Click add
    page.add_product_in_basket()
    # Calculate quiz
    page.solve_quiz_and_get_code()
    description_in_basket = page.get_text(*ProductPageLocators.DESCRIPTION_PRODUCT_IN_BASKET)
    price_in_basket = page.get_text(*ProductPageLocators.PRICE_PRODUCT_IN_BASKET)
    # Test case after add in basket
    # time.sleep(1000)
    page.should_be_after_add_in_basket(price_in_basket, description_in_basket)


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, test_link)
    page.open()
    page.add_product_in_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, test_link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, test_link)
    page.open()
    page.add_product_in_basket()
    page.should_not_be_success_message_after_add_in_basket()
