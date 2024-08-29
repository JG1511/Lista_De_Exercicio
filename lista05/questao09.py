tamanho_A = int(input("Digite o tamanho do conjunto A: "))
tamanho_B = int(input("Digite o tamanho do conjunto B: "))
lista_A = []
lista_B = []
flag_A = 1
flag_B = 1

print("Conjunto A:")
while flag_A <= tamanho_A :
    valor = int(input("Digite um número para lista: "))
    lista_A.append(valor)
    string = input("Digite uma letra, nome ou número: ")
    lista_A.append(string)
    
    flag_A += 1

print("Conjunto B:")
while flag_B <= tamanho_B :
    valor = int(input("Digite um número para lista: "))
    lista_B.append(valor)
    string = input("Digite uma letra, nome ou número: ")
    lista_B.append(string)
   

    flag_B += 1

conjunto_A = set(lista_A)
conjunto_B = set(lista_B)

if conjunto_B <= conjunto_A:
    print("B é subconjunto de A")
else:
    print("B não é subconjunto de A")

conjunto_C = conjunto_A.difference(conjunto_B)

print(f"Conjunto A: {conjunto_A}")
print(f"Conjunto B: {conjunto_B}")
print(f"Conjunto C: {conjunto_C}")