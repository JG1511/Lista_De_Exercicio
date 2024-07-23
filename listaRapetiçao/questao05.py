# Escreva um programa que leia dois valores inteiros e escreva como saída a diferença
# entre o maior valor e o menor valor.

valor = int(input("Digite o primeiro valor: "))
valor2= int(input("Digite o segundo valor: "))

if valor < valor2:
    valor_sub = valor2 - valor
    print("A diferença entre o maior valor e o menor: ", valor_sub)
elif valor2 < valor:
     valor_sub = valor - valor2
     print("A diferença entre o maior valor e o menor: ",  valor_sub)
    
    