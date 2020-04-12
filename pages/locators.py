from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_FORM = (By.CSS_SELECTOR, "#register_form")

    EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    COFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_BUTTON = (By.CSS_SELECTOR, "#register_form > button")

class ProductPageLocators():
    ADD_TO_CART_BTN = (By.CLASS_NAME, "btn-add-to-basket")
    ARTICLE_NAME = (By.CSS_SELECTOR, "div.col-sm-6.product_main>h1")
    ARTICLE_COST = (By.CSS_SELECTOR, "div.col-sm-6.product_main>p.price_color")
    CART_ARTICLE_NAME = (By.CSS_SELECTOR, "#messages>div:nth-child(1)>div>strong")
    CART_COST = (By.CSS_SELECTOR, "#messages>div.alert.alert-safe.alert-noicon.alert-info.fade.in>div>p:nth-child(1)>strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_BTN = (By.LINK_TEXT, "View basket")
    EMPTY_BASKET_MES = (By.CSS_SELECTOR, "#content_inner>p")
    ARTICLE_IN_BASKET = (By.CLASS_NAME, "basket_summary")


