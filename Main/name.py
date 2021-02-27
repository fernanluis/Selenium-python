from selenium import webdriver

import time

controlador = webdriver.Chrome(executable_path = '../Drivers/chromedriver.exe')

controlador.get("https://www.udemy.com/join/login-popup/?locale=en_US&response_type=html&next=https%3A%2F%2Fwww.udemy.com%2F")
time.sleep(1)

usuario = controlador.find_element_by_name("email")
clave = controlador.find_element_by_name("password")
time.sleep(1)

usuario.send_keys("sdasdfadsf@gmail.com")
time.sleep(5)

clave.send_keys("2531251345")
time.sleep(5)

boton = controlador.find_element_by_name("submit")

# método click
boton.click()
time.sleep(5)
#finalizar
controlador.quit()
