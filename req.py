import requests

# Enviando a requisição POST para o servidor
response = requests.post("https://frsales.pythonanywhere.com/", json={
    "arroz_inicial": 10000,
    "arroz_final": 22000,
    "entradas_arroz": 75000,
    "casca_inicial": 7000,
    "casca_final": 9000,
    "saidas_casca": 13000,
    "pallet_farelo_inicial": 10,
    "pallet_farelo_final": 20,
    "contagem_estoquista_farelo": 200,
    "bag_quirela_inicial": 800,
    "bag_quirela_final": 0,
    "contagem_estoquista_quirela": 4800
})

if response.status_code == 200:
    dados_relatorio = response.json()  # A resposta JSON

    # Acessando o relatório como texto
    relatorio = dados_relatorio.get('relatorio', '')
    
    print(relatorio)

else:
    print(f"Erro na requisição. Status code: {response.status_code}")
