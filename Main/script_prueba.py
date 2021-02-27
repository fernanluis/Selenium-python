# llamar módulo seleniume importar webdriver
from selenium import webdriver
# webdriver es una implementación que trae selenium y que permite crear una instancia
# para conectarse con el navegador pero a partir de uno de esots 2 drivers, es decir,
# a partir de un drivers de navegador.

# variable que tiene como contenido o valor el driver chromedriver
driver = webdriver.Chrome(executable_path = '../Drivers/chromedriver.exe')

# ver método para linux, este parece ser sólo para windows
#driver.maximize_linux() # método para maximizar la ventana una vez abierta en el navegador

# método get que permite redireccionar a la URL a la cual se desea redireccionar
driver.get("https://www.udemy.com/?utm_source=adwords-brand&utm_medium=udemyads&utm_campaign=NEW-AW-PROS-Branded-Search-SP-SPA_._ci__._sl_SPA_._vi__._sd_All_._la_SP_._&tabei=7&utm_term=_._ag_53604040718_._ad_254061738919_._de_c_._dm__._pl__._ti_kwd-310556426868_._li_1000112_._pd__._&gclid=Cj0KCQiA-OeBBhDiARIsADyBcE4UAngEEzH_DeALNJeJsO9fDBUazAAfCyVfXFITdt-N2UdeM0yqYIcaAtFLEALw_wcB")

# otro método de Selenium permita cerrar la instancia
driver.close()
