loja_1_item = []
loja_1_valor = []
loja_2_item = []
loja_2_valor = []

print("Loja 1")
for i in range(3):
    nome = input(f"Digite o nome do item {i+1}: ")
    loja_1_item.append(nome)
    valor = int(input(f"Digite o valor do item {i+1}: "))
    loja_1_valor.append(valor)

loja_1 = {}
for i in range(len(loja_1_item)):
    loja_1[loja_1_item[i]] = loja_1_valor[i]

print("Loja 2")
for i in range(3):
    nome = input(f"Digite o nome do intem {i+1}: ")
    loja_2_item.append(nome)
    valor = int(input(f"Digite o valor do item {i+1}: "))
    loja_2_valor.append(valor)

loja_2 = {}

for i in range(len(loja_1_item)):
    loja_2[loja_2_item[i]] = loja_2_valor[i]

estoque = {}

for chave1, valor1 in loja_1.items():
    if chave1 in estoque:
        estoque[chave1] += valor1
    else:
        estoque[chave1] = valor1

for chave2, valor2 in loja_2.items():
    if chave2 in estoque:
        estoque[chave2] += valor2
    else:
        estoque[chave2] = valor2

print(f"Loja 1: {loja_1}")
print(f"Loja 2: {loja_2}")
print(f"Estoque: {estoque}")


