import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.FormPage import FormPage

# Фикстура для создания WebDriver
@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    yield driver
    driver.quit()

def test_form(driver):
    form = FormPage(driver)
    form.form_filling()
    form.form_submit()
    form.form_asserting()

    driver.quit()