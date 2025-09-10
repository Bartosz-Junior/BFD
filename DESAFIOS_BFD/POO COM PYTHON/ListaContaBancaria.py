class ListaContas:
    def __init__(self):
        self.usuarios = []

    def add_usuario(self):
        print("_____ CADASTRO DE USUÁRIO _____")
        usuario = str(input("Nome de usuário: "))
        senha = str(input("Cadastre uma senha: "))
        self.usuarios.append({usuario: senha})

    def listar_usuario(self):
        for i,v in enumerate(self.usuarios):
            print(i,v)

usuario_1 = ListaContas()
usuario_1.add_usuario()
usuario_1.add_usuario()
usuario_1.listar_usuario()
