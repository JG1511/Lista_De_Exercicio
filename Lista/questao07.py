var_soma_pares = 0

for i in range(5):
    valor = int(input("Digite um valor: "))

    if valor % 2 == 0:
        var_soma_pares += valor
print("O valor do somatori dos pares é: ", var_soma_pares)