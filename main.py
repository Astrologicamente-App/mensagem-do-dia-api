from mensagem_do_dia import request_mensagem_do_dia, escolhe_bicho
from flask import Flask, jsonify, request
from pyngrok import ngrok

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/api/mensagem-do-dia', methods=['GET'])
def mensagem_do_dia():
    data_de_nascimento = request.args.get('data_nascimento')

    if data_de_nascimento:
        mensagem = request_mensagem_do_dia(data_nascimento=data_de_nascimento)
        return mensagem
    else:
        return "Por favor, forneça a data de nascimento como parâmetro na URL."


@app.route('/api/bicho-da-sorte', methods=['GET'])
def bicho_da_sorte():
    data_de_nascimento = request.args.get('data_nascimento')

    if data_de_nascimento:
        bicho = escolhe_bicho(data_nascimento=data_de_nascimento)
        return bicho
    else:
        return "Por favor, forneça a data de nascimento como parâmetro na URL."


if __name__ == "__main__":
	app.run(host='0.0.0.0')