from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form > button.btn-add-to-basket")
    PRICE_PRODUCT = (By.CSS_SELECTOR, "div.product_main > p.price_color")
    DESCRIPTION_PRODUCT = (By.CSS_SELECTOR, "div.product_main > h1")
    PRICE_PRODUCT_IN_BASKET = (By.CSS_SELECTOR, '#messages div.alert:nth-child(3) > div.alertinner strong')
    DESCRIPTION_PRODUCT_IN_BASKET = (By.CSS_SELECTOR, '#messages div.alert:nth-child(1) > div.alertinner strong')
