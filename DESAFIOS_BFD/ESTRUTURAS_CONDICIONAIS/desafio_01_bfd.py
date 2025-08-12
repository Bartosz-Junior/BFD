#SOLICITE NOME E NOTA DE UM ALUNO, PEÇA LOGIN E SENHA, VALIDE SE É ADMIN 1234, SE SIM ACESSO PERMITIDO
#SE NÃO USUARIO E SENHA INCORRETOS

#Solicitando dados do aluno(nome e senha)
nome_aluno = str(input("Informe o nome do aluno: "))
nota_aluno = float(input("Informe a nota que deseja registrar: "))

print("Informe Login e Senha para registrar Nome e Nota do aluno.")

login_usuario = str(input("Login: ")).lower().strip()
senha_usuario = str(input("Senha: ")).lower().strip()

if (login_usuario == "admin" and senha_usuario == "admin123"):
    print("Acesso ao sistema liberado.\nNota salva com sucesso!")
else:
    print("Usuário ou senha incorretos.")
