from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# Откройте страницу
driver.get("http://the-internet.herokuapp.com/login")

# В поле username введите значение tomsmith.
#input_field = driver.find_element(By.TAG_NAME, 'input')
username_field = driver.find_element(By.ID, 'username')
username_field.send_keys('tomsmith')

sleep(5)

# В поле password введите значение SuperSecretPassword!
password_field = driver.find_element(By.ID, 'password')
password_field.send_keys('SuperSecretPassword!')

sleep(5)

# Нажмите кнопку Login
login_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
login_button.click()

sleep(5)

driver.quit()