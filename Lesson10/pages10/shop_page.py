import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ShopPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открытие страницы магазина {url}")
    def open(self, url: str) -> None:
        self.driver.get(url)

    @allure.step("Авторизация на странице")
    def get_authorisation(self) -> None:
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()

    @allure.step("Добавление товаров в корзину")
    def add_to_cart(self) -> None:
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-backpack']"))
        ).click()
        self.driver.find_element(By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-bolt-t-shirt']").click()
        self.driver.find_element(By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-onesie']").click()

    @allure.step("Переход в корзину")
    def get_to_cart(self) -> None:
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    @allure.step("Нажмите Checkout")
    def click_checkout(self) -> None:
        self.driver.find_element(By.ID, "checkout").click()

    @allure.step("Заполнение формы своими данными. Нажмите кнопку Continue")
    def add_checkout_data(self) -> None:
        self.driver.find_element(By.ID, "first-name").send_keys("Имя")
        self.driver.find_element(By.ID, "last-name").send_keys("Фамилия")
        self.driver.find_element(By.ID, "postal-code").send_keys("123456")
        self.driver.find_element(By.ID, "continue").click()

    @allure.step("Получение итоговой стоимости заказа")
    def get_total(self) -> set:
        total = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
        )
        total = self.driver.find_element(By.CLASS_NAME, "summary_total_label").text
        return total