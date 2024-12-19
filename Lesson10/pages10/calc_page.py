import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalcPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открытие страницы калькулятора")
    def open(self, url: str) -> None:
        self.driver.get(url)

    @allure.step("Установка задержки на 45 сек")
    def get_delay(self, delay: int) -> None:
        delay_field = self.driver.find_element(By.ID, "delay")
        delay_field.clear()
        delay_field.send_keys(delay)

    @allure.step("Сложение 7 и 8")
    def calc_sum(self) -> None:
        self.driver.find_element(By.XPATH, "//span[text()='7']").click()
        self.driver.find_element(By.XPATH, "//span[text()='+']").click()
        self.driver.find_element(By.XPATH, "//span[text()='8']").click()
        self.driver.find_element(By.XPATH, "//span[text()='=']").click()

    def wait_result(self, delay, result):
        waiter = WebDriverWait(self.driver, delay + 1)
        waiter.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.screen'), str(result)))

    @allure.step("Ожидание и получение результата")
    def result_text(self):
        result = self.driver.find_element(By.CSS_SELECTOR, '.screen')
        return result.text
