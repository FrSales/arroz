import requests

# Enviando a requisição POST para o servidor
response = requests.post("https://frsales.pythonanywhere.com/", json={
    "arroz_inicial": 10000,
    "arroz_final": 10000,
    "entradas_arroz": 65000,
    "casca_inicial": 5000,
    "casca_final": 5000,
    "saidas_casca": 14000,
    "pallet_farelo_inicial": 10,
    "pallet_farelo_final": 20,
    "contagem_estoquista_farelo": 200,
    "bag_quirela_inicial": 0,
    "bag_quirela_final": 500,
    "contagem_estoquista_quirela": 3200
})

if response.status_code == 200:
    dados_relatorio = response.json()   # resposta JSON

    # Acessando o relatório como texto
    relatorio = dados_relatorio.get('relatorio', '')
    
    print(relatorio)

else:
    print(f"Erro na requisição. Status code: {response.status_code}")
