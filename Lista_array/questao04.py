# Escreva um programa que receba como entrada 3 parâmetros: um valor inteiro corres-
# pondente à quantidade de elementos de dois arrays unidimensionais; duas sequências

# de valores do tamanho do primeiro parâmetro, os quais deverão ser armazenados em
# duas listas distintas. Em seguida, o programa deverá criar uma lista resultante formada
# pela intercalação dos valores de cada uma das sequências de entrada. Como saída o
# programa deverá imprimir as duas listas iniciais e a lista resultante.

tamanho = int(input("Digite o tamanho do array: "))
lista_um = []
lista_dois = []

print("Primeira Lista")

for j in range(tamanho):
    valor = input("Digite números/nomes: ")
    lista_um += [valor]
print("Segunda Lista")

for i in range(tamanho):
    valor = input("Digite números/nome: ")
    lista_dois += [valor]

lista_resultante = []
for i in range(tamanho):
    lista_resultante += [lista_um[i]]
    lista_resultante += [lista_dois[i]]

print(f"Primeira_Lista: {lista_um}")
print(f"Segunda_Lista: {lista_dois}")
print(f"Lista final: {lista_resultante}")


    

