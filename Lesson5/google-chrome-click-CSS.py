from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

# Откройте страницу http://uitestingplayground.com/classattr.
driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/classattr")

# Кликните на синюю кнопку.
search_box = driver.find_element(By.XPATH, "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]").click()

sleep(10)
driver.quit()

# Запустите скрипт три раза подряд. Убедитесь, что он отработает одинаково.