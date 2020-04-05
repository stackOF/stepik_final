from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_CART_BTN = (By.CLASS_NAME, "btn-add-to-basket")
    ARTICLE_NAME = (By.CSS_SELECTOR, "div.col-sm-6.product_main>h1")
    ARTICLE_COST = (By.CSS_SELECTOR, "div.col-sm-6.product_main>p.price_color")
