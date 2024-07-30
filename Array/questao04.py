tamanho_da_lista = int(input("Digite um tamanho para lista: "))
lista_inicial = []

for _ in range(tamanho_da_lista):
    valor = int(input("Digite um valor: "))
    lista_inicial += [valor]
lista_final = [item ** 2 for item in lista_inicial if item % 2 != 0]
print(f"Quadrado dos elemnetos impares:{lista_final}")