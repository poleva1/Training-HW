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

def test_01_form(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

# Заполнение формы
    first_name = driver.find_element(By.CSS_SELECTOR, 'input[name="first-name"]')
    first_name.clear()
    first_name.send_keys("Иван")

    last_name = driver.find_element(By.CSS_SELECTOR, 'input[name="last-name"]')
    last_name.clear()
    last_name.send_keys("Петров")

    address = driver.find_element(By.CSS_SELECTOR, 'input[name="address"]')
    address.clear()
    address.send_keys("Ленина, 55-3")

    zip = driver.find_element(By.CSS_SELECTOR, 'input[name="zip-code"]')
    zip.clear()
    zip.send_keys("")

    city = driver.find_element(By.CSS_SELECTOR, 'input[name="city"]')
    city.clear()
    city.send_keys("Moscow")

    country = driver.find_element(By.CSS_SELECTOR, 'input[name="country"]')
    country.clear()
    country.send_keys("Russia")

    email = driver.find_element(By.CSS_SELECTOR, 'input[name="e-mail"]')
    email.clear()
    email.send_keys("test@skypro.com")

    phone = driver.find_element(By.CSS_SELECTOR, 'input[name="phone"]')
    phone.clear()
    phone.send_keys("+7985899998787")

    job = driver.find_element(By.CSS_SELECTOR, 'input[name="job-position"]')
    job.clear()
    job.send_keys("QA")

    company = driver.find_element(By.CSS_SELECTOR, 'input[name="company"]')
    company.clear()
    company.send_keys("SkyPro")

# Нажатие кнопки Submit
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

# Ожидание появления всех предупреждений
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".alert")))

# Получаем все элементы предупреждений
    alerts = driver.find_elements(By.CSS_SELECTOR, ".alert")

# Проходим по всем предупреждениям
    for alert in alerts:
        # Проверяем, что каждый alert имеет ожидаемый класс и отображается
        if "alert-danger" in alert.get_attribute("class"):
            assert alert.is_displayed(), "Поле Zip code не подсвечено красным."
        elif "alert-success" in alert.get_attribute("class"):
            assert alert.is_displayed(), "Не все поля подсвечены зелёным."

    print("Все проверки прошли успешно!")

# Закрытие браузера
    driver.quit()