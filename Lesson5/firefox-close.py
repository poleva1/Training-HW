from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    # Откройте страницу http://the-internet.herokuapp.com/entry_ad.
driver.get("http://the-internet.herokuapp.com/entry_ad")

    # Ожидание появления модального окна
WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.CSS_SELECTOR, '.modal-footer > p')) )

    # Нажатие на кнопку 'Close'
close_button = driver.find_element(By.CSS_SELECTOR, '.modal-footer > p')
for _ in range(3): # Пытаемся три раза
    try:
        close_button.click()
        break
    except ElementNotInteractableException:
        (time.sleep(1)) # Ждем перед следующей попыткой

sleep(5)
driver.quit()