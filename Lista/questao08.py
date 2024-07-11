var_num = int(input("Digite um valor: "))
var_soma = 0

for i in range(var_num):
    valor  =  int(input("Digite outros valores: "))

    if valor % 2 == 0:
        valor = 1
        var_soma += valor
print("Existem essa quantidade de valores pares: ",var_soma)