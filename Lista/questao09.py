var_soma_par = 0
var_soma_impar = 0

for i in range (10) :
    valor = int(input("Digite um valor: "))

    if valor % 2 == 0:
        var_soma_par += valor
    elif valor % 2 != 0:
        var_soma_impar +=valor

print("Valor par: ", var_soma_par)
print("Valor impar ", var_soma_impar)
