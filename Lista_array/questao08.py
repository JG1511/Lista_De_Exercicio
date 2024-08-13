# Escreva um programa que receba como entrada uma string constituída por uma se-
# quência de números inteiros separados por espaço. O programa deverá transformar

# essa string em uma lista de números inteiros e apresentar o resultado da soma dos
# valores das posições ímpares dessa lista. 

lista = input("Digite os valores com espaço: ")
numero = []

for i in range(0,len(lista),2):
    numero += [int(i) for _ in lista]

print(numero)