from selenium.webdriver import Remote as RemoteWebDriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators
from math import log, sin


class BasePage:
    def __init__(self, browser: RemoteWebDriver, url, timeout=10):
        self.browser = browser
        self.url = url
        # self.browser.implicitly_wait(timeout)

    def click(self, how, what):
        try:
            self.browser.find_element(how, what).click()
        except NoSuchElementException:
            return None

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def go_to_basket_page(self):
        link = self.browser.find_element(*BasePageLocators.BASKET_PAGE_LINK)
        link.click()

    def get_text(self, how, what):
        try:
            return self.browser.find_element(how, what).text
        except NoSuchElementException:
            return None

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def open(self):
        self.browser.get(self.url)

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"

    def send(self, how, what, keys):
        try:
            self.browser.find_element(how, what).send_keys(keys)
        except NoSuchElementException:
            return None

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(log(abs((12 * sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
