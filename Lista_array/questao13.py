linhas = 3
colunas = 3
matriz_a = []
matriz_b = []
matriz_resultante = [[0 for _ in range(linhas)] for _ in range(colunas)]

print("Primeira matriz")
for i in range(linhas):
    linha = []
    for j in range(colunas):
        valor = int(input(f"Digite o valor das poisições ({i},{j}): "))
        linha += [valor]
    matriz_a += [linha]

print("Segunda matriz")
for i in range(linhas):
    linha = []
    for j in range(colunas):
        valor = int(input(f"Digite o valor das poisições ({i},{j}): "))
        linha += [valor]
    matriz_b += [linha]

for i in range(colunas):
    for j in range(linhas):
        if matriz_a[i][j] > matriz_b[i][j]:
            matriz_resultante[i][j] = matriz_a[i][j]
        if matriz_a[i][j] < matriz_b[i][j]:
            matriz_resultante[i][j] = matriz_b[i][j]
        else:
            matriz_resultante[i][j] = matriz_a[i][j]
print("Matriz a")
for _ in matriz_a:
    print(_)
print("Matriz b")
for _ in matriz_b:
    print(_)

print("matriz resultante:")

for _ in matriz_resultante:
    print(_)