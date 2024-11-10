from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(20)
driver.get("http://uitestingplayground.com/textinput")

# Введите в поле текст SkyPro.
input_field = driver.find_element(By.TAG_NAME, 'input')
input_field.send_keys("SkyPro")

# Нажатие на синюю кнопку
click = driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()

# Ожидание появления текста на синей кнопке
blue_button = WebDriverWait(driver, 25).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#updatingButton"))
)

# Получение текста и вывод в консоль
print(blue_button.text)

# Закрытие браузера
driver.quit()