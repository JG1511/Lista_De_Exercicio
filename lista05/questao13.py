lista_aluno = []
lista_nota = []
quantidade_alunos = int(input("São quantos alunos: "))

for i in range(quantidade_alunos):
    nome = input(f"Digite o nome de aluno {i+1}: ")
    lista_aluno.append(nome)
    for j in range(1):
        nota = int(input(f"Digite nota do aluno {i+1}, multiplos de 10(10,20,30,...): "))
        lista_nota.append(nota)

dicionario_aluno_nota = {}

for i in range(len(lista_aluno)):
    dicionario_aluno_nota[lista_aluno[i]] = lista_nota[i]

dicionario_nota_aluno = {}

for chave, valor in dicionario_aluno_nota.items():
    if valor not in dicionario_nota_aluno:
        dicionario_nota_aluno[valor] = [chave]
    else:
        dicionario_nota_aluno[valor].append(chave)
    

print(dicionario_aluno_nota)
print(dicionario_nota_aluno)

