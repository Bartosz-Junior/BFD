relacao_alunos = {}

def add_aluno():
    print("***** CADASTRO DE ALUNO *****\n")
    try:
        nome_aluno = str(input("Nome do aluno: "))
        matricula_aluno = int(input("Matricula aluno:"))
        if matricula_aluno not in relacao_alunos.keys():
            relacao_alunos.update({matricula_aluno: {"Nome": nome_aluno, "Nota_1" : 0, "Nota_2" : 0, "Nota_3" : 0, "Média" : 0}})
        else:
            print("Matricula já existente.")
    except ValueError:
        print("Valor inválido!")

def remover_aluno():
    print("***** REMOVER ALUNO *****\n")
    try:
        remover_aluno_matricula = int(input("Matricula do aluno: "))
        if remover_aluno_matricula in relacao_alunos:
            print(relacao_alunos[remover_aluno_matricula])
            relacao_alunos.pop(remover_aluno_matricula)
            print("Aluno excluido com sucesso!\n")
        else:
            print("Matricula não encontrada!")
    except ValueError:
        ("Informe a matricula corretamente!")

def listar_alunos():
    print("***** LISTA DE ALUNOS *****\n")
    if relacao_alunos:
        for i, v in enumerate(relacao_alunos.items()):
            print(v)
