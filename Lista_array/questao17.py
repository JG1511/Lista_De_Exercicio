import random

linhas_a = int(input("Digite o valor de linhas da primeira matriz: "))
colunas_a = int(input("Digite o valor de colunas da primeira matriz: "))
linhas_b = int(input("Digite o valor de linhas da segunda matriz: "))
colunas_b = int(input("Digite o valor de colunas da seunda matriz: "))

if colunas_a != linhas_b:
    print("Impossibilidade de realizar o produto matricial")
else:

    matriz_a =[]
    matriz_b = []
    matriz_resultante = [[0 for _ in range(colunas_b)] for _ in range(linhas_a)]

    numero_aleatorio_inicial = int(input("Digite o valor do número alatorio inical: "))
    numero_aleatorio_final = int(input("Digite o valor do número alatorio inical: "))

    for i in range (linhas_a):
        linha_a = []
        for j in range(colunas_a):
            valor_a = random.randint(numero_aleatorio_inicial,numero_aleatorio_final)
            linha_a.append(valor_a)
        matriz_a.append(linha_a)

    for i in range (linhas_b):
        linha_b = []
        for j in range(colunas_b):
            valor_b = random.randint(numero_aleatorio_inicial,numero_aleatorio_final)
            linha_b.append(valor_b)
        matriz_b.append(linha_b)

    linhas_a = len(matriz_a)
    colunas_a = len(matriz_a[0])
    linha_b = len(matriz_b)
    colunas_b = len(matriz_b[0])

    for i in range(linhas_a):
        for j in range(colunas_b):
            for k in range(colunas_a):
                matriz_resultante[i][j] += matriz_a[i][k] * matriz_b[k][j]

    for linha in matriz_resultante:
        print(linha)
