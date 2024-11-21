import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.CalcPage import CalcPage

# Фикстура для создания WebDriver
@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()

def test_calculator(driver):
    calc_page = CalcPage(driver)
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    calc_page.set_delay(45)
    calc_page.calculate_sum()
    result_text = calc_page.get_result()
    print(f"Результат: {result_text}")

    driver.quit()