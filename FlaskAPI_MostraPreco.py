from flask import Flask, jsonify
import subprocess
from paginahtml import pghtml
from datetime import date, timedelta, datetime

app = Flask(__name__)

@app.route('/')
def home():
    return pghtml


linkMostraPreco = '/api/mostra-preco'

@app.route(linkMostraPreco, methods=['GET'])
def run_script():

    data_atual = datetime.now()

    data_atual_date = date.today()

    formato_datetime = "%d/%m/%Y"

    with open('./Data/Dados_Capturados.txt', 'r') as file:
        data_ultima_captura_str = file.readline().strip()
        data_ultima_captura = datetime.strptime(data_ultima_captura_str, '%Y-%m-%d')
        data_inicial = file.readline().replace('\n','')
        data_final = file.readline().replace('\n','')
        preco_gasolina = file.readline().replace('\n','')

    if data_atual <= (data_ultima_captura + timedelta(days=7)):
        response_data  = {
            'DataInicial' : data_inicial,
            'DataFinal' : data_final,
            'Preco' : preco_gasolina,
        }
        return jsonify(response_data)
    else:
        try:
            result = subprocess.check_output(['python', 'MostraPreco_Script.py'], stderr=subprocess.STDOUT, text=True)
            resultado_separado = result.split('\n')
            data_inicial = resultado_separado[1]
            data_final = resultado_separado[2]
            preco_gasolina = resultado_separado[0].replace(',','.')

            if resultado_separado[-3] == "1":
                response_data = {
                    'Erro' : resultado_separado[-2]
                }
            else:
                response_data  = {
                    'DataInicial' : data_inicial,
                    'DataFinal' :data_final,
                    'Preco' : preco_gasolina,

                    #'Tempo_Execucao_X' : resultado_separado[3],
                    #'Tempo_Execucao_Y' : resultado_separado[4],
                    #'YDados' : result,
                    #'ZDados' : resultado_separado
                    
                }
                with open('./Data/Dados_Capturados.txt', 'w') as file:
                    file.write(f"{data_atual_date}\n")
                    file.write(f"{data_inicial}\n")
                    file.write(f"{data_final}\n")
                    file.write(f"{preco_gasolina}\n")
            return jsonify(response_data)

        except subprocess.CalledProcessError as e:
            return jsonify(error=str(e.output))

if __name__ == '__main__':
    app.run(debug=False)