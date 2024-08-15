# Escreva um programa que receba como entrada uma string constituída por uma se-
# quência de números inteiros separados por espaço. O programa deverá transformar

# essa string em uma lista de números inteiros e apresentar o resultado da soma dos
# valores das posições ímpares dessa lista. 

lista_inicial = input("Digite os valores com espeço: ")
lista_final = lista_inicial.split()

lista_numero = [int(numero) for numero in lista_final]
num_str = " "
soma_num = 0

for valor in lista_numero:
    if valor % 2 == 1:
        soma_num += valor
        if valor == 0:
            num_str += str(valor)
        else:
            num_str += f" + {valor} "
        
print(f"Soma:{num_str} = {soma_num}") 

