# Escreva um programa que leia três valores e determine se eles podem formar um

# triângulo. Caso possam, classifique o triângulo como equilátero, isósceles ou esca-
# leno.

valor1 = int(input("Digite um valor: "))
valor2 = int(input("Digite um valor: "))
valor3 = int(input("Digite um valor: "))

if valor1 == valor2 and valor1 == valor3 and valor2 == valor3:
    print("esse triangulo é equilátero")
elif valor1 == valor2 or valor1 == valor3 or valor2 == valor3:
    print("esse trangulo é isósceles")
elif valor1 != valor2 and valor1 != valor3 and valor2 != valor3:
    print("esse triangulo é escaleno")
