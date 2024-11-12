import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

from Lesson2.Lesson2_if import password


# Фикстура для создания WebDriver
@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()

# Открытие страницы
def test_03_shop(driver):
    driver.get("https://www.saucedemo.com/")

    driver.maximize_window()

# Авторизация
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

# Добавьте в корзину товары
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-backpack']"))
    ).click()
    driver.find_element(By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-bolt-t-shirt']").click()
    driver.find_element(By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-onesie']").click()

# Перейти в корзину
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

# Нажмите Checkout
    driver.find_element(By.ID, "checkout").click()

# Заполните форму своими данными (имя, фамилия, индекс) и нажмите кнопку Continue
    driver.find_element(By.ID, "first-name").send_keys("Имя")
    driver.find_element(By.ID, "last-name").send_keys("Фамилия")
    driver.find_element(By.ID, "postal-code").send_keys("123456")
    driver.find_element(By.ID, "continue").click()

# Прочитайте со страницы итоговую стоимость (Total).
    total = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
    )
    total = driver.find_element(By.CLASS_NAME, "summary_total_label").text

# Вывод итоговой стоимости в консоль
    print(f"Итоговая стоимость: {total}")

# Проверьте, что итоговая сумма равна $58.29
    assert total == "Total: $58.29", f"Итоговая сумма не равна $58.29, а равна {total}"
    print("Итоговая сумма проверена успешно.")

# Закройте браузер.
    driver.quit()