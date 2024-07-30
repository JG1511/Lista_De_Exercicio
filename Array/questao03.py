#Questão 03

lista_int = []
lista_final = []
passo = int(input("Digite o número de passos: "))

for _ in range(5):
    valor = int(input("Digite valores para a lista: "))
    lista_int += [valor]

tamanho = len(lista_int)
passo = passo % tamanho

if passo > 0:
    lista_final += lista_int [passo + 1: ] + lista_int[:passo + 1]


print(f"Lista fornecida pelo o usuario:{lista_int}")
print(f"Lista rotacionada:{lista_final}")

