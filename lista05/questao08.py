lista_A = input("Digite uma sequencia de valores separados por espaço: ").split()
lista_numero_A = [int(numero) for numero in lista_A]
divisor = int(input("Digite um número para ser o divisor: "))

lista_de_divisor = []

for i in range(len(lista_numero_A)):
    if lista_numero_A[i] % divisor == 0:
        lista_de_divisor.append(lista_numero_A[i])

conjunto_A = set(lista_numero_A)
conjunto_resposta = set(lista_de_divisor)

print(f"Conjunto inical: {conjunto_A}")
print(f"Conjunto resposta: {conjunto_resposta}")