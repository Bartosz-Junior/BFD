import usuarios


def menu():
    print("Bem-vindo ao sistema de LOGIN - BFD 2025")
    print("[1] - LOGIN")
    print("[2] - CADASTRAR NOVO USUÁRIO")
    print("[0] - SAIR")

def login():
    print("***** LOGIN *****\n")
    usuario_login = str(input("Login: "))
    usuario_senha = str(input("Senha: "))
    if usuario_login in usuarios.usuarios.keys() and usuario_senha in usuarios.usuarios.values():
        print("Sucesso!")
    else:
        print("Usuário ou senha incorreto.")

def registrar_usuario():
    print("***** CADASTRAR USUÁRIO *****")
    novo_usuario = str(input("Informe o Login do novo usuário: "))
    nova_senha = str(input("Informe a senha do novo usuário: "))
    usuarios.usuarios.update({novo_usuario : nova_senha})
