var_soma = 0 

for i in range(5):
    valor = int(input("Digite um valor: "))

    if valor >= 10 and valor < 20:
        var_soma += valor

print("Somatorio é: ", var_soma)