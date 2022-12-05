def separarEquipes(lista, n):
    for i in range(0, len(lista), n):
        yield lista[i:i + n]


listaAlunos = []
qtdeAlunos = int(input("Digite a quantidade de alunos: "))
qtdeEquipe = int(input("Digite a quantidade de equipes: "))
for aluno in range(qtdeAlunos):
    aluno = input("Digite o nome do aluno: ")
    listaAlunos.append(aluno)
alunosPorEquipe = int(qtdeAlunos / qtdeEquipe)

print(list(separarEquipes(listaAlunos, alunosPorEquipe)))
