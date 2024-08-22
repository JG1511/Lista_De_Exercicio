linhas = 4
colunas = 4
matriz = []
soma_total = 0
num_str = " "


for i in range(linhas):
    linha = []
    for  j in range(colunas):
        valor = int(input(f"Digite o valor das posições({i},{j}):  "))
        linha += [valor]
    matriz += [linha]

for i in range(linhas):
    for j in range(colunas):
        if i % 2 == 1 and j % 2 == 1:
            soma_total += matriz[i][j]
            if i == 0 and j == 0:
                num_str += matriz[i][j]
            else:
                num_str += f" + {matriz[i][j]}"

print(f"Soma: {num_str} = {soma_total}")