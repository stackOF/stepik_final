from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_article_to_cart(self):
        self.should_be_add_to_cart_button_on_product_page()
        add_to_cart_btn = self.browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
        add_to_cart_btn.click()

    def should_be_add_to_cart_button_on_product_page(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART_BTN), "Add to cart button not found"

    def should_be_promo_in_link(self):
        # проверка на наличие промо в url адресе
        assert "?promo=newYear" in self.browser.current_url, "Not Exist 'promo' in current url"

    def check_added_to_cart_article_name(self):
        self.should_be_article_name_on_product_page()
        assert self.browser.find_element(By.CSS_SELECTOR, "div.col-sm-6.product_main > h1").text ==\
               self.browser.find_element(By.CSS_SELECTOR, "#messages>div:nth-child(1)>div>strong").text,\
            "The article name in the basket does not match the item added or the article is not added to the basket"

    def check_added_to_cart_article_cost(self):
        self.should_be_article_cost_on_product_page()
        assert self.browser.find_element(By.CSS_SELECTOR, "div.col-sm-6.product_main>p.price_color").text ==\
               self.browser.find_element(By.CSS_SELECTOR,
                                         "#messages>div.alert.alert-safe.alert-noicon.alert-info.fade.in>div>p:nth-child(1)>strong").text,\
            "The article cost in the basket does not match the item added"

    def should_be_article_name_on_product_page(self):
        assert self.is_element_present(*ProductPageLocators.ARTICLE_NAME), "Article name not found on page"

    def should_be_article_cost_on_product_page(self):
        assert self.is_element_present(*ProductPageLocators.ARTICLE_COST), "Article cost not found on page"