from .base_page import BasePage
from .locators import LoginPageLocators
from selenium import webdriver

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "'login' not in current url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form not found"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_FORM), "Registration form not found"

    def register_new_user(self, email, password):
        reg_email = self.browser.find_element(*LoginPageLocators.EMAIL)
        reg_email.send_keys(email)
        reg_pass = self.browser.find_element(*LoginPageLocators.PASSWORD)
        reg_pass.send_keys(password)
        conf_pass = self.browser.find_element(*LoginPageLocators.COFIRM_PASSWORD)
        conf_pass.send_keys(password)
        reg_button  = self.browser.find_element(*LoginPageLocators.REG_BUTTON)
        reg_button.click()