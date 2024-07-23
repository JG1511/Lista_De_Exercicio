print("Digite um numero negativo para parar")

inicio = int(input("Digite um valor para iniciar: "))
par = 0
impar = 0

while(inicio > 0):
    inicio = int(input("Digite o valor: ")) 
    if inicio % 2 == 0: 
        par += 1
    elif inicio % 2 !=0 and inicio > 0 :
        impar+=1
print("Quantidade de par: ", par)
print("Quantidade de impar: ", impar)
