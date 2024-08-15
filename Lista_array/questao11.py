linhas = int(input("Digite o número de Linhas: "))
colunas = int(input("Digite o número de Colunas: "))

matriz = []
for i in range(linhas):
    linha = []
    for j in range(colunas):
        valor = int(input(f"Digite os valores da posição: ({i},{j}): "))
        linha += [valor]
    matriz += [linha]

for i in range(linhas):
    soma_linha = 0
    for j in range(colunas):
        soma_linha += matriz[i][j] 
    print(f"{matriz[i]} = {soma_linha}")