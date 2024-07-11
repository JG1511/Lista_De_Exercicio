print("Calculo de um somatorio de uma sequencia de numero")

var_1 =  int(input("Digite o total de números a serem somados: "))
var_soma = 0

for  i in range(var_1):
    valor = int(input("Digite um valor: "))

    var_soma += valor

print("Número do somatorio é: ", var_soma)