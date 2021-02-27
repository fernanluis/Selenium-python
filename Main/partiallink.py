from selenium import webdriver

import time

driver = webdriver.Chrome(executable_path = "../Drivers/chromedriver.exe")
driver.get("https://www.udemy.com/join/login-popup/?locale=en_US&response_type=html&next=https%3A%2F%2Fwww.udemy.com%2F")
time.sleep(1)

# cómo acceder a 'has olvidado tu contraseña' con link parcial
link_recuperacion = driver.find_element_by_partial_link_text("Forgot")
link_recuperacion.click()

correo = driver.find_element_by_id('form-element--1')
correo.send_keys('sdasdfadsf@gmail.com')
time.sleep(5)

validar = driver.find_element_by_class_name('recaptcha-checkbox-border')

# hacer click sobre el captcha
validar.click()

boton = driver.find_element_by_class_name('btn-primary')
boton.click()

driver.quit()
