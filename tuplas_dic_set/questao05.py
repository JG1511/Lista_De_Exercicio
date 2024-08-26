tamanho = int(input("Digite o tamanho do conjunto: "))
lista_numero_a = []
lista_numero_b = []

print("Conjunto A:")
for i in range(tamanho):
    valor = int(input("digite os valores: "))
    lista_numero_a.append(valor)

print("Conjunto B:")
for i in range(tamanho):
    valor = int(input("digite os valores: "))
    lista_numero_b.append(valor) ## +=[valor]

conjunto_a = set(lista_numero_a)
conjunto_b = set(lista_numero_b)

conjunto_final = conjunto_a & conjunto_b


print(f"Conjunto final: {conjunto_final}")
