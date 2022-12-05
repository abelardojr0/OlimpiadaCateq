listaAlunos = []
qtdeAlunos = int(input("Digite a quantidade de alunos: "))
qtdeEquipe = int(input("Digite a quantidade de equipes: "))
for aluno in range(qtdeAlunos):
    aluno = input("Digite o nome do aluno: ")
    listaAlunos.append(aluno)
print(listaAlunos)