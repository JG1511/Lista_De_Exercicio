linhas = 3
colunas = 6

matriz = []
matriz_modificada = [[0 for _ in range(colunas)] for _ in range(linhas)]

for i in range(linhas):
    linha = []
    for j in range(colunas):
        valor = int(input(f"Digite os valores das posicao({i},{j}): "))
        linha.append(valor)
    matriz.append(linha)
soma_colunas = 0
for j in range(colunas):
    if j % 2 == 1:
        for i in range(linhas):       
            soma_colunas += matriz[i][j]
media_aritimetica_colunas = 0        
for j in range(colunas):
    
    for i in range(linhas):
        if j == 1 or j == 3:
           media_aritimetica_colunas += matriz[i][j]/linhas

for j in range(colunas):
    for i in range(linhas):
        matriz_modificada[i][j] = matriz[i][j]

for i in range(linhas):
    matriz_modificada [i][5] = matriz[i][3] + matriz[i][4]

print(f"Media: {media_aritimetica_colunas}")
print(f"Soma das colunas impares: {soma_colunas}")


print("Matriz inicial:")
for linha in matriz:
    print(linha)

print("Matriz modificada:")
for linha_modificada in matriz_modificada:
    print(linha_modificada)
