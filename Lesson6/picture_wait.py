from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# Открытие страницы
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
driver.maximize_window()
waiter = WebDriverWait(driver, 30)

# Ожидание загрузки всех картинок
waiter.until(
    EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "#landscape"))
)

# Получение значения атрибута src у 3-й картинки
third_picture = driver.find_element(By.CSS_SELECTOR,"#award").get_attribute("src")

# Вывод значения в консоль
print(f"Значение атрибута src у 3-й картинки: {third_picture}")

# Закрытие браузера
driver.quit()