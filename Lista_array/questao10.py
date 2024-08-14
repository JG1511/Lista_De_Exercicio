linhas = 3
colunas = 3 
matriz = []
soma_impar = 0

for i in range(linhas):
    linha = []
    for j in range(colunas):
        valor = int(input(f"Digite os valores das posicao: ({i},{j}): "))
        linha += [valor]
    matriz += [linha]

for i in range(linhas):
    for j in range(colunas):
        if matriz[i][j] % 2 != 0:
            soma_impar += 1

print("Matriz:")

for _ in matriz:
    print(_)

print(f"Números impares: {soma_impar}")