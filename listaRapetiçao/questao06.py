# Escreva um programa que solicita ao usuário 3 valores inteiros. Em seguida o pro-
# grama deverá exibir os 3 valores digitados pelo usuário em ordem crescente.

valor = int(input("Digite um valor:"))
valor_1 = int(input("Digite um valor:"))
valor_2 = int(input("Digite um valor:"))

if valor < valor_1 < valor_2:
    print(valor, valor_1, valor_2)

elif valor_1 < valor < valor_2:
    print(valor_1, valor,valor_2)

elif valor_1 < valor_2 < valor:
    print(valor_1, valor_2, valor)

elif valor_2 < valor < valor_1:
    print(valor_2,valor, valor_1)

elif valor < valor_2 < valor_1:
    print(valor,valor_2,valor_1)

elif valor_2 < valor_1 < valor:
    print(valor_2,valor_1,valor)