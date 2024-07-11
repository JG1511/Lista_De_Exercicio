var_soma_par = 0 
var_soma_impar = 0

for i in range(10):
    valor = int(input("Digite um valor: "))

    if valor % 2 == 0:
        var_soma_par += valor
    elif valor %2 != 0 :
        var_soma_impar += valor

if var_soma_impar > var_soma_par:
    print("O somatorio dos impares é maior ")
elif var_soma_impar < var_soma_par:
    print("O somatorio dos impares é menor")
elif var_soma_impar == var_soma_par:
    print("O somatorio dos impares e pares são iguais")