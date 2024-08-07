linhas_1 = int(input("Digite o número de linhas da primeira matriz: "))
colunas_1 = int(input("Digite o número de colunas da primeira matriz: "))
linhas_2 = int(input("Digite o número de linhas da segunda matriz: "))
colunas_2 = int(input("Digite o número de colunas da segunda matriz: "))
linhas_final = linhas_1
colunas_final = colunas_1

matriz_usuario_1 = []
matriz_usuario_2 = []
matriz_final =[[0 for _ in range(linhas_final)]for _ in range(colunas_final)]

for i in range (linhas_1):
    linha = []
    for j in range(colunas_1):
        valor = int(input(f"Digite os valoreses das posicao({i},{j}): "))
        linha += [valor]
    matriz_usuario_1 += [linha]

for i in range(linhas_2):
    linha_segunda_matriz = []
    for j in range(colunas_2):
        valor_segunda_matriz = int(input(f"Digite os valores das posicao({i},{j}): "))
        linha_segunda_matriz += [valor_segunda_matriz]
    matriz_usuario_2 += [linha_segunda_matriz]

for i in range(linhas_1):
    for j in range(colunas_1):
        if matriz_usuario_1[i][j] > matriz_usuario_2[i][j]:
            matriz_final[i][j] = 1
        elif matriz_usuario_1[i][j] < matriz_usuario_2[i][j]:
                matriz_final[i][j] = 2
        elif matriz_usuario_1[i][j] == matriz_usuario_2[i][j]:
                matriz_final[i][j] = 0

print("Primeira matriz")

for matriz in matriz_usuario_1:
    print(matriz)

print("Segunda matriz")

for matriz in matriz_usuario_2:
    print(matriz)

print("Matriz final")

for matriz in matriz_final:
    print(matriz)
