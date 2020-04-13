from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.locators import AllPagesLocators
import pytest

@pytest.mark.login_guest #тесты
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, AllPagesLocators.MAINPAGELINK)
        page.open()
        page.go_to_login_page()

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, AllPagesLocators.MAINPAGELINK)
        page.open()
        page.should_be_login_link()

def test_guest_can_go_to_login_page(browser):

    page = MainPage(browser, AllPagesLocators.MAINPAGELINK)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = BasketPage(browser, AllPagesLocators.MAINPAGELINK)
    page.open()
    page.go_to_basket_page()
    page.should_not_be_article_in_basket()
    page.should_be_empty_basket_message()

@pytest.mark.xfail(reason="negative test")
def test_guest_see_product_in_basket_opened_from_main_page(browser):
    page = BasketPage(browser, AllPagesLocators.MAINPAGELINK)
    page.open()
    page.go_to_basket_page()
    page.should_be_article_in_basket()
    page.should_not_be_empty_basket_message()