def descasque (estoque_inicial,estoque_final,entradas):
    return estoque_inicial + entradas - estoque_final

def casca (estoque_inicial_casca,estoque_final_casca,saidas):
    return -1 * (estoque_inicial_casca - saidas) + estoque_final_casca

def farelo (estoque_inicial_farelo,estoque_final_farelo,contagem_estoquista_f):
    return (contagem_estoquista_f - estoque_inicial_farelo + estoque_final_farelo) * 25

def quirela (estoque_inicial_quirela,estoque_final_quirela,contagem_estoquista_q):
    return contagem_estoquista_q - estoque_inicial_quirela + estoque_final_quirela


def main (arroz_inicial, arroz_final, entradas_arroz,
         casca_inicial, casca_final, saidas_casca,
         pallet_farelo_inicial, pallet_farelo_final, contagem_estoquista_farelo,
         bag_quirela_inicial, bag_quirela_final, contagem_estoquista_quirela):

    arroz_descascado = descasque(arroz_inicial, arroz_final, entradas_arroz)
    casca_gerada = casca(casca_inicial, casca_final, saidas_casca)
    farelo_gerado = farelo(pallet_farelo_inicial, pallet_farelo_final, contagem_estoquista_farelo)
    quirela_gerada = quirela(bag_quirela_inicial, bag_quirela_final, contagem_estoquista_quirela)

    percentual_casca_arroz = (casca_gerada * 100) / arroz_descascado
    percentual_farelo_arroz = (farelo_gerado * 100) / arroz_descascado
    percentual_quirela_arroz = (quirela_gerada * 100) / arroz_descascado

    return f"""\n*Relatório de produção:*
- Início do descasque: 07:15
- Fim: 17:05
- Observações:
- Quantidade descascada: {f"{arroz_descascado:,}".replace(",", ".")} kg
- Casca gerada: {f"{casca_gerada:,}".replace(",", ".")} kg ({"{:.2f}".format(percentual_casca_arroz)}% do arroz descascado)
- Farelo gerado: {f"{farelo_gerado:,}".replace(",", ".")} kg ({"{:.2f}".format(percentual_farelo_arroz)}% do arroz descascado)
- Quirela gerada: {f"{quirela_gerada:,}".replace(",", ".")} kg ({"{:.2f}".format(percentual_quirela_arroz)}% do arroz descascado)\n"""
