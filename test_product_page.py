from .pages.product_page import ProductPage
import time
from selenium import webdriver

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()

    #Проверка на промо (не явное задание)
    page.should_be_promo_in_link()

    #Проверяем, что на странице есть все элементы, с которыми будем работать (!только те, что нажатия на добавление товара)
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
    time.sleep(2)



