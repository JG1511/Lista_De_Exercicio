lista_A = input("Digite os números do conjunto A com espaço: ").split()
lista_B = input("Digite os números do conjunto B com espaço: ").split()
lista_C = input("Digite os números do conjunto C com espaço: ").split()

lista_numero_A = [int(numero) for numero in lista_A]
lista_numero_B = [int(numero) for numero in lista_B]
lista_numero_C = [int(numero) for numero in lista_C]

conjunto_A = set(lista_numero_A)
conjunto_B = set(lista_numero_B)
conjunto_C = set(lista_numero_C)

uniao = conjunto_A.union(conjunto_B)
diferenca = uniao.difference(conjunto_C)

print(f"União: {uniao}")
print(f"Diferença: {diferenca}")


