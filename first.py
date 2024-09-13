from atv import *

def quantidade_total():
    qtd_total = 0
    for i in produtos:
        qtd_total += i["qtd"]
    return qtd_total

def valor_total():
    val_total = 0
    for i in produtos:
        val_total += i["preco"]*i["qtd"]
    return val_total

"""
qtd_total = quantidade_total()
val_total = valor_total()

media = qtd_total/len(produtos)


print(f"A quantidade total de produtos vendidos foi {qtd_total}.\nA média de produtos vendidos foi {media}.\nO faturamento total foi R${val_total}")
"""