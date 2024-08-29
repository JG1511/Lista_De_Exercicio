lista_user_inicial = input("Digite seu nome, idade e estado com esapaço: ")
lista_user_final = lista_user_inicial.split()

tupla = tuple(lista_user_final)

print(f"Nome: {tupla[0]}")
print(f"idade: {tupla[1]}")
print(f"Estado: {tupla[2]}")