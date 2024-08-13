# leia 10 valores inteiros e armazene em uma lista. O programa deve imprimir no terminal
# quantos valores pares foram digitados pelo usuário. Dica: use o operador “%” para
# verificar se o número é par (ZERO é neutro, ZERO NÃO É PAR). Exemplos:

lista_usuario = []
soma_par = 0

for _ in range(10):
    valor = int(input("Digite os valores da lista: "))
    lista_usuario += [valor]
for elemento in lista_usuario:
    if elemento % 2 == 0 and elemento != 0:
        soma_par += 1

print(f"Quantidade de valores par: {soma_par}")