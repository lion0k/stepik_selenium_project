from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    price: str
    description: str

    def should_be_before_add_in_basket(self):
        self.should_be_button_add_basket()
        self.should_be_price_product()
        self.should_be_description_product()

    def should_be_after_add_in_basket(self, price, description):
        self.should_be_price_product_in_basket()
        self.should_be_description_product_in_basket()
        self.check_correct_price_in_basket(price)
        self.check_correct_description_in_basket(description)

    def should_be_button_add_basket(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_TO_BASKET), "Button add to basket is not present"

    def should_be_price_product(self):
        assert self.is_element_present(*ProductPageLocators.PRICE_PRODUCT), "Price product is not present"
        self.price = self.get_text(*ProductPageLocators.PRICE_PRODUCT)

    def should_be_description_product(self):
        assert self.is_element_present(*ProductPageLocators.DESCRIPTION_PRODUCT), "Description product is not present"
        self.description = self.get_text(*ProductPageLocators.DESCRIPTION_PRODUCT)

    def add_product_in_basket(self):
        link = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        link.click()

    def should_be_price_product_in_basket(self):
        assert self.is_element_present(*ProductPageLocators.PRICE_PRODUCT_IN_BASKET),\
            "Price product is not present in basket"

    def should_be_description_product_in_basket(self):
        assert self.is_element_present(*ProductPageLocators.DESCRIPTION_PRODUCT_IN_BASKET),\
            "Description product is not present in basket"

    def check_correct_price_in_basket(self, price):
        assert self.price == price, "Price in basket is not equal price in product page"

    def check_correct_description_in_basket(self, description):
        assert self.description == description, "Description in basket is not equal description in product page"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.DESCRIPTION_PRODUCT_IN_BASKET), \
            "Success message is presented, but should not be"

    def should_not_be_success_message_after_add_in_basket(self):
        assert self.is_disappeared(*ProductPageLocators.DESCRIPTION_PRODUCT_IN_BASKET), \
            "Success message is presented and not disappeared, but should not be"
