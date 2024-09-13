import atv

def resumo(produtos):
    qtdmaior = 0
    qtdmenor = 99999999


    for item in produtos:
        qtd = item["qtd"] 
        if qtd >= qtdmaior:
            itemmaisvendido = item
            qtdmaior = qtd
        if qtd  <= qtdmenor:
            itemmenosvendido = item
            qtdmenor = qtd
    print (f"mais  vendido {itemmaisvendido}")
    print (f"menos vendido {itemmenosvendido}")
# resumo(atv.produtos)