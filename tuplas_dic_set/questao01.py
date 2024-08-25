tamanho_numeros = int(input("Quantos números você quer: "))
lista_numeros = []

for i in range(tamanho_numeros):
    valor = int(input("Digite os números: "))
    lista_numeros += [valor]

tuplas_numero = tuple(lista_numeros)
tuplas_par = ()
for i in tuplas_numero:
    if i % 2 == 0 :
        tuplas_par += (i,)

print(tuplas_par)
    
