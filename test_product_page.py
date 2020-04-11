from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
import time
from selenium import webdriver
import pytest
from .pages.locators import ProductPageLocators

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.should_not_be_article_in_basket()
    page.should_be_empty_basket_message()

@pytest.mark.xfail(reason="negative test")
def test_guest_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.should_be_article_in_basket()
    page.should_not_be_empty_basket_message()

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
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()

    # Проверка на промо (не явное задание)
    # page.should_be_promo_in_link()

    # Проверяем, что на странице есть все элементы, с которыми будем работать
    # (!Только те, что есть и нужны до добавления товара в корзину)
    page.should_be_article_name_on_product_page()
    page.should_be_article_cost_on_product_page()
    page.should_be_add_to_cart_button_on_product_page()

    # Тест добавления товара в корзину
    page.add_article_to_cart()
    page.solve_quiz_and_get_code()

    # Проверки наличия новых элементов, что добавляются после успешного долобавления товара в корзину
    page.should_be_article_name_in_message()
    page.should_be_article_cost_in_message()

    # Проверки соответствия наименования и цены нав странице  с этими же полями в корзине
    page.check_added_to_cart_article_name()
    page.check_added_to_cart_article_cost()
    # time.sleep(2)

# Возможность логина со страницы товаров
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

# Возможность перехода на страницу логина со страницы товаров
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.xfail(reason="negative test")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_article_to_cart()
    assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "A message about a successful article addition after some time is present"

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "A message about a successful article addition is present"

@pytest.mark.xfail(reason="negative test")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_article_to_cart()
    assert page.is_disappeared (*ProductPageLocators.SUCCESS_MESSAGE), \
        "A message about a successful article addition after some time is not disappeared"

