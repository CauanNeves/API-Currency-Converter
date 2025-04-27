from flask import Flask, request, jsonify
import requests

#Iniciando
app = Flask(__name__)

API_KEY= 'SUA_CHAVE_DE_API_AQUI'

#Função para buscar a taxa de câmbio
def get_exchange_rate(from_currency, to_currency):
    url= f'https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{from_currency}'
    
    response= requests.get(url= url) #Requisição HTTP
    data= response.json()
    
    try:
        if response.status_code == 200:
            rate= data['conversion_rates'].get(to_currency)
            if rate:
                return rate
            else:
                return None
        else:
            return None
    except Exception as e:
        print(f'Erro ao acessar a API: {e}')
        return None

#Rota de Conversão
@app.route('/convert', methods= ['GET'])
def convert_currency():
    from_currency= request.args.get('from')
    to_currency= request.args.get('to')
    amount= request.args.get('amount')
    
    #Lógica de conversão
    if not from_currency or not to_currency or not amount:
        return jsonify({
            'message': 'Parâmetros inválidos. "from", "to" e "amount" são obrigatórios.'
        })
    
    rate= get_exchange_rate(from_currency, to_currency)
    if rate:
        converted_amount= float(amount) * rate
        return jsonify({
            'from': from_currency,
            'to': to_currency,
            'amount': amount,
            'converted_amount': converted_amount,
            'rate': rate
        }, 200)
    else:
        return jsonify({
            'error': 'Não foi possível obter a taxa de câmbio'
        }, 500)

#Rota taxa de conversão
@app.route('/rate', methods= ['GET'])
def get_rate():
    from_currency= request.args.get('from')
    to_currency= request.args.get('to')
    
    #Lógica pra mostrar a taxa de câmbio
    if not from_currency or not to_currency:
        return jsonify({
            'message': 'Parâmetros inválidos. "from" e "to" são obrigatórios.'
        })
    
    rate= get_exchange_rate(from_currency, to_currency)
    if rate:
        return jsonify({
            'from': from_currency,
            'to': to_currency,
            'rate': rate
        }, 200)
    else:
        return jsonify({
            'erro': 'Não foi possível obter a taxa de câmbio'
        }, 500)
        
    
    
#rota lista de moeda
@app.route('/currencies', methods= ['GET'])
def list_currencies():
    
    #Lógica de listar as moedas
    url= f'https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD'
    response= requests.get(url)
    
    if response.status_code == 200:
        data= response.json()
        currencies= list(data['conversion_rates'].keys())
        return jsonify({
            'curriencies': currencies    
        }, 200)
    else:
        return jsonify({
            'error':'Não foi possível obter lista de moedas.'
        }, 500)
            
    
if __name__ == '__main__':
    app.run(port= 5000, debug= True, host= 'localhost')