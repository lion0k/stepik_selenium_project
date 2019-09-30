from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import BasePageLocators


class LoginPage(BasePage):
    def register_new_user(self, email: str, password: str) -> None:
        assert self.send(*LoginPageLocators.EMAIL_FIELD, email) is None, 'Not found or exist field email'
        assert self.send(*LoginPageLocators.PASSWORD_FIELD, password) is None, 'Not found or exist field password'
        assert self.send(*LoginPageLocators.CONFORM_PASSWORD_FIELD, password) is None, 'Not found or exist field\
         conform password'
        assert self.click(*LoginPageLocators.BUTTON_REGISTRATION_SUBMIT) is None, 'Not found or exist button \
        submit registration'
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User is not login in"

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url, "Login link is not found"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
