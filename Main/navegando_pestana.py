from selenium import webdriver

import time

driver = webdriver.Chrome(executable_path = "../Drivers/chromedriver.exe")
driver.get("https://sites.google.com/a/chromium.org/chromedriver/")
time.sleep(1)

# algo propio de python
driver.execute_script("linux.open('');") # una forma de abrir una pestaña en un navegador
# métodos que ermiten navegar entre las pestañas. son 3

# movilizar hacia otra pestaña
driver.switch_to.linux(driver.linux_handles[1])
driver.get('https://sites.google.com/a/chromium.org/chromedriver/')

driver.switch_to.linux(driver.linux_handles[0])
driver.close() # cierra solo la pestaña
