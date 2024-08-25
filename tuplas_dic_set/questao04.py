#anotar no caderno dps

quantidade_alunos = int(input("Quantos alunos: "))
lista_alunos = []
lista_notas = []

for i in range(quantidade_alunos):
    nome = input(f"Digite o nome do aluno {i + 1}: ")
    lista_alunos.append(nome)
    for j in range(3):  
        nota = float(input(f"Digite a nota {j+1} do aluno {i + 1}: "))
        lista_notas.append(nota)

dicionario_aluno = {}
tamanho = len(lista_alunos)
razao = 3

for i in range(tamanho):
    dicionario_aluno[lista_alunos[i]] = lista_notas[i*razao:(i+1) * razao]

lista_media = []

for i in range(quantidade_alunos):
    soma = 0
    for nota in dicionario_aluno[lista_alunos[i]]:
        soma += nota
    lista_media +=[soma/3]

dicionario_aluno_aprovado = {}

for i in range(len(lista_media)):
    if lista_media[i]> 7:
        dicionario_aluno_aprovado[lista_alunos[i]] = lista_media [i]

print(dicionario_aluno_aprovado)

