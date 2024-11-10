from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("http://uitestingplayground.com/ajax")

# Нажатие на синюю кнопку
click = driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()

# Ожидание появления текста на зеленой плашке
green_banner = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'div#content > p.bg-success'))
)

# Получение текста из зеленой плашки и вывод в консоль
print(green_banner.text)

# Закрытие браузера
driver.quit()