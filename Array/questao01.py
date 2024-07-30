#Questão 01
lista_inteiros = []
lista_sem_rep = []
for _ in range(4):
    valor = int(input("Digite valores inteiros: "))       
    lista_inteiros += [valor]
for valor in lista_inteiros:
    if valor not in lista_sem_rep:
        lista_sem_rep += [valor]
print(f"lista fornecida pelo o usuario: {lista_inteiros}")
print(f"Lista sem repticao:{lista_sem_rep}")