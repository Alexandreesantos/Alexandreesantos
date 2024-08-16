from flask import Flask, render_template, request, redirect, url_for
import datetime

app = Flask(__name__)

# Função para gerar o romaneio
def gerar_romaneio(dados):
    romaneio = f"Romaneio gerado em {datetime.datetime.now()}\n"
    for item in dados:
        romaneio += f"{item['produto']} - Quantidade: {item['quantidade']}\n"
    return romaneio

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        produtos = request.form.getlist('produto')
        quantidades = request.form.getlist('quantidade')

        dados = [{'produto': prod, 'quantidade': qt} for prod, qt in zip(produtos, quantidades)]

        romaneio = gerar_romaneio(dados)

        return render_template('romaneio.html', romaneio=romaneio)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
