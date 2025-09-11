import alunos
import notas

while True:
    try:
        notas.menu()
        escolha = int(input("Escolha uma opção: "))

        if escolha == 1:
            alunos.add_aluno()
        elif escolha == 2:
            alunos.remover_aluno()
        elif escolha == 3:
            alunos.listar_alunos()
        elif escolha == 4:
            notas.lancar_notas()
        elif escolha == 5:
            notas.calcular_media()
        elif escolha == 0:
            print("Saindo ...")
            break

    except ValueError:
        print("Opção Inválida!")
