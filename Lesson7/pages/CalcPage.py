from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalcPage:

    def __init__(self, driver):
        self._driver = driver

    def set_delay(self, delay):
        #delay = self._driver.find_element(By.ID, "delay").send_keys("45")
        delay = self._driver.find_element(By.ID, "delay")
        delay.clear()
        delay.send_keys("45")

    def calculate_sum(self):
        self._driver.find_element(By.XPATH, "//span[text()='7']").click()
        self._driver.find_element(By.XPATH, "//span[text()='+']").click()
        self._driver.find_element(By.XPATH, "//span[text()='8']").click()
        self._driver.find_element(By.XPATH, "//span[text()='=']").click()

    def get_result(self):
        result = WebDriverWait(self._driver, 60).until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
        )
        result_text = self._driver.find_element(By.CSS_SELECTOR, ".screen").text
        return result_text
