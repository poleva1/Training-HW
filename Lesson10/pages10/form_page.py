import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FormPage:
    def __init__(self, driver):
        self.driver = driver


    @allure.step("Открытие страницы формы {url}")
    def open(self, url: str) -> None:
        self.driver.get(url)

    @allure.step("Заполнение формы {first_name} {last_name}, {address}")
    def fill_form(self, first_name: str, last_name: str, address: str, zip_code: str, city: str, country: str,
             email: str, phone: str, job_position: str, company: str) -> None:
        self.driver.find_element(By.CSS_SELECTOR, "input[name='first-name']").send_keys(first_name)
        self.driver.find_element(By.CSS_SELECTOR, "input[name='last-name']").send_keys(last_name)
        self.driver.find_element(By.CSS_SELECTOR, "input[name='address']").send_keys(address)
        #self.driver.find_element(By.CSS_SELECTOR, "input[name='zip code']").send_keys(zip_code)
        self.driver.find_element(By.CSS_SELECTOR, "input[name='city']").send_keys(city)
        self.driver.find_element(By.CSS_SELECTOR, "input[name='country']").send_keys(country)
        self.driver.find_element(By.CSS_SELECTOR, "input[name='e-mail']").send_keys(email)
        self.driver.find_element(By.CSS_SELECTOR, "input[name='phone']").send_keys(phone)
        self.driver.find_element(By.CSS_SELECTOR, "input[name='job-position']").send_keys(job_position)
        self.driver.find_element(By.CSS_SELECTOR, "input[name='company']").send_keys(company)

    @allure.step("Отправка формы")
    def submit_form(self) -> None:
        submit = self.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    @allure.step("Ожидание появления всех предупреждений")
    def wait_for_alerts(self) -> None:
        WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".alert")))

    @allure.step("Получение всех элементов предупреждений")
    def get_alerts(self) -> None:
        alerts = self.driver.find_elements(By.CSS_SELECTOR, ".alert")

    def find_fields(self):
         self.fields = {
            "first_name": (By.ID, "first-name"),
            "last_name": (By.ID, "last-name"),
           "address": (By.ID, "address"),
        "email": (By.ID, "e-mail"),
        "phone": (By.ID, "phone"),
        "zip_code": (By.ID, "zip-code"),
        "city": (By.ID, "city"),
        "country": (By.ID, "country"),
        "job_position": (By.ID, "job-position"),
        "company": (By.ID, "company")
    }


    def get_class(self, field_name):
        locator = self.fields[field_name]
        self.driver.find_element(*locator)
        return self.driver.find_element(*locator).get_attribute("class")