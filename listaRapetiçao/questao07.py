# Escreva um programa que solicita ao usuário 3 valores inteiros. Em seguida o pro-
# grama deverá perguntar ao usuário se deseja ver os valores impressos em ordem

# crescente ou decrescente. Após a escolha, o programa deverá exibir os valores or-
# denados conforme indicação do usuário.


var_1 = int(input("Digite o primeiro num: "))
var_2 = int(input("Digite o segundo num: "))
var_3 = int(input("Digite o terceiro num: "))

flag = input("Deseja ver em ordem crescente: (s/n)")

match flag:
    case "s" :
        if var_1 < var_2 < var_3:
            print(var_1, var_2,var_3)
        elif var_2 < var_1 < var_3:
            print(var_2,var_1,var_3)
        elif var_2 < var_3 < var_1:
            print(var_2,var_3,var_1)
        elif var_3 < var_2 < var_1:
            print(var_3,var_2,var_1)
        elif var_3 < var_1 < var_2:
            print(var_3,var_1,var_2)
        elif var_1<var_3 <var_2:
            print(var_1,var_3,var_2)
    
    case "n":
        flag_dec = input("Deseja ver em ordem decrescente: (s/n)")

        match flag_dec:
            case "s":
                if var_1 > var_2 > var_3:
                    print(var_1, var_2, var_3)
                elif var_2 > var_1 > var_3:
                    print(var_2,var_1,var_3)
                elif var_2 > var_3 > var_1:
                    print(var_2,var_3,var_1)
                elif var_3 > var_2 > var_1:
                    print(var_3,var_2,var_1)
                elif var_3 > var_1 > var_2:
                    print(var_3,var_1,var_2)
                elif var_1 > var_3 > var_2:
                    print(var_1,var_3,var_2)
            case "n":
                print("Fim do programa")
        