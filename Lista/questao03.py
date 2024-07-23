valor_1 = int(input("Digite um valor: "))
valor_2 = int(input("Digite o segundo valor: "))
valor_soma = 0 

if valor_1 < valor_2:
    for i in range(valor_1, valor_2):
        print(i, end = ",")
        valor_soma += i
else:
     for i in range(valor_2, valor_1):
        print(i, end = ",")
        valor_soma += i
print("Valor do somatorio é: ", valor_soma)

