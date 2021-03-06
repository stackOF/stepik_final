from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By
from selenium import webdriver


class ProductPage(BasePage):
    def add_article_to_cart(self):
        add_to_cart_btn = self.browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
        add_to_cart_btn.click()

    def check_added_to_cart_article_name(self):
        assert self.browser.find_element(*ProductPageLocators.ARTICLE_NAME).text == \
               self.browser.find_element(*ProductPageLocators.CART_ARTICLE_NAME).text,\
            "The article name in the basket does not match the item added or the article is not added to the basket"

    def check_added_to_cart_article_cost(self):
        assert self.browser.find_element(*ProductPageLocators.ARTICLE_COST).text == \
               self.browser.find_element(*ProductPageLocators.CART_COST).text, \
            "The article cost in the basket does not match the item added"

    #Блок проверок на наличие элементов---------------------------------------------------------------------------------
    def should_be_add_to_cart_button_on_product_page(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART_BTN), "Add to cart button not found"

    def should_be_article_name_on_product_page(self):
        assert self.is_element_present(*ProductPageLocators.ARTICLE_NAME), "Article name not found on page"

    def should_be_article_cost_on_product_page(self):
        assert self.is_element_present(*ProductPageLocators.ARTICLE_COST), "Article cost not found on page"

    def should_be_article_name_in_message(self):
        assert self.is_element_present(*ProductPageLocators.CART_ARTICLE_NAME), "Article name in cart not found on page"

    def should_be_article_cost_in_message(self):
        assert self.is_element_present(*ProductPageLocators.CART_COST), "Article cost in cart not found on page"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_not_be_success_message_due_to_not_disappearing(self):
        assert self.is_disappeared(*ProductPageLocators.DISAPPEARED_MESSAGE), \
            "Success message is presented, but should not be (should have disappeared)"
    #Конец блока проверок на наличие элементов--------------------------------------------------------------------------