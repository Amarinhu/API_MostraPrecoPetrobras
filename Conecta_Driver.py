from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

inicio_tempo = time.time()

try:
    chrome_driver_path = "./ChromeDriver/chromedriver.exe"

    chrome_options = Options()
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--blink-settings=imagesEnabled=false')
    chrome_options.add_argument('--disable-gpu')
    #chrome_options.add_experimental_option( "prefs",{'profile.managed_default_content_settings.javascript': 2})
    chrome_service = Service(executable_path=chrome_driver_path)


    chrome_service = Service(chrome_driver_path)

    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    driver.set_window_size(1100, 800)

    driver.get("https://precos.petrobras.com.br/web/precos-dos-combustiveis/w/gasolina/df")

except:
    erro_texto = 'Houve um erro na conexão ou parametrização do WebDriver'
