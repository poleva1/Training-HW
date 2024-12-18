import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from Lesson10.pages10.shop_page import ShopPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()

@allure.epic("Тестирование интернет-магазина")
@allure.severity("Critical")
@allure.description("Проверка авторизации, добавления товара в корзину и оформления")
@allure.title("Проверка оформления заказа")
def test_shop(driver):
    shop_page = ShopPage(driver)

    with allure.step("Открыть страницу магазина"):
        shop_page.open("https://www.saucedemo.com/")

    with allure.step("Авторизоваться на странице"):
        shop_page.get_authorisation("standard_user", "secret_sauce")

    with allure.step("Добавить товары в корзину"):
        shop_page.add_to_cart()

    with allure.step("Перейти в корзину"):
        shop_page.get_to_cart()

    with allure.step("Нажать Checkout"):
        shop_page.click_checkout()

    with allure.step("Заполнить форму своими данными {first_name} {last_name} {post_code}. Нажать кнопку Continue"):
        shop_page.add_checkout_data("Имя", "Фамилия", "123456")

    with allure.step("Получить итоговую стоимость заказа {total}"):
        shop_page.get_total()
        assert total == "58,29"