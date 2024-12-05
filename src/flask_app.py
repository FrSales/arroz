from flask import Flask, request, jsonify
from a import main

app = Flask(__name__)

@app.route('/', methods=['POST'])
def gerar_relatorio():
    dados = request.get_json()
    if not dados:
        return jsonify({"error": "No data provided"}), 400

    try:
        arroz_inicial = dados['arroz_inicial']
        arroz_final = dados['arroz_final']
        entradas_arroz = dados['entradas_arroz']
        casca_inicial = dados['casca_inicial']
        casca_final = dados['casca_final']
        saidas_casca = dados['saidas_casca']
        pallet_farelo_inicial = dados['pallet_farelo_inicial']
        pallet_farelo_final = dados['pallet_farelo_final']
        contagem_estoquista_farelo = dados['contagem_estoquista_farelo']
        bag_quirela_inicial = dados['bag_quirela_inicial']
        bag_quirela_final = dados['bag_quirela_final']
        contagem_estoquista_quirela = dados['contagem_estoquista_quirela']
    except KeyError as e:
        return jsonify({"error": f"Missing field: {e}"}), 400

    resultado = main(
        arroz_inicial, arroz_final, entradas_arroz,
        casca_inicial, casca_final, saidas_casca,
        pallet_farelo_inicial, pallet_farelo_final, contagem_estoquista_farelo,
        bag_quirela_inicial, bag_quirela_final, contagem_estoquista_quirela
    )

    return jsonify({"relatorio": resultado})

if __name__ == "__main__":
    app.run()
