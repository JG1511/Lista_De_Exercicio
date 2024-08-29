tamanho = int(input("Digite o tamanho da lista: "))
lista = []

for i in range(tamanho):
    valor = int(input("Digite os valores da lista: "))
    lista.append(valor) # mesma coisa +=

conjunto_inicial = set(lista)
lista_final = []

for i in conjunto_inicial:
    lista_final.append(i)

maior_valor = lista_final[0]
indice = 0

for i in range(len(lista_final)):
    if lista_final[i] > maior_valor:
        maior_valor = lista_final[i]
        indice = i

lista_final[indice] = maior_valor * 2
conjunto_final = set(lista_final)

print(f"Lista de entrada: {lista}")
print(f"Conjunto de saida: {conjunto_final}")

