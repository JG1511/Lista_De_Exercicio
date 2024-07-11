var_soma = 0

for i in range(5):
    var_num = int(input("Digite um valor: "))

    if var_num < 10:
        var_soma += var_num
print("O somatorio é: ", var_soma)