from flask import Flask, request, jsonify

#Iniciando
app = Flask(__name__)

#Rota de Conversão
@app.route('/convert', methods= ['GET'])
def convert_currency():
    from_currency= request.args.get('from')
    to_currency= request.args.get('to')
    amount= request.args.get('amount')
    
    #Lógica de conversão
    
    return jsonify({
        'message':'Conversão ainda não implementada'
    })

#Rota taxa de conversão
@app.route('/rate', methods= ['GET'])
def get_rate():
    from_currency= request.args.get('from')
    to_currency= request.args.get('to')
    
    #Lógica pra mostrar a taxa de câmbio
    
    return jsonify({
        'message': 'Taxa de câmbio ainda não implementada'
    })
    
#rota lista de moeda
@app.route('/currencies', methods= ['GET'])
def list_currencies():
    
    #Lógica de listar as moedas
    
    return jsonify({
        'message':'Lista de moedas ainda não implementada'
    })
    
if __name__ == '__main__':
    app.run(port= 5000, debug= True, host= 'localhost')