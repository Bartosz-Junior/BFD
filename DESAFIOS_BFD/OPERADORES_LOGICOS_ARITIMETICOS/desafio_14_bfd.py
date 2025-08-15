#Pergunte a nota de um aluno e se ele fez trabalho extra (True/False). 
#Aprove se a nota for ≥ 7 ou se fez trabalho extra.

#Entrada de dados com nota e se fez trabalho extra
nota = float(input("Informe a nota do aluno: "))
trabalho_extra = str(input("Digite [S] ou [N] se fez ou não o trabalho extra: ")).upper().strip()

#Verifica se aprovado
verifica_aprovado = nota >= 7 or trabalho_extra == "S"

#Imprime se aprovado se nota maior ou igual 7 aprovado, se trabalho == sim aprovado

print(f"O aluno está aprovado? {verifica_aprovado}.")
