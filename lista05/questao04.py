tamanho = int(input("Digite o tamanho da lista: "))
lista_numero = []

for i in range(tamanho):
    valor = int(input("Digite os valores da lista: "))
    lista_numero += [valor]

lista_numero_slice =lista_numero[0:3]

tupla = tuple(lista_numero)
slice_tupla = tuple(lista_numero_slice)

print(f"Tupla: {tupla}")
print(f"Slice tupla: {slice_tupla}")

