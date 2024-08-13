# Escreva um programa que recebe como entrada valores inteiros para criar duas listas

# de mesmo tamanho. O tamanho das listas deverá ser definido pelo usuário. O pro-
# grama deverá somar os valores pares e ímpar de cada uma das listas. Em seguida,

# comparar as somas e informar qual dos somatórios é maior ou se há um empate.

lista_um = []
lista_dois = []
tamanho = int(input("Digite o tamanho da lista: "))
soma_par_1 = 0
soma_impar_1 = 0
soma_par_2 = 0
soma_impar_2 = 0

print("Lista 1")
for i in range(tamanho):
    valor = int(input("Digite os valores da primeira lista: "))
    lista_um += [valor]
print("Lista 2")
for j in range(tamanho):
    valor = int(input("Digite os valores da segunda lista: "))
    lista_dois += [valor]

for elemento in lista_um:
    if elemento % 2 == 0:
        soma_par_1 += elemento
    else:
        soma_impar_1 += elemento

for elemento in lista_dois:
    if elemento % 2 == 0:
        soma_par_2 += elemento
    else:
        soma_impar_2 += elemento

if soma_par_1 > soma_par_2:
    print("ListaPar1 > ListaPar2")
    if soma_impar_1 > soma_impar_2:
        print("ListaImpar1 > ListaImpar2")
    if soma_impar_1 < soma_impar_2:
        print("ListaImpar2 > ListaImpar1")
    if soma_impar_1 == soma_impar_2:
        print("ListaImpar1 = ListaImpar2")    
if soma_par_1 < soma_par_2:
    print("ListaPar2 > ListaPar1")
    if soma_impar_1 > soma_impar_2:
        print("ListaImpar1 > ListaImpar2")
    if soma_impar_1 < soma_impar_2:
        print("ListaImpar2 > ListaImpar1")
    if soma_impar_1 == soma_impar_2:
        print("ListaImpar1 = ListaImpar2")

if soma_par_1 == soma_par_2:
    print("ListaPar1 = ListaPar2")
    if soma_impar_1 > soma_impar_2:
        print("ListaImpar1 > ListaImpar2")
    if soma_impar_1 < soma_impar_2:
        print("ListaImpar2 > ListaImpar1")
    if soma_impar_1 == soma_impar_2:
        print("ListaImpar1 = ListaImpar2")    