from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# Откройте страницу
driver.get("http://the-internet.herokuapp.com/inputs")

# Введите в поле текст 1000.
input_field = driver.find_element(By.TAG_NAME, 'input')
input_field.send_keys("1000")

sleep(5)

# Очистите это поле (метод clear).
input_field.clear()

sleep(5)

# Введите в это же поле текст 999.
input_field.send_keys("999")

sleep(5)

driver.quit()