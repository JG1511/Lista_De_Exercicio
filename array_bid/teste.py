# matriz = [[0 for _ in range(4)]for _ in range(4)]
# print(matriz)

# #Para exibir a matriz
# for linha in matriz:
#     print(linha)

#Questão 05

# entrada = int(input("Digite o valor de entrada: "))
# lista_usuario = []
# soma = 0

# for i in range(entrada):
#     valor = int(input("Digite os valores: "))
#     lista_usuario += [valor]

# menor_elemento  = lista_usuario[0]
# maior_elemento = lista_usuario[0]

# for elemento in lista_usuario:
#     if elemento < menor_elemento:
#         menor_elemento = elemento
#     if elemento > maior_elemento:
#         maior_elemento = elemento
#     soma += elemento

# soma_aritimetica = soma / len(lista_usuario)

# print(f"Menor elemento: {menor_elemento}")
# print(f"Maior elemento: {maior_elemento}")
# print(f"Media aritimetica: {soma_aritimetica}")

#Questão 06

lista_numero = []
lista_nome = []

for i in range(6):
    valor = int(input("Digite os valores: "))
    lista_numero += [valor]
for i in range(6):
    letra = input("Digite letras: ")
    lista_nome += [letra]

for i in range (1,6,2):
    lista_numero[i] = lista_nome [i]

print(lista_numero)
