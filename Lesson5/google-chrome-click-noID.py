from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

# Откройте страницу http://uitestingplayground.com/dynamicid.
driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/dynamicid")

# Кликните на синюю кнопку
search_box = driver.find_element(By.XPATH, "//button[text()='Button with Dynamic ID']").click()

sleep(5)
driver.quit()

# Запустите скрипт три раза подряд. Убедитесь, что он отработает одинаково.

