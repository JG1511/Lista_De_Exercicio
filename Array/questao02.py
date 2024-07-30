#Questão 02

lista_inteiros = []
lista_pares = []
numero_alvo = int(input("Digite um número alvo: "))

for _ in range(5):
    valor = int(input("Digite valores inteiros: "))
    lista_inteiros += [valor]

for i in range(len(lista_inteiros)):
   for j in range(i + 1, len(lista_inteiros)):
       if lista_inteiros [i] + lista_inteiros [j] == numero_alvo:
           lista_pares += [lista_inteiros [i], lista_inteiros [j] ]
print("Pares encontrados: ", lista_pares)