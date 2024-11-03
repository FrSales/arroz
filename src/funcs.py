def descasque (par1,par2,par3):
    estoque_inicial = par1
    estoque_final = par2
    entradas = par3
    return estoque_inicial + entradas - estoque_final

def casca (par1,par2,par3):
    estoque_inicial_casca = par1 #int(input("Casca inicial:"))
    estoque_final_casca = par2 #int(input("Casca final:"))
    saidas = par3 #int(input("Saídas de casca:"))
    return -1 * (estoque_inicial_casca - saidas) + estoque_final_casca

def farelo (par1,par2,par3):
    estoque_inicial_farelo = par1 #int(input("Pallet incompleto inicial:"))
    estoque_final_farelo = par2 #int(input("Pallet incompleto final:"))
    contagem_estoquista_f = par3 #int(input("Contagem do estoquista:"))
    return (contagem_estoquista_f - estoque_inicial_farelo + estoque_final_farelo) * 25

def quirela (par1,par2,par3):
    estoque_inicial_quirela = par1 #int(input("Bag incompleto inicial:"))
    estoque_final_quirela = par2 #int(input("Bag incompleto final:"))
    contagem_estoquista_q = par3 #int(input("Contagem do estoquista:"))
    return contagem_estoquista_q - estoque_inicial_quirela + estoque_final_quirela