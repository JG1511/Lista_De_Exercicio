posicao_1 = int(input("Digite a posição 1: "))
posicao_2 = int(input("digite a posição 2 para mudar de lugar com a posição 1: "))

tupla = (1,2,3,4,5)
lista_tupla = []

for i in tupla:
    lista_tupla += [i]

flag = lista_tupla[posicao_1]


lista_tupla[posicao_1] = lista_tupla[posicao_2]
lista_tupla[posicao_2] = flag

tupla_final = tuple(lista_tupla)

print(f"Tupla A: {tupla}")
print(f"Tupla B: {tupla_final}")
