item = [('banana',3),('uva',5),('uva',2),('banana',2),('perâ',2)]
meu_dicionario_itens ={}

for chave, valor in item:
    if chave in meu_dicionario_itens:
        meu_dicionario_itens[chave] += valor
    else:
        meu_dicionario_itens[chave] = valor

print(meu_dicionario_itens)