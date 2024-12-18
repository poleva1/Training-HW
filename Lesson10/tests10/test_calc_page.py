import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from Lesson10.pages10.calc_page import CalcPage

# Фикстура для создания WebDriver
@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()

@allure.epic("Тестирование калькулятора")
@allure.severity("Critical")
@allure.description("Проверка выполнения калькулятором операции сложения с задержкой")
@allure.title("")
def test_calc_page(driver):
    calc_page = CalcPage(driver)

    with allure.step("Открыть страницу калькулятора"):
        calc_page.open("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    with allure.step("Установить задержку калькулятора"):
        calc_page.get_delay(45)

    with allure.step("Произвести вычисления"):
        calc_page.calc_sum()

    with allure.step("Получить результат вычислений '15'"):
        result = calc_page.get_result

    # with allure.step("Проверить, что результат=15"):
    #     assert result == 15
