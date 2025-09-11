#1- CRIE UMA CLASSE PRODUTO COM ATRIBUTOS PRIVADOS NOME E PRECO.
#USE GETTERS E SETTERS PARA GARANTIR QUE O PRECO NUNCA SEJA NEGATIVO.
 
class Produto:
    def __init__(self, nome, preco):    #Método inicializador
        self.__nome = nome              
        self.__preco = preco

    def get_nome(self):                 #Get_nome para retornar o nome do produto
        return self.__nome
    
    def get_preco(self):                #Get_preco para retornar o preço do produto
        return self.__preco
    
    def set_nome(self,nome_produto):    #Set_nome para alterar o nome do produto se necessário
        self.__nome = nome_produto

    def set_preco(self, preco):         #Set_preco para alterar o preço do produto, não aceita valores menores que 0(zero)
        if preco < 0:
            return f"{preco} não é um valor válido para preço!"
        else:
            self.__preco = preco

notebook = Produto("Acer", 1000)        #Instancia do produto Notebook
print(notebook.get_nome())              #Imprime o nome do produto
print(notebook.get_preco())             #Imprimi o preco do produto
notebook.set_preco(11000)               #Atualiza o preco do produto
notebook.set_nome("Positivo")           #Altera o nome do produto
print(notebook.get_nome())              #imprime o novo nome
print(notebook.get_preco())              #Imprime o novo preco

#2 -CRIE UMA CLASSE ABSTRATA FUNCIONARIO COM METODO ABSTRATO CALCULAR_SALARIO().
#CRIE GERENTE E VENDEDOR QUE IMPLEMENTEM DE FORMAS DIFERENTES.
from abc import ABC, abstractmethod

class Funcionario(ABC):
    @abstractmethod
    def calcular_salario(self):
        pass

class Gerente(Funcionario):
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def calcular_salario(self):
        return self.salario
    
    def get_nome(self):
        return self.nome
    
    def get_salario(self):
        return self.salario
    
    def set_nome(self, nome):
        self.nome = nome

    def set_salario(self, novo_salario):
        self.salario = novo_salario
    
class Vendedor(Funcionario):
    def __init__(self, nome, salario, comissao):
        self.__nome = nome
        self.__comissao = comissao
        self.__salario = salario

    def calcular_salario(self):
           self.__salario = self.__salario + (self.__salario * (self.__comissao/100))
    
    def get_nome(self):
        return self.__nome
    
    def get_comissao(self):
        return self.__comissao
    
    def get_salario(self):
        return self.__salario
    
    def set_nome(self, nome):
        self.__nome = nome

    def set_comissao(self, comissao):
        self.__comissao = comissao

    def set_salario(self, salario):
        self.__salario = salario


#Instancia de gerente salario normal não comissionado

gerente_01 = Gerente("Junior", 5000)
gerente_01.get_nome()
gerente_01.get_salario()

#Instancia de vendedor com e sem comissao
print("________Dados vendedor__________")
vendedor_01 = Vendedor("Edvaldo", 3000, 5)   # instancia de vendedor
print(vendedor_01.get_nome())                #imprimindo nome vendedor
print(vendedor_01.get_salario())             #imprimindo salario vendedor
print(vendedor_01.get_comissao())            #imprimindo comissão %
print("________Novos dados______________")
vendedor_01.calcular_salario()               #calculando salario com comissão
print(vendedor_01.get_salario())             #Imprimindo salario com comissão

#3- EXPANDA O EXEMPLO DA CONTABANCARIA:
#ADICIONE TRANSFERENCIA ENTRE CONTAS.
#USE GETTERS PARA EXIBIR O SALDO.

class ContaBancaria:
    def __init__(self, titular, num_conta, saldo = 0 ):
        self.titular = titular
        self.num_conta = num_conta
        self.saldo = saldo
        self.__extrato = {}

    def extrato(self):
        print("***** EXTRATO *****")
        if self.__extrato:
            for i,v in enumerate(self.__extrato):
                print(i, v)

    def depositar(self):
        print("***** DEPOSITAR *****")
        valor_deposito = float(input("Valor do deposito: R$"))
        if self.saldo > 10000:
            self.saldo += valor_deposito + (valor_deposito * 5/100)
            self.__extrato.update({"Deposito" :valor_deposito })
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
        print("[4] - Transferencia entre contas")
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

#4- CRIE UM SISTEMA DE TRANSPORTE:
#CLASSE ABSTRATA TRANSPORTE.
#CLASSES ONIBUS, METRÔ  E BICICLETA QUE IMPLEMENTEM VIAJAR()

class Transporte(ABC):
    def viajar(self,origem, destino):
        self.origem = origem
        self.destino = destino

class Onibus(Transporte):
    def viajar(self, origem, destino):
        print(f"Você esta viajando de Onibus de {origem} para {destino}!")
    
class Metro(Transporte):
    def viajar(self, origem, destino):
        print(f"Você esta viajando de Metrô de {origem} para {destino}!")
    
class Bicicleta(Transporte):
    def viajar(self, origem, destino):
        print(f"Você está viajando de bicicleta de {origem} para {destino}!")
    
onibus = Onibus()
onibus.viajar("Recife", "Petrolina")
metro = Metro()
metro.viajar("São José", "Coqueiral")
bicicleta = Bicicleta()
bicicleta.viajar("Varzea", "Cordeiro")
