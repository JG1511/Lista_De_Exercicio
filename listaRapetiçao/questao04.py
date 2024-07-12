# Escreva um programa que dado dois valores informe qual deles é o maior.

valor = int(input("Digite um valor: "))
valor2 = int(input("Digite outro valor: "))

if valor < valor2:
    print("Esse valor é o maior: ", valor2)
elif valor2 < valor:
    print("Esse valor é o maior: ", valor)
    