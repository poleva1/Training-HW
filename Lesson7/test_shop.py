import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.ShopPage import ShopPage

# Фикстура для создания WebDriver
@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()

def test_shop(driver):
    shop_page = ShopPage(driver)
    driver.get("https://www.saucedemo.com/")
    shop_page.authorisation("standard_user", "secret_sauce")
    shop_page.add_to_cart()
    shop_page.go_to_cart()
    shop_page.checkout()
    shop_page.fill_form("Иван", "Петров", "123456")
    total = shop_page.get_total()

    assert total == "Total: $58.29", f"Итоговая сумма не равна $58.29, а равна {total}"
    print("Итоговая сумма проверена успешно и равна $58.29.")

    driver.quit()
