from selenium import webdriver
# selenium es la API
# webdriver es una implementación que permite conectar a selenium con el drive del navegador
import time

# variable con instruciones para ejeuctar
controlador = webdriver.Chrome(executable_path = '../Drivers/chromedriver.exe')
# executable_path da la ruta de donde está e drive ejecutable para ejecutar la prueba

# dar el link a testear
controlador.get("https://www.udemy.com/join/login-popup/?locale=en_US&response_type=html&next=https%3A%2F%2Fwww.udemy.com%2F")
time.sleep(1)


# como acceder a un componente de una aplicación web. Instanciar componentes
usuario = controlador.find_element_by_id("email--1")
clave = controlador.find_element_by_id("id_password")
time.sleep(1)

# enviar claves
usuario.send_keys("sdasdfadsf@gmail.com")
time.sleep(5)

clave.send_keys("2531251345")
time.sleep(5)

# crear instancia del botón
boton = controlador.find_element_by_id("submit-id-submit")

# método click
boton.click()
time.sleep(5)
#finalizar
controlador.quit()
