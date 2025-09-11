import ListaContaBancaria as lb

class ContaBancaria:
    def __init__(self, titular, num_conta, saldo = 0):
        self.titular = titular
        self.num_conta = num_conta
        self.saldo = saldo
        self._extrato = []

    def extrato(self):
        print("***** EXTRATO *****")
        for i,v in enumerate(self._extrato):
            print(i,v)
        print("\n")
        print(f"Saldo em conta: R${self.saldo}")

    def depositar(self):
        print("***** DEPOSITAR *****")
        valor_deposito = float(input("Valor do deposito: R$"))      #Valor do deposito a ser realizado
        if self.saldo > 10000:                                      #se saldo em conta for maior que 10 mil o proximo deposito renderá 5% de cashback
            self.saldo += valor_deposito + (valor_deposito * 5/100)
            print(f"Você recebeu 5% do valor depositado, por ter mais de 10 mil na conta.")
            self._extrato.append({"+" : (valor_deposito + (valor_deposito * 5/100))})
        else:
            self.saldo += valor_deposito
            print("Deposito realizado com sucesso!")
            self._extrato.append({"+" : valor_deposito})


    def sacar(self):
        print("***** SACAR *****\n")
        valor_saque = float(input("Valor do saque: "))              #Valor que o usuario deseja sacar
        if self.saldo >= valor_saque:
            self.saldo -= valor_saque
            self._extrato.append({"-" : valor_saque})
            print("Saque realizado com sucesso!\n")
        else:
            print("Saldo insuficiente!")
            print(f"Seu saldo é de R${self.saldo}")

    def tranferencia(self):
        pass


junior = ContaBancaria(str(input("Informe o nome do titular: ")), int(input("Informe a conta: ")))

while True:
    try:
        print("____________ MENU ____________")
        print("[1] - Extrato")
        print("[2] - Depositar")
        print("[3] - Sacar")
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
            case 0:
                break

    except ValueError:
        print("Opção inválida!")

#3- EXPANDA O EXEMPLO DA CONTABANCARIA:
#ADICIONE TRANSFERENCIA ENTRE CONTAS.
#USE GETTERS PARA EXIBIR O SALDO.