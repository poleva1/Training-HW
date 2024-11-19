from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FormPage:

    def __init__(self, driver):
        self._driver = driver

    def form_filling(self):
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="first-name"]').send_keys("Иван")
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="last-name"]').send_keys("Петров")
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="address"]').send_keys("Ленина, 55-3")
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="zip-code"]').send_keys("")
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="city"]').send_keys("Moscow")
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="country"]').send_keys("Russia")
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="e-mail"]').send_keys("test@skypro.com")
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="phone"]').send_keys("+7985899998787")
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="job-position"]').send_keys("QA")
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="company"]').send_keys("SkyPro")

    def form_submit(self):
        submit_button = WebDriverWait(self._driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
        submit_button.click()

    def form_asserting(self):
        assert 'alert-danger' in self._driver.find_element(By.CSS_SELECTOR, '#zip-code').get_attribute("class")
        assert 'success' in self._driver.find_element(By.CSS_SELECTOR, '#first-name').get_attribute("class")
        assert 'success' in self._driver.find_element(By.CSS_SELECTOR, '#last-name').get_attribute("class")
        assert 'success' in self._driver.find_element(By.CSS_SELECTOR, '#address').get_attribute("class")
        assert 'success' in self._driver.find_element(By.CSS_SELECTOR, '#e-mail').get_attribute("class")
        assert 'success' in self._driver.find_element(By.CSS_SELECTOR, '#phone').get_attribute("class")
        assert 'success' in self._driver.find_element(By.CSS_SELECTOR, '#city').get_attribute("class")