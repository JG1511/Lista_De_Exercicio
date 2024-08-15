texto = input("Palavras separadas por espaço: ")
lista_string = texto.split()
lista_final = [string for string in lista_string if string not in (".",";")]

