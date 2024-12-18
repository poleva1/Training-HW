import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalcPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открытие страницы калькулятора {url}")
    def open(self, url: str) -> None:
        self.driver.get(url)

    @allure.step("Установка задержки на 45 сек {delay}")
    def get_delay(self, delay: int) -> None:
        delay_field = self.driver.find_element(By.ID, "delay")
        delay_field.clear()
        delay_field.send_keys("45")

    @allure.step("Сложение 7 и 8")
    def calc_sum(self) -> None:
        self.driver.find_element(By.XPATH, "//span[text()='7']").click()
        self.driver.find_element(By.XPATH, "//span[text()='+']").click()
        self.driver.find_element(By.XPATH, "//span[text()='8']").click()
        self.driver.find_element(By.XPATH, "//span[text()='=']").click()

    @allure.step("Ожидание и получение результата") #{result}
    def get_result(self) -> str:
        WebDriverWait(self.driver, 60).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, "screen"), "15")
        )
        return self.driver.find_element(By.CSS_SELECTOR, "screen").text
