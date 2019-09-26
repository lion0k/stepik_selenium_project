from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators


def go_to_login_page(browser):
    link = browser.find_element_by_css_selector("#login_link")
    link.click()


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
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
    page.should_be_after_add_in_basket(price_in_basket, description_in_basket)
