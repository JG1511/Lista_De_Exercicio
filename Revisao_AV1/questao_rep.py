# https://pessoal.dainf.ct.utfpr.edu.br/leoneloalmeida/cursos/if71a-s83-2016-01/algoritmos_3_exerc.pdf

#Questão 1

# tabuada = int(input("Digite o valor da tabuda: "))
# resultado = 0

# for i in range(1, 10 + 1, +1):
#     resultado = tabuada * i
#     print(tabuada, "x" , i, "=", resultado)

#Questão 2

# tabuada = int(input("Digite o valor da tabuda: "))
# fim = int(input("Digite até onde você quer: "))
# resultado = 0

# for i in range(1, fim +1, +1):
#     resultado = tabuada * i
#     print(tabuada, "x" , i, "=", resultado)

#Questão 3

# tabuada = int(input("Digite o valor da tabuda: "))
# resultado = 0

# for i in range(1, 10 + 1, +1):
#     resultado = tabuada * i
#     if resultado % 2 == 0:
#       print(tabuada, "x" , i, "=", resultado)

#Questão 4

# tabuada = int(input("Digite o valor da tabuda: "))
# resultado = 0

# for i in range(1, 10 + 1, +1):
#     resultado = tabuada * i
#     if resultado % 2 != 0:
#       print(tabuada, "x" , i, "=", resultado)

#Questão 5
escolha = int(input("Digite (1-para crescente/2-para decrescente)"))

match escolha:
    case 1:
        a1 = int(input("Digite o primeiro termo: "))
        r = int(input("Digite a razão: "))
        n = int(input("Digite quanto você quer:")) 


        for i in range(n):
            print(a1)
            a1 += r
    case 2: 
         a1 = int(input("Digite o ultimo termo: "))
         r = int(input("Digite a razão: "))
         n = int(input("Digite quanto você quer:")) 


         for i in range(n):
            print(a1)
            a1 -= r

#Questão 6
