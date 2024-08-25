paises = int(input("Quantidade de paises: "))
lista_pais = []
lista_pupulacao = []

for i in range(paises):
    nome = input(f"Digite o nome do pais({i + 1}): ")
    lista_pais += [nome]
    for j in range(1):
        valor = float(input(f"Digite o valor da população  do pais {i + 1}: "))
        lista_pupulacao += [valor]

dicionario_pais = {}
tamanho = len(lista_pais)

for i in range(tamanho):
    dicionario_pais[lista_pais[i]] = lista_pupulacao[i]

maior_valor = 0
maior_populacao = ""
for chave,valor in dicionario_pais.items():
    if valor > maior_valor:
        maior_valor = valor
        maior_populacao = chave

print(maior_populacao)