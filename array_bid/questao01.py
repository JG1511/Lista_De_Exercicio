linhas = int(input("Digite o número de linhas: "))
colunas = int(input("Digite o número de colunas: "))

matriz_usuario = []
for i in range(linhas):
    linha = []
    for j in range(colunas):
        valor = int(input(f"Digite o valor para a posicao({i},{j}): "))
        linha += [valor]  
    matriz_usuario += [linha]

for i in range(linhas):
    for j in range(colunas):
        if matriz_usuario[i][j] < 0:
            matriz_usuario[i][j] *= -2

for _ in matriz_usuario:
    print(_)