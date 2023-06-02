from flask import Flask, render_template, jsonify, request
from datetime import datetime

app = Flask(__name__)

AGENDA = {}
ANO_ATUAL = datetime.now().year

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route("/<nome>")
def index_parametro_rota(nome):
    return "Olá {}".format(nome.title()), 200

@app.route("/index/")
def index_parametro_query():
    nome = request.args.get('nome')
    return "Olá {}".format(nome.title()), 200

@app.route("/cadastrar/")
def cadastrar():
    nome = request.args.get('nome')
    telefone = request.args.get('telefone')
    nascimento = request.args.get('nascimento')
    signo = request.args.get('signo')

    if nome and telefone and signo and signo:
        AGENDA[nome] = {'telefone': telefone,
                        'nascimento': nascimento,
                        'signo': signo
        }
        msg = 'Cadastro realizado com sucesso!'
        status = 200
    else:
        msg = 'Informações incompletas! Por favor, informe: nome, telefone, ano nascimento, signo.'
        status = 400

    return msg, status

@app.route("/lista/<nome>")
def listar_telefones(nome):
    status = 404
    resposta = {}

    if contato_existe(nome):
        resposta[nome] = AGENDA.get(nome)
        status = 200
    
    return jsonify(contatos=resposta, total=len(resposta)), status

@app.route("/lista/completa/")
def listar_agenda():
    agenda_temp = {}

    for chave in AGENDA.keys():
        agenda_temp[chave] = AGENDA.get(chave)
        nascimento = AGENDA.get(chave).get('nascimento')
        agenda_temp[chave]['idade'] = ANO_ATUAL - int(nascimento)

    return jsonify(contatos=agenda_temp, total=len(agenda_temp)), 200
    

def contato_existe(nome):
    if AGENDA.get(nome) is None:
        return False
    
    return True


if __name__ == '__main__':
    app.run(debug=True)