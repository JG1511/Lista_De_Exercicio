# Escreva um programa que solicite um número entre 1 e 10. Caso o usuário digite um
# valor dentro dessa faixa o programa deverá exibir a mensagem “O número digitado
# está DENTRO da faixa solicitada.”, senão o programa deverá exibir a mensagem “O
# número digitado está FORA da faixa solicitada.”.

valor = int(input("Digite um número entre 1 e 10: "))

if 1 < valor < 10:
    print("O número digitado está DENTRO da faixa solicitada")
elif valor == 1 or valor == 10:
    print("É um valor entre")
else:
    print("O número digitado está FORA da faixa solicitada")