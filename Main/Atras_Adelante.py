from selenium import webdriver

import time

driver = webdriver.Chrome(executable_path = "../Drivers/chromedriver.exe")
time.sleep(1)

driver.get("https://sites.google.com/a/chromium.org/chromedriver/")
time.sleep(5)

# abrir una nueva pestaña
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])
time.sleep(5)

driver.get("https://chromedriver.storage.googleapis.com/index.html?path=88.0.4324.96/")
time.sleep(5)

driver.get('https://github.com/fernanluis/Selenium-python')
time.sleep(5)

driver.execute_script("window.open('');")
driver.get("https://www.w3schools.com/xml/xpath_intro.asp")
driver.get("https://www.udemy.com/course/testing-debugging-software-completo-walter-coto-alvaro-chirou/learn/lecture/25130082#notes")

# regresar atrás
driver.back()

# redireccionar a una pestaña
driver.switch_to.window(driver.window_handles[1])
driver.back()

driver.switch_to.window(driver.window_handles[0])
driver.close()
driver.close()

# hacia adelante
driver.forward()

driver.quit()
