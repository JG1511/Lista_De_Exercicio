#Questão 11 lista 03 

quantidade_numeros  =  int(input("Digite a quantidade de numeros: "))
soma_numeros = 0
num_str = ""

for i in range(quantidade_numeros ):
    valor = int(input("Digite seus numero: "))
    soma_numeros += valor

    if i == 0:
        num_str += str(valor)
    else:
        num_str += f" + {valor}"

print(f"Soma: {num_str} = {soma_numeros}")

