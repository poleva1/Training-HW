import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from Lesson10.pages10.form_page import FormPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()

@allure.epic("Заполнение формы онлайн")
@allure.severity("Critical")
@allure.description("Проверка заполнения онлайн формы с условием отсуствия некоторых данных")
@allure.title("Проверка отправки формы с незаполненным полем")
def test_form(driver):
    form_page = FormPage(driver)

    with allure.step("Открыть страницу формы"):
        form_page.open("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    with allure.step("Заполнить форму"):
        form_page.fill_form(
            first_name='Иван',
            last_name='Петров',
            address='Ленина, 55-3',
            zip_code='',
            city='Москва',
            country='Россия',
            email='test@skypro.com',
            phone='+7985899998787',
            job_position='QA',
            company='SkyPro')

    with allure.step("Отправить форму"):
        form_page.submit_form()

    with allure.step("Ожидание появления предупреждений"):
        form_page.wait_for_alerts()
        form_page.get_alerts()


        form_page.find_fields()
        # Удостоверяемся, что в классах есть ожидаемый результат
        assert "success" in form_page.get_class("first_name")
        assert "success" in form_page.get_class("last_name")
        assert "success" in form_page.get_class("address")
        assert "success" in form_page.get_class("email")
        assert "success" in form_page.get_class("phone")
        assert "success" in form_page.get_class("city")
        assert "success" in form_page.get_class("country")
        assert "success" in form_page.get_class("job_position")
        assert "success" in form_page.get_class("company")
        assert "danger" in form_page.get_class("zip_code")