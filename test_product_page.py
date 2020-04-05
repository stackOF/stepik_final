from .pages.product_page import ProductPage
import time
from selenium import webdriver

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_promo_in_link()
    page.add_article_to_cart()

    page.solve_quiz_and_get_code()
    page.check_added_to_cart_article_name()
    page.check_added_to_cart_article_cost()
    time.sleep(2)



