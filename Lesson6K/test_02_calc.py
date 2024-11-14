import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Фикстура для создания WebDriver
@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()

# Открытие страницы
def test_02_calc(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    driver.maximize_window()

    delay_field = driver.find_element(By.ID, "delay")
    delay_field.clear()
    delay_field.send_keys("45")

# Нажатие на кнопки 7, +, 8, =
    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()

# Ожидание результата 15 через 45 секунд
    result = WebDriverWait(driver, 60).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
)

# Проверка (assert), что результат 15
    assert result, "Результат не равен 15"
    print("Результат отображен правильно: 15")

# Закрытие браузера
    driver.quit()