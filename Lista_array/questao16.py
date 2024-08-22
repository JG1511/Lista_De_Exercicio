import random

linhas = 3
colunas = 3 
matriz_a = []
matriz_b = []
matriz_resultante = [[0 for _ in range(linhas)] for _ in range(colunas)]

for i in range(linhas):
    linha = []
    for j in range(colunas):
        valor = random.randint(1,9)
        linha.append(valor)
    matriz_a.append(linha)

for i in range(linhas):
    linha = []
    for j in range(colunas):
        valor = random.randint(1,9)
        linha.append(valor)
    matriz_b.append(linha)

linhas_a = len(matriz_a)
colunas_a = len(matriz_a[0])
linhas_b = len(matriz_b)
colunas_b = len(matriz_b[0])

for i in range(linhas_a):
    for j in range(colunas_b):
        for k in range(colunas_a):
            matriz_resultante[i][j] += matriz_a[i][k] * matriz_b[k][j]

print("Matriz A:")
for _ in matriz_a:
    print(_)
print("Matriz B: ")
for _ in matriz_b:
    print(_)
print("Matriz resultante: ")
for _ in matriz_resultante:
    print(_)