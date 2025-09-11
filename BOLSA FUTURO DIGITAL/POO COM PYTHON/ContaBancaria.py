class ListaContas:
    def __init__(self):
        self.usuarios = []

    def add_usuario(self, ContaBancaria):
        self.usuarios.append({"Titular" : ContaBancaria.titular, "Conta" : ContaBancaria.num_conta, "Saldo" : ContaBancaria.saldo})

    def listar_usuario(self):
        for i in self.usuarios:
            print(i)



class ContaBancaria:
    def __init__(self, titular, num_conta, saldo = 0, num_transacao = 0):
        self.titular = titular
        self.num_conta = num_conta
        self.saldo = saldo
        self._extrato = {}
        self.num_transacao = num_transacao

    def extrato(self):
        print("***** EXTRATO *****")
        print(f"Nº Transação\tValor")
        for i,v in self._extrato.items():
            print(f"{i}\t\t{v}")
        print("\n")
        print(f"Saldo em conta: R${self.saldo}")

    def depositar(self):
        print("***** DEPOSITAR *****")
        valor_deposito = float(input("Valor do deposito: R$"))
        if valor_deposito > 0:                                          #Valor do deposito a ser realizado
            if self.saldo > 10000:                                      #se saldo em conta for maior que 10 mil o proximo deposito renderá 5% de cashback
                self.saldo += valor_deposito + (valor_deposito * 5/100)
                print(f"Você recebeu 5% do valor depositado, por ter mais de 10 mil na conta.")
                self._extrato.update({self.num_transacao : (valor_deposito + (valor_deposito * 5/100))})
                self.num_transacao += 1
            else:
                self.saldo += valor_deposito
                print("Deposito realizado com sucesso!")
                self._extrato.update({self.num_transacao : valor_deposito})
                self.num_transacao += 1
        else:
            print("Valor inválido!")


    def sacar(self):
        print("***** SACAR *****\n")
        valor_saque = float(input("Valor do saque: "))              #Valor que o usuario deseja sacar
        if self.saldo >= valor_saque:
            self.saldo -= valor_saque
            self._extrato.update({self.num_transacao : -valor_saque})
            print("Saque realizado com sucesso!\n")
            self.num_transacao += 1
        else:
            print("Saldo insuficiente!")
            print(f"Seu saldo é de R${self.saldo}")

    def tranferencia(self):
        print("*****   TRANSFERIR PARA:   *****\n")
        minha_lista.listar_usuario()
        conta_recebe = int(input("Informe o número da conta:"))
        achou_conta = False
        for num_conta in minha_lista.usuarios:
            



minha_lista = ListaContas()
minha_lista.add_usuario(ContaBancaria("Junior", 1010))
minha_lista.add_usuario(ContaBancaria("Camila", 1020))
minha_lista.add_usuario(ContaBancaria("Bartosz", 1030))
junior = ContaBancaria(str(input("Informe o nome do titular: ")), int(input("Informe a conta: ")))

while True:
    try:
        print("____________ MENU ____________")
        print("[1] - Extrato")
        print("[2] - Depositar")
        print("[3] - Sacar")
        print("[4] - Transferir entre contas")
        print("[0] - Sair")
        print("______________________________")

        opcao = int(input("Escolha uma opção: "))

        match opcao:
            case 1:
                junior.extrato()
            case 2:
                junior.depositar()
            case 3:
                junior.sacar()
            case 4:
                junior.tranferencia()
            case 0:
                break

    except ValueError:
        print("Opção inválida!")

#3- EXPANDA O EXEMPLO DA CONTABANCARIA:
#ADICIONE TRANSFERENCIA ENTRE CONTAS.
#USE GETTERS PARA EXIBIR O SALDO.