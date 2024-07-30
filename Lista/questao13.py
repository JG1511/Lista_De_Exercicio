tabuada = int(input("Digite o valor da tabuada :"))
resultado = 0

for i in range(1, 10 +1, 1):
    resultado = tabuada * i
    print(tabuada, "x", i, "=", resultado, end = " , ")
    