linhas = int(input("Digite o número de linhas: "))
colunas = int(input("Digite o número de colunas "))
matriz = []


for i in range(linhas):
    linha = []
    for j in range(colunas):
        valor = int(input(f"Digite o valores das posições ({i},{j}): "))
        linha += [valor]
    matriz += [linha]

for j in range(colunas):
    soma_colunas = 0
    for i in range(linhas):
        soma_colunas += matriz[i][j]
    print(f"coluna{j} = {soma_colunas}")
    