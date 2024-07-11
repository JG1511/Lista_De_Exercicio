var_1 = int(input("Digite um valor: "))
var_2 = int(input("Digite o segundo valor: "))

var_soma = 0 

for i in range(var_1,var_2 + 1):
        var_soma += i

print("O valor do somatorio é: " , var_soma)
