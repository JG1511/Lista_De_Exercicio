import random

matriz = []
linhas = random.randint(2,10)
colunas = random.randint(2,10)

for i in range(linhas):
    linha = []
    for j in range(colunas):
        valor = random.randint(100,999)
        linha.append(valor)
    matriz.append(linha)

menor_valor = matriz[0][0]
maior_valor = matriz[0][0]
menor_posicao = (0,0)
maior_posicao = (0,0)

for i in range(linhas):
    for j in range(colunas):
        if matriz[i][j] < menor_valor:
            menor_valor = matriz[i][j]
            menor_posicao = (i,j)
        if matriz[i][j] > maior_valor:
            maior_valor = matriz [i][j]
            maior_posicao = (i,j)
            
print("Matriz")
for _ in matriz:
    print(_)

print(f"Menor valor: {menor_valor} ({menor_posicao})")
print(f"Maior valor: {maior_valor} ({maior_posicao})")