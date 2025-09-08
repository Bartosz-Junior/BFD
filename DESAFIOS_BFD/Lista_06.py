#1. Funções Básicas
#Crie uma função chamada `dobrar` que recebe um número como parâmetro e retorna o
#dobro desse valor. Teste a função com o número 5.

def dobrar(numero):
    return numero * 2

#2. Classe Simples
#Crie uma classe `Livro` com os atributos `titulo` e `autor`. Adicione um método
#`exibir_dados` que retorna uma string no formato: `"Título: [titulo], Autor: [autor]"`. Instancie
#um livro com título "1984" e autor "George Orwell", e chame o método.

class livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def exibir_dados(self):
        print(f"Titulo: {self.titulo}, Autor: {self.autor}.")

#3. Objetos e Atributos
#Dada a classe `Carro` abaixo:

class carro:
    def __init__(self, modelo, cor):
        self.modelo = modelo
        self.cor = cor

#Crie um objeto `meu_carro` com modelo "Fusca" e cor "Azul". Em seguida, altere a cor
#para "Vermelho" e imprima o novo valor do atributo `cor`.

'''meu_carro = carro("Fusca", "Azul")
print(meu_carro.cor)
meu_carro.cor = "Vermelho"
print(meu_carro.cor)'''

#4. Funções com Múltiplos Parâmetros
#Escreva uma função `calcular_imc` que recebe peso (kg) e altura (m) e retorna o IMC
#(peso / altura2). Se o IMC for:
#- < 18.5: retorne "Abaixo do peso"
#- 18.5 a 24.9: retorne "Peso normal"
#- 25 a 29.9: retorne "Sobrepeso"
#- ≥ 30: retorne "Obesidade"
#Teste com peso 70 kg e altura 1.75 m.

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    if imc < 18.5:
        print("Abaixo do peso.")
    elif imc >= 18.5 and imc < 24.9:
        print("Peso normal.")
    elif imc >= 25 and imc <= 29.9:
        print("Sobrepeso.")
    elif imc > 30:
        print("Obesidade.")

#5. Métodos que Modificam Atributos
#Crie uma classe `Conta` com atributo `saldo` (inicializado como 0). Adicione métodos:
#- `depositar(valor)`: adiciona o valor ao saldo
#- `sacar(valor)`: subtrai o valor do saldo (apenas se houver saldo suficiente)
#Crie uma conta, deposite 100, saque 30 e imprima o saldo final.

class conta_bancaria:
    def __init__(self, saldo = 0):
        self.saldo = saldo

    def depositar(self, valor):
        if valor <= 0:
            print("O valor a ser depositado deve ser maior que zero.")
        elif valor > 0:
            self.saldo += valor
            print("Deposito realizado com sucesso.")
    
    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente, tente um valor menor.")
        elif valor <= self.saldo:
            self.saldo -= valor
            print("Saque realizado com sucesso.")

'''conta_01 = conta_bancaria()
print(conta_01.saldo)
conta_01.depositar(100)
print(conta_01.saldo)
conta_01.sacar(30)
print(conta_01.saldo)'''


#6. Interação entre Objetos
#Crie uma classe `Pedido` com atributos `produto` e `quantidade`. Crie uma classe
#`Cliente` com atributo `nome` e um método `fazer_pedido(produto, quantidade)` que retorna
#um objeto `Pedido`. Faça um cliente "João" fazer um pedido de "Notebook" com quantidade 2.

class pedido:
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade

class cliente(pedido):
    def __init__(self, nome):
        self.nome = nome

    def fazer_pedido(self, produto, quantidade):
        return pedido(produto, quantidade)

'''joao = cliente("João")
pedido_de_joao = joao.fazer_pedido("Notebook", 2)
print(f"Cliente: {joao.nome}")
print(f"Produto: {pedido_de_joao.produto}")
print(f"Quantidade: {pedido_de_joao.quantidade}")'''


#7. Métodos Especiais
#Crie uma classe `Ponto` com atributos `x` e `y`. Implemente o método `__str__` para
#retornar `"(x, y)"` e o método `__add__` para permitir a soma de dois pontos (soma das
#coordenadas). Teste criando dois pontos (1, 2) e (3, 4), somando-os e imprimindo o resultado.

class ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return self.x, self.y

    def __add__(self, x, y):
        return self.x + x , self.y + y


#8. Classe com Lista de Objetos
#Crie uma classe `Turma` com atributo `alunos` (lista vazia). Adicione métodos:
#- `adicionar_aluno(aluno)`: adiciona um objeto `Aluno` à lista
#- `media_turma()`: calcula a média das notas de todos os alunos (cada aluno tem uma
#lista de notas)
#Use a classe `Aluno` da aula. Crie 3 alunos com notas [8,7,9], [6,5,7], [9,8,9], adicione-os
#à turma e calcule a média geral.
'''
class turma:
    def __init__(self):
        self.alunos = []
        self.nota_aluno = []
        self.media_aluno = []
        self.media_turma = 0


    def add_aluno(self, aluno, *notas):
        self.alunos.append(aluno)
        self.nota_aluno.append(notas)
        self.media_aluno.append(sum(notas)/len(notas))


    def cal_media_turma(self):
        if self.nota_aluno:
            self.media_turma = sum(self.media_aluno)/len(self.media_aluno)
        else:
            print("A lista de médias está vazia!")

    def status(self):
        print(f"Alunos: {self.alunos}")
        print(f"Média por aluno: {self.media_aluno}")
        print(f"Média da turma: {self.media_turma}")

turma_01 = turma()
turma_01.add_aluno("Junior", 8,7,9)
turma_01.add_aluno("Camila", 6,5,7)
turma_01.add_aluno("Bartosz", 9,8,9)
turma_01.cal_media_turma()
turma_01.status()
'''

#9. Composição de Objetos
#Crie uma classe `Motor` com atributo `potencia`. Crie uma classe `Carro` com atributos
#`modelo` e `motor` (objeto da classe `Motor`). Adicione um método `exibir_detalhes` que
#retorna `"Modelo: [modelo], Motor: [potencia] CV"`. Crie um motor de 150 CV, um carro
#"Ferrari" com esse motor, e exiba os detalhes.

class Motor:
    def __init__(self):
        pass


class Carro(Motor):
    def __init__(self, modelo, motor):
        pass


    def exibir_detalhes(self):
        pass