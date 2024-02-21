from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import date, timedelta, datetime
import time
import Conecta_Driver as cd

inicio_tempoY = time.time()

erro = 0
erro_texto = "Ok"

try:
    xpathbotaoAceitaCookies = "//button[@id='onetrust-reject-all-handler']"
    botaoAceitaCookies = WebDriverWait(cd.driver, 40).until(
        EC.element_to_be_clickable((By.XPATH, xpathbotaoAceitaCookies))
    )
    botaoAceitaCookies.click()
except:
    pass

try:
    xpathbotaoVerPreco = "//div[@id='botao-finalizador' and @data-lfr-editable-id='Ver formação de preço' and @data-lfr-editable-type='text']"
    botaoVerPreco = WebDriverWait(cd.driver, 40).until(
        EC.element_to_be_clickable((By.XPATH, xpathbotaoVerPreco))
    )
    botaoVerPreco.click()
except:
    erro = 1
    erro_texto = 'Nao encontrado o botao finalizador'
    
time.sleep(1)

try:
    xpathPrecoGasolina = "//p[contains(@class, 'real-value') and contains(@data-lfr-editable-type, 'text') and contains(@data-lfr-editable-id, 'telafinal-precofinal') and @id='telafinal-precofinal']"
    precoGasolina = WebDriverWait(cd.driver, 40).until(
        EC.presence_of_element_located((By.XPATH, xpathPrecoGasolina))
    )
    print(precoGasolina.text)
except:
    erro = 1
    erro_texto = 'Nao encontrado o preco da Gasolina'

try:
    xpathPeriodoDeColeta = "//span[@data-lfr-editable-type='text' and @data-lfr-editable-id='telafinal-textoColeta']"

    periodoDeColeta = WebDriverWait(cd.driver, 40).until(
        EC.presence_of_element_located((By.XPATH, xpathPeriodoDeColeta))
    )
    data_formatada = '%d/%m/%Y'

    tratamentoPeriodoColeta = periodoDeColeta.text.replace(" ", "").split("a")
    periodoInicial = tratamentoPeriodoColeta[0]
    periodoFinal = tratamentoPeriodoColeta[1]
    datetimePeriodoInicial = datetime.strptime(periodoInicial, data_formatada)
    datetimePeriodoFinal = datetime.strptime(periodoFinal, data_formatada)
    periodoInicialmil = int(datetimePeriodoInicial.timestamp() * 1000)
    periodoFinalmil = int(datetimePeriodoFinal.timestamp() * 1000)
    print(periodoInicialmil)
    print(periodoFinalmil)
except:
    erro = 1
    erro_texto = 'Nao encontrado o periodo de coleta'

fim_tempo = time.time()
tempo_execucao = round(fim_tempo - cd.inicio_tempo)
tempo_execucaoY = round(fim_tempo - inicio_tempoY)
print(f'{tempo_execucao} seg')
print(f'{tempo_execucaoY} seg')
print(erro)
print(erro_texto)

    

