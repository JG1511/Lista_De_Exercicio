linhas_matriz = int(input("Digite o número de linhas: "))
colunas_matriz = int(input("Digite o número de colunas: "))

matriz_user_1 = []
matriz_user_2 = []
matriz_resultado = [[0 for _ in range(linhas_matriz)]for _ in range(colunas_matriz)]
flag = 1

for i in range(linhas_matriz):
    linha_primeira_matriz = []
    for j in range(colunas_matriz):
        valor_primeira_matriz = int(input(f"Digite os valores das posicao({i},{j}): "))
        linha_primeira_matriz += [valor_primeira_matriz]
    matriz_user_1 += [linha_primeira_matriz]

for i in range(linhas_matriz):
    linha_segunda_matriz = []
    for j in range(colunas_matriz):
        valor_segunda_matriz = int(input(f"Digite os valores das posicao({i},{j}): "))
        linha_segunda_matriz += [valor_segunda_matriz]
    matriz_user_2 += [linha_segunda_matriz]

while (flag != 0):
    print('===========================================================')
    pergunta = input("Qual operacao você deseja realizar(+,-,/,*,%): ")
    flag = int(input("Deseja continuar (1-sim/0-Não): "))
    print('===========================================================')

    match pergunta:
        case "+":
            for i in range(linhas_matriz):
                for j in range(colunas_matriz):
                    matriz_resultado[i][j] += matriz_user_1[i][j] + matriz_user_2[i][j]    
            for _ in matriz_resultado:
                print(_)
        case "-":
            for i in range(linhas_matriz):
                for j in range(colunas_matriz):
                    matriz_resultado[i][j] += matriz_user_1[i][j] - matriz_user_2[i][j]    
            for _ in matriz_resultado:
                print(_)
        case "/":
            for i in range(linhas_matriz):
                for j in range(colunas_matriz):
                    matriz_resultado[i][j] += matriz_user_1[i][j] / matriz_user_2[i][j]    
            for _ in matriz_resultado:
                print(_)
        case "*":
            for i in range(linhas_matriz):
                for j in range(colunas_matriz):
                    matriz_resultado[i][j] += matriz_user_1[i][j] * matriz_user_2[i][j]    
            for _ in matriz_resultado:
                print(_)
        case "%":
            for i in range(linhas_matriz):
                for j in range(colunas_matriz):
                    matriz_resultado[i][j] += matriz_user_1[i][j] % matriz_user_2[i][j]    
            for _ in matriz_resultado:
                print(_)