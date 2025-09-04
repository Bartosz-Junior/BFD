class ContaBancaria:
    def __init__(self, titular, num_conta, saldo = 0, ):
        self.titular = titular
        self.num_conta = num_conta
        self.saldo = saldo

    def extrato(self):
        print("***** EXTRATO *****")
        print(f"R${self.saldo}")

    def depositar(self):
        print("***** DEPOSITAR *****")
        valor_deposito = float(input("Valor do deposito: R$"))
        if self.saldo > 10000:
            self.saldo += valor_deposito + (valor_deposito * 5/100)
            print(f"Você recebeu 5% do valor depositado, por ter pelo menos 10 mil na conta.")
        else:
            self.saldo += valor_deposito
            print("Deposito realizado com sucesso!")


    def sacar(self):
        print("***** SACAR *****\n")
        valor_saque = float(input("Valor do saque: "))
        if self.saldo >= valor_saque:
            self.saldo -= valor_saque
            print("Saque realizado com sucesso!\n")
        else:
            print("Saldo insuficiente!")
            print(f"Seu saldo é de R${self.saldo}")

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
