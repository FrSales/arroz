def descasque (par1,par2,par3):
    estoque_inicial = par1
    estoque_final = par2
    entradas = par3
    return estoque_inicial + entradas - estoque_final

def casca (par1,par2,par3):
    estoque_inicial_casca = par1
    estoque_final_casca = par2 
    saidas = par3 
    return -1 * (estoque_inicial_casca - saidas) + estoque_final_casca

def farelo (par1,par2,par3):
    estoque_inicial_farelo = par1 
    estoque_final_farelo = par2 
    contagem_estoquista_f = par3 
    return (contagem_estoquista_f - estoque_inicial_farelo + estoque_final_farelo) * 25

def quirela (par1,par2,par3):
    estoque_inicial_quirela = par1 
    estoque_final_quirela = par2 
    contagem_estoquista_q = par3 
    return contagem_estoquista_q - estoque_inicial_quirela + estoque_final_quirela