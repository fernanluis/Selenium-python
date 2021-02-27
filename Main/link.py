from selenium import webdriver

import time

driver = webdriver.Chrome(executable_path = "../Drivers/chromedriver.exe")
driver.get("https://www.udemy.com/join/login-popup/?locale=en_US&response_type=html&next=https%3A%2F%2Fwww.udemy.com%2F")
time.sleep(1)

# cómo acceder a 'has olvidado tu contraseña'
link_recuperacion = driver.find_element_by_link_text("Forgot Password")
link_recuperacion.click()

driver.quit()
