from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        current_url = self.browser.current_url
        assert "login" in current_url, "url doesn't contain login word"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        is_login_form = self.browser.is_element_present(*LoginPageLocators.LOGIN_FORM)
        assert is_login_form, "login page doesn't contain login form"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        is_register_form = self.browser.is_element_present(*LoginPageLocators.REGISTER_FORM)
        assert is_register_form, "login page doesn't contain register form"
