# Crie um programa que solicite ao usuário uma lista de números inteiros e uma string
# de mesmo comprimento. O programa deve substituir os números nos índices ímpares

# da lista por caracteres correspondentes da string nos mesmos índices. Exiba a se-
# quência resultante, separada por um espaço em branco.

lista_numero = []
lista_nome = []
tamanho = int(input("Digite o tamanho das listas: "))

for i in range(tamanho):
    valor = int(input("Digite valores: "))
    lista_numero += [valor]
for j in range(tamanho):
    letras = input("Digite letras: ")
    lista_nome += [letras]

for i in range(1, tamanho, 2):
    lista_numero[i] = lista_nome[i]

print(lista_numero)