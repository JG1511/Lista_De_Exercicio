linhas = 4
colunas = 4
matriz = []

for i in range(linhas):
    linha = []
    for j in range(colunas):
        valor = int(input(f"Digite os valores das posições ({i},{j}): "))
        linha += [valor]
    matriz += [linha]

for i in range(linhas):
    soma_linha = 0
    for j in range(colunas):
      if i % 2 == 1 and j % 2 == 1:
        soma_linha += matriz[i][j]
    print(soma_linha)