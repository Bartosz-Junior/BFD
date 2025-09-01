import alunos

def calcular_media():
    matricula = int(input("Matricula: "))
    nota_1 = alunos.relacao_alunos[matricula]["Nota_1"]
    nota_2 = alunos.relacao_alunos[matricula]["Nota_2"]
    nota_3 = alunos.relacao_alunos[matricula]["Nota_3"]
    alunos.relacao_alunos[matricula]["Média"] = ({"Média" : (nota_1 + nota_2 + nota_3) / 3})
    

def lancar_notas():
    print("***** LANÇAR NOTAS *****")
    matricula = int(input("Matricula: "))
    for i in range(1,4):
        nota = float(input(f"Informe a {i}ª nota: "))
        alunos.relacao_alunos[matricula][f"Nota_{i}"] = nota
