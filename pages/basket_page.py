from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest

class BasketPage(BasePage):
    def should_not_be_article_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ARTICLE_IN_BASKET), "Basket is not empty"

    def should_be_empty_basket_message(self):
        assert self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MES).text ==\
               "Your basket is empty. Continue shopping", "There is not text that the basket is empty"

    def should_be_article_in_basket(self):
        assert self.is_element_present(*BasketPageLocators.ARTICLE_IN_BASKET), "Basket is empty"

    def should_not_be_empty_basket_message(self):
        assert self.is_not_element_present(*BasketPageLocators.EMPTY_BASKET_MES).text ==\
               "Your basket is empty. Continue shopping","There is text that the basket is empty"