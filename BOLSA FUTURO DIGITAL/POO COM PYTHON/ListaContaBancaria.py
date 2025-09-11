import ContaBancaria

class ListaContas:
    def __init__(self):
        self.usuarios = {}

    def add_usuario(self, ContaBancaria):
        self.usuarios.update({"Titular:" : ContaBancaria.titular, "Conta" : ContaBancaria.num_conta, "Saldo" : ContaBancaria.saldo})

    def listar_usuario(self):
        for i,v in self.usuarios.items():
            print(i,v)

