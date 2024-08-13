# Para tanto, o programa deverá inicialmente solicitar ao usuário quantos valores serão
# fornecidos para análise e só depois solicitar os valores a serem analisados. A análise
# consistirá em identificar e apresentar a partir da sequência de valores fornecidos, o
# menor valor, o maior valor e a média aritmética dos valores.

tamanho = int(input("Digite quantos valores serao fornecidos: "))
lista_usuario = []
soma = 0

for _ in range(tamanho):
    valor = int(input("Digite os valores da lista: "))
    lista_usuario += [valor]

menor_valor = lista_usuario[0]
maior_valor = lista_usuario [0]

for elemento in lista_usuario:
    if elemento < menor_valor:
        menor_valor = elemento
    elif elemento > maior_valor:
        maior_valor = elemento
    soma += elemento

media = soma / len(lista_usuario)

print(f"menor valor: {menor_valor}")
print(f"maior valor: {maior_valor}")
print(f"Media aritimetica: {media}")