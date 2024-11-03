from funcs import *

print (f"""\n*Relatório de produção:*
- Início do descasque: 07:15
- Fim: 17:05
- Observações: 
- Quantidade descascada: {descasque(int(input("Arroz inicial:")), int(input("Arroz final:")), int(input("Entradas arroz:")))} kg
- Casca gerada: {casca(int(input("Casca inicial:")), int(input("Casca final:")), int(input("Saídas casca:")))} kg
- Farelo gerado: {farelo(int(input("Pallet farelo inicial:")), int(input("Pallet farelo final:")), int(input("Contagem estoquista:")))} kg
- Quirela gerada: {quirela(int(input("Bag quirela inicial:")), int(input("Bag quirela final:")), int(input("Contagem estoquista:")))} kg\n""")