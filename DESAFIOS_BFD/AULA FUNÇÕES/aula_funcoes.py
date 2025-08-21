lista_tarefas = []
tarefas_removidas = []


def add_tarefa():
    tarefa = str(input("Qual tarefa você deseja adicionar: ")).lower().strip()
    lista_tarefas.append(tarefa)
    print("Tarefa salva com sucesso!")

def listar_tarefas_pendentes():
    print(f"***** TAREFAS PENDENTES *****")
    print(lista_tarefas)

def marcar_concluidas():
    concluir_tarefa = str(input("Qual tarefa você concluiu: "))
    if (concluir_tarefa in lista_tarefas):
        lista_tarefas.remove(concluir_tarefa)
        lista_tarefas.append(concluir_tarefa + "- CONCLUIDO")
    else:
        print("Registro não econtrado!")

def remover_tarefa():
    tarefa_remover = str(input("Qual tarefa você deseja remover: ")).lower().strip()
    tarefas_removidas.append(tarefa_remover)
    lista_tarefas.remove(tarefa_remover)

    if (tarefa_remover not in lista_tarefas):
        print("Registro não encontrado!")
        print(lista_tarefas)
    else:
        print("Registro removido com sucesso!")
        print("***** LISTA ATUALIZADA *****")
        print(lista_tarefas)

add_tarefa()
add_tarefa()
add_tarefa()
listar_tarefas_pendentes()
marcar_concluidas()
listar_tarefas_pendentes()
