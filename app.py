from flask import Flask, render_template, request, redirect, url_for
import datetime
import json
import os

app = Flask(__name__)

# Caminho para o arquivo que armazenará os dados dos clientes
DATABASE_PATH = 'clientes.json'

# Função para carregar dados dos clientes
def carregar_dados():
    if os.path.exists(DATABASE_PATH):
        with open(DATABASE_PATH, 'r') as file:
            return json.load(file)
    return {}

# Função para salvar dados dos clientes
def salvar_dados(dados):
    with open(DATABASE_PATH, 'w') as file:
        json.dump(dados, file, indent=4)

# Função para gerar o romaneio
def gerar_romaneio(dados):
    romaneio = f"Romaneio gerado em {datetime.datetime.now()}\n"
    for item in dados['itens']:
        romaneio += f"{item['produto']} - Quantidade: {item['quantidade']}\n"
    return romaneio

@app.route('/', methods=['GET', 'POST'])
def index():
    clientes = carregar_dados()
    if request.method == 'POST':
        nome_cliente = request.form['nome']
        produtos = request.form.getlist('produto')
        quantidades = request.form.getlist('quantidade')

        dados_cliente = {
            'nome': nome_cliente,
            'itens': [{'produto': prod, 'quantidade': qt} for prod, qt in zip(produtos, quantidades)]
        }

        # Salvar ou atualizar os dados do cliente
        clientes[nome_cliente] = dados_cliente
        salvar_dados(clientes)

        romaneio = gerar_romaneio(dados_cliente)

        return render_template('romaneio.html', romaneio=romaneio)
    
    return render_template('index.html', clientes=clientes)

if __name__ == '__main__':
    app.run(debug=True)
