from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ShopPage:

    def __init__(self, driver):
        self._driver = driver

    def authorisation(self, username, password):
        self._driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self._driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self._driver.find_element(By.ID, "login-button").click()

    def add_to_cart(self):
        WebDriverWait(self._driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-backpack']"))
        ).click()
        self._driver.find_element(By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-bolt-t-shirt']").click()
        self._driver.find_element(By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-onesie']").click()

    def go_to_cart(self):
        self._driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    def checkout(self):
        self._driver.find_element(By.ID, "checkout").click()

    def fill_form(self, first_name, last_name, postal_code):
        self._driver.find_element(By.ID, "first-name").send_keys("Имя")
        self._driver.find_element(By.ID, "last-name").send_keys("Фамилия")
        self._driver.find_element(By.ID, "postal-code").send_keys("123456")
        self._driver.find_element(By.ID, "continue").click()

    def get_total(self):
        total = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
        )
        total = self._driver.find_element(By.CLASS_NAME, "summary_total_label").text
        return total
