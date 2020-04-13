from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.locators import ProductPageLocators
from .pages.locators import LoginPageLocators
from .pages.locators import AllPagesLocators

from selenium import webdriver
import pytest
import time

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = BasketPage(browser, AllPagesLocators.MAINPAGELINK)
    page.open()
    page.go_to_basket_page()
    page.should_not_be_article_in_basket()
    page.should_be_empty_basket_message()

@pytest.mark.xfail(reason="negative test")
def test_guest_see_product_in_basket_opened_from_product_page(browser):
    page = BasketPage(browser, AllPagesLocators.MAINPAGELINK)
    page.open()
    page.go_to_basket_page()
    page.should_be_article_in_basket()
    page.should_not_be_empty_basket_message()

@pytest.mark.need_review
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  pytest.param(
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                      marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param(
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                      marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
                                  ])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_article_name_on_product_page()
    page.should_be_article_cost_on_product_page()
    page.should_be_add_to_cart_button_on_product_page()
    page.add_article_to_cart()
    page.solve_quiz_and_get_code() #осталось от задания курса, сейчас не несет никакой логики
    page.should_be_article_name_in_message()
    page.should_be_article_cost_in_message()
    page.check_added_to_cart_article_name()
    page.check_added_to_cart_article_cost()

def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser,AllPagesLocators.ARTICLELINK1)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser,AllPagesLocators.ARTICLELINK1)
    page.open()
    page.go_to_login_page()

@pytest.mark.xfail(reason="negative test")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, AllPagesLocators.ARTICLELINK2)
    page.open()
    page.add_article_to_cart()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, AllPagesLocators.ARTICLELINK2)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail(reason="negative test")
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, AllPagesLocators.ARTICLELINK2)
    page.open()
    page.add_article_to_cart()
    page.should_not_be_success_message_due_to_not_disappearing()

@pytest.mark.authorized_user
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, AllPagesLocators.MAINPAGELINK)
        page.open()
        page.go_to_login_page()

        email = str(time.time()) + "@fakemail.org"
        password = 'A1B2C3QWERTY123'
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, AllPagesLocators.ARTICLELINK2)
        page.open()
        page.should_be_article_name_on_product_page()
        page.should_be_article_cost_on_product_page()
        page.should_be_add_to_cart_button_on_product_page()
        page.add_article_to_cart()
        # page.solve_quiz_and_get_code() #осталось от задания курса, сейчас не несет никакой логики
        page.should_be_article_name_in_message()
        page.should_be_article_cost_in_message()
        page.check_added_to_cart_article_name()
        page.check_added_to_cart_article_cost()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, AllPagesLocators.ARTICLELINK2)
        page.open()
        page.should_not_be_success_message()