# Librerias
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# Configuración de la navegación
opciones = webdriver.ChromeOptions()
opciones.add_argument('--user-data-dir=C:/sesion')
opciones.add_experimental_option('excludeSwitches', ['enable-logging'])
service = Service(executable_path='C:/chromedriver.exe')
navegacion = webdriver.Chrome(service = service, options = opciones)
url_whatsapp_base = "https://web.whatsapp.com/send/?type=phone_number&app_absent=0"

def wa_login():
    print("---")
    print("WA: Iniciando sesión")
    navegacion.get(url_whatsapp_base)
    time.sleep(5)
    navegacion.save_screenshot('captura.png')
    time.sleep(55)
    print("WA: Iniciando sesión")

wa_login()