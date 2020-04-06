from .pages.product_page import ProductPage
import time
from selenium import webdriver
import pytest

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()

    #Проверка на промо (не явное задание)
    #page.should_be_promo_in_link()

    #Проверяем, что на странице есть все элементы, с которыми будем работать
    # (!Только те, что есть и нужны до добавления товара в корзину)
    page.should_be_article_name_on_product_page()
    page.should_be_article_cost_on_product_page()
    page.should_be_add_to_cart_button_on_product_page()

    #Тест добавления товара в корзину
    page.add_article_to_cart()
    page.solve_quiz_and_get_code()

    #Проверки наличия новых элементов, что добавляются после успешного долобавления товара в корзину
    page.should_be_article_name_in_message()
    page.should_be_article_cost_in_message()

    #Проверки соответствия наименования и цены нав странице  с этими же полями в корзине
    page.check_added_to_cart_article_name()
    page.check_added_to_cart_article_cost()
    #time.sleep(2)



