from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

# Откройте страницу http://the-internet.herokuapp.com/add_remove_elements/.
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

# Пять раз кликните на кнопку Add Element
search_box = driver.find_element(By.XPATH, "//button[text()='Add Element']").click()
search_box = driver.find_element(By.XPATH, "//button[text()='Add Element']").click()
search_box = driver.find_element(By.XPATH, "//button[text()='Add Element']").click()
search_box = driver.find_element(By.XPATH, "//button[text()='Add Element']").click()
search_box = driver.find_element(By.XPATH, "//button[text()='Add Element']").click()

# еще вариант
# for _ in range(5):
    # driver.find_element(By.XPATH, "//button[text()='Add Element']").click()

# Соберите со страницы список кнопок Delete
buttons = driver.find_elements(By.XPATH, "//button[text()='Delete']")
print(len(buttons))

# Выведите на экран размер списка
for button in buttons:
    button = button.find_element(By.XPATH, "//button[text()='Delete']").text
    print(button)

# еще вариант
# print(f"Количество кнопок Delete: {len(buttons)}")
# for button in buttons:
   # print(button.text)

sleep(5)
driver.quit()
