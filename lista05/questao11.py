pontuacao = ",."
texto = input("Digite um texto: ").split()
contador = {}

for palavra in texto:
    palavra_sem_pontuacao = ""
    for letra in palavra:
        if letra not in pontuacao:
            palavra_sem_pontuacao += letra
    
    palavra_sem_pontuacao = palavra_sem_pontuacao.lower()

    if palavra_sem_pontuacao in contador:
        contador[palavra_sem_pontuacao] += 1
    else:
        contador[palavra_sem_pontuacao] = 1


print(contador)