class ListaContas:
    def __init__(self):
        self.usuarios = []

    def add_usuario(self):
        print("_____ CADASTRO DE USUÁRIO _____")
        usuario = str(input("Nome de usuário: "))
        senha = str(input("Cadastre uma senha: "))
        self.usuarios.append({usuario: senha, "saldo" : 0})

    def listar_usuario(self):
        for i,v in enumerate(self.usuarios):
            print(i,v)

