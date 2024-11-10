from funcs import *

arroz_descascado = descasque(int(input("Arroz inicial:")), int(input("Arroz final:")), int(input("Entradas arroz:")))
casca_gerada = casca(int(input("Casca inicial:")), int(input("Casca final:")), int(input("Saídas casca:")))
farelo_gerado = farelo(int(input("Pallet farelo inicial:")), int(input("Pallet farelo final:")), int(input("Contagem estoquista:")))
quirela_gerada = quirela(int(input("Bag quirela inicial:")), int(input("Bag quirela final:")), int(input("Contagem estoquista:")))

percentual_casca_arroz = (casca_gerada * 100) / arroz_descascado
percentual_farelo_arroz = (farelo_gerado * 100) / arroz_descascado
percentual_quirela_arroz = (quirela_gerada * 100) / arroz_descascado

print (f"""\n*Relatório de produção:*
- Início do descasque: 07:15
- Fim: 17:05
- Observações:
- Quantidade descascada: {f"{arroz_descascado:,}".replace(",", ".")} kg
- Casca gerada: {f"{casca_gerada:,}".replace(",", ".")} kg ({"{:.2f}".format(percentual_casca_arroz)}% do arroz descascado)
- Farelo gerado: {f"{farelo_gerado:,}".replace(",", ".")} kg ({"{:.2f}".format(percentual_farelo_arroz)}% do arroz descascado)
- Quirela gerada: {f"{quirela_gerada:,}".replace(",", ".")} kg ({"{:.2f}".format(percentual_quirela_arroz)}% do arroz descascado)\n""")