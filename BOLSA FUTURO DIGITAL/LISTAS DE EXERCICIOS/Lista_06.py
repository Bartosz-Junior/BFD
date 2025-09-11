#1. Funções Básicas
#Crie uma função chamada `dobrar` que recebe um número como parâmetro e retorna o
#dobro desse valor. Teste a função com o número 5.

def dobrar(numero):
    return numero * 2   #função que retorna o dobre de um número

#2. Classe Simples
#Crie uma classe `Livro` com os atributos `titulo` e `autor`. Adicione um método
#`exibir_dados` que retorna uma string no formato: `"Título: [titulo], Autor: [autor]"`. Instancie
#um livro com título "1984" e autor "George Orwell", e chame o método.

class livro:
    def __init__(self, titulo, autor): # método inicializador da classe
        self.titulo = titulo           #atributo
        self.autor = autor             #atributo

    def exibir_dados(self):            # Método para exibir dados dos objetos instanciados
        print(f"Titulo: {self.titulo}, Autor: {self.autor}.")

#3. Objetos e Atributos
#Dada a classe `Carro` abaixo:

class carro:
    def __init__(self, modelo, cor):   #Método inicializador da classe carro
        self.modelo = modelo
        self.cor = cor

#Crie um objeto `meu_carro` com modelo "Fusca" e cor "Azul". Em seguida, altere a cor
#para "Vermelho" e imprima o novo valor do atributo `cor`.

meu_carro = carro("Fusca", "Azul")
print(meu_carro.cor)
meu_carro.cor = "Vermelho"
print(meu_carro.cor)

#4. Funções com Múltiplos Parâmetros
#Escreva uma função `calcular_imc` que recebe peso (kg) e altura (m) e retorna o IMC
#(peso / altura2). Se o IMC for:
#- < 18.5: retorne "Abaixo do peso"
#- 18.5 a 24.9: retorne "Peso normal"
#- 25 a 29.9: retorne "Sobrepeso"
#- ≥ 30: retorne "Obesidade"
#Teste com peso 70 kg e altura 1.75 m.

def calcular_imc(peso, altura):     #Função para calcular IMC de acordo com questão.
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

class conta_bancaria:                   #Método inicializador da classe conta bancaria
    def __init__(self, saldo = 0):
        self.saldo = saldo

    def depositar(self, valor):         #Método para depositar dinheiro na conta
        if valor <= 0:
            print("O valor a ser depositado deve ser maior que zero.")
        elif valor > 0:
            self.saldo += valor
            print("Deposito realizado com sucesso.")
    
    def sacar(self, valor):              #Método para sacar dinheiro da conta
        if valor > self.saldo:
            print("Saldo insuficiente, tente um valor menor.")
        elif valor <= self.saldo:
            self.saldo -= valor
            print("Saque realizado com sucesso.")

conta_01 = conta_bancaria()
print(conta_01.saldo)
conta_01.depositar(100)
print(conta_01.saldo)
conta_01.sacar(30)
print(conta_01.saldo)


#6. Interação entre Objetos
#Crie uma classe `Pedido` com atributos `produto` e `quantidade`. Crie uma classe
#`Cliente` com atributo `nome` e um método `fazer_pedido(produto, quantidade)` que retorna
#um objeto `Pedido`. Faça um cliente "João" fazer um pedido de "Notebook" com quantidade 2.

class pedido:
    def __init__(self, produto, quantidade):        #Método inicializador da classe pedido
        self.produto = produto
        self.quantidade = quantidade

class cliente(pedido):                              #Classe cliente que interage com a classe pedido
    def __init__(self, nome):
        self.nome = nome

    def fazer_pedido(self, produto, quantidade):    #Método fazer_pedido que recebe os dados do pedido.
        return pedido(produto, quantidade)

joao = cliente("João")
pedido_de_joao = joao.fazer_pedido("Notebook", 2)
print(f"Cliente: {joao.nome}")
print(f"Produto: {pedido_de_joao.produto}")
print(f"Quantidade: {pedido_de_joao.quantidade}")


#7. Métodos Especiais
#Crie uma classe `Ponto` com atributos `x` e `y`. Implemente o método `__str__` para
#retornar `"(x, y)"` e o método `__add__` para permitir a soma de dois pontos (soma das
#coordenadas). Teste criando dois pontos (1, 2) e (3, 4), somando-os e imprimindo o resultado.

class ponto:
    def __init__(self, x, y):       #Método inicializador da classe ponto que recebe dois pontos em um sistema
        self.x = x                  #de coordenandas cartesianas
        self.y = y

    def __str__(self):
        return self.x, self.y

    def __add__(self, x, y):            #Método que soma os valores do pontos anteriores com novos.
        return self.x + x , self.y + y


#8. Classe com Lista de Objetos
#Crie uma classe `Turma` com atributo `alunos` (lista vazia). Adicione métodos:
#- `adicionar_aluno(aluno)`: adiciona um objeto `Aluno` à lista
#- `media_turma()`: calcula a média das notas de todos os alunos (cada aluno tem uma
#lista de notas)
#Use a classe `Aluno` da aula. Crie 3 alunos com notas [8,7,9], [6,5,7], [9,8,9], adicione-os
#à turma e calcule a média geral.

class turma:
    def __init__(self):         #Método inicializador da classe turma
        self.alunos = []        #lista de alunos vazia
        self.nota_aluno = []    #lista de notas
        self.media_aluno = []   #lista de media por aluno
        self.media_turma = 0    #média da turma


    def add_aluno(self, aluno, *notas):     #função para adicionar aluno a turma com as notas
        self.alunos.append(aluno)           #append para adicionar o aluno na lista de alunos
        self.nota_aluno.append(notas)       #append para adicionar as notas na lista de notas
        self.media_aluno.append(sum(notas)/len(notas))  #calcula a media do aluno e dá um append


    def cal_media_turma(self): #calcula a média da turma
        if self.nota_aluno:
            self.media_turma = sum(self.media_aluno)/len(self.media_aluno)
        else:
            print("A lista de médias está vazia!")

    def status(self):       #imprimi os detalhes da turma como lista de alunos, media por aluno e media da turma
        print(f"Alunos: {self.alunos}")
        print(f"Média por aluno: {self.media_aluno}")
        print(f"Média da turma: {self.media_turma}")

turma_01 = turma()      #instancia da classe turma com uma nova turma
turma_01.add_aluno("Junior", 8,7,9) #adiciona um aluno a turma com suas notas
turma_01.add_aluno("Camila", 6,5,7) #adiciona um aluno a turma com suas notas
turma_01.add_aluno("Bartosz", 9,8,9) #adiciona um aluno a turma com suas notas
turma_01.cal_media_turma()      #calcula  média da turma
turma_01.status()


#9. Composição de Objetos
#Crie uma classe `Motor` com atributo `potencia`. Crie uma classe `Carro` com atributos
#`modelo` e `motor` (objeto da classe `Motor`). Adicione um método `exibir_detalhes` que
#retorna `"Modelo: [modelo], Motor: [potencia] CV"`. Crie um motor de 150 CV, um carro
#"Ferrari" com esse motor, e exiba os detalhes.

class Motor:        
    def __init__(self, potencia):   #metodo inicializador da classe motor
        self.potencia = potencia



class Carro(Motor):
    def __init__(self, modelo, motor):      #metodo inicializador da classe carro que herda de motor
        self.modelo = modelo
        self.motor = motor

    def exibir_detalhes(self):              #exibi os detalhes do carro.
        return f'Modelo: {self.modelo}, Motor: {self.motor} CV.'
    

motor_ferrari = Motor(potencia=150)
Ferrari = Carro(modelo = "Ferrari", motor= motor_ferrari.potencia)
print(Ferrari.exibir_detalhes())


#Questão Desafio
#10. Sistema de Biblioteca
#Crie um sistema com as classes:
#- Livro: atributos `titulo`, `autor`, `disponivel` (True por padrão)
#- Biblioteca: atributo `livros` (lista de objetos `Livro`)
#- Usuario: atributo `nome` e método `emprestar_livro(biblioteca, titulo)` que:
#- Procura o livro na biblioteca
#- Se disponível, altera `disponivel` para False e retorna `"Livro emprestado com
#sucesso!"`
#- Senão, retorna `"Livro indisponível!"`
#Teste criando 3 livros, adicionando-os à biblioteca, e um usuário "Ana" emprestando um
#livro disponível e um indisponível.

class Livro:
    def __init__(self, titulo, autor):          # Método inicializador da classe Livro
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

class Biblioteca:   
    def __init__(self):                         #Método inicializador da classe Biblioteca
        self.livros = []

    def add_livro(self, livro):                 #funcçã para adicionar livro na lista livro da classe biblioteca
        #ADICIONA LIVRO A LISTA LIVROS.
        self.livros.append(livro)
        print(f"Livro '{livro.titulo}' adicionado à biblioteca.")
    
    def listar_livros_disponiveis(self):        #Função para listar todos os livros disponiveis na lista livros
        #LISTA TODOS OS LIVROS DA BIBLIOTECA
        livros_disponiveis = []
        for livro in self.livros:           #Itera sobre a lista livros e se disponivel adicionar a lista disponiveis
            if livro.disponivel:
                livros_disponiveis.append(livro)

        if livros_disponiveis:              #itera sobre a lista de disponiveis e retorna a lista.
            print("\nLivros Disponiveis:")
            for livro in livros_disponiveis:
                print(f"-{livro.titulo} por {livro.autor}")
        else:
            print(f"\nNão há livros disponíveis no momento.")

class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.livros_emprestados = []
    
    def emprestar_livro(self,biblioteca, titulo_livro):         #função para pegar livro emprestado
        livro_encontrado = None     #Lista de livros encontrados 

        for livro in biblioteca.livros:         #Verifica se o livro foi encontrado na lista de livros da biblioteca
            if livro.titulo.lower() == titulo_livro.lower():
                livro_encontrado = livro
                break

        if livro_encontrado:        #Se o livro for encontrado e estiver disponivel será colocado como indisponivel e taxado como emprestado
            if livro_encontrado.disponivel:
                livro_encontrado.disponivel = False
                self.livros_emprestados.append(livro_encontrado)
                print(f"{livro_encontrado.titulo} foi emprestado para {self.nome}")
            else:
                print(f"O livro {livro_encontrado.titulo} não está disponivel.")
        else:
            print(f"O livro {titulo_livro} não existe na biblioteca.")

    def devolver_livro(self, biblioteca, titulo_livro):     #Função para devolver livro a biblioteca e coloca-lo como disponivel novamente.
        livro_para_devolver = None
        for livro in self.livros_emprestados:
            if livro.titulo.lower() == titulo_livro.lower():
                livro_para_devolver = livro
                break

        if livro_para_devolver:
            livro_para_devolver.disponivel = True
            self.livros_emprestados.remove(livro_para_devolver)
            print(f"{livro_para_devolver.titulo} foi devolvido por {self.nome}.")
        else:
            print(f"Você não possui o livro {titulo_livro} para devolver.")


# --- Exemplo de uso ---

# Inicializa a biblioteca e adiciona alguns livros
minha_biblioteca = Biblioteca()
minha_biblioteca.add_livro(Livro("Python para data Science", "John Paul"))
minha_biblioteca.add_livro(Livro("Python para leigos", "Jonh Paul"))
minha_biblioteca.add_livro(Livro("O Senhor dos Anéis", "J.R.R. Tolkien"))

# Cria um usuário
usuario1 = Usuario("Junior")

# Lista os livros disponíveis
minha_biblioteca.listar_livros_disponiveis()

# Usuário empresta um livro
print("\n--- Ação de empréstimo ---")
usuario1.emprestar_livro(minha_biblioteca, "1984")

# Tenta emprestar o mesmo livro novamente
print("\n--- Tentando emprestar livro já emprestado ---")
usuario1.emprestar_livro(minha_biblioteca, "1984")

# Tenta emprestar um livro que não existe
print("\n--- Tentando emprestar livro inexistente ---")
usuario1.emprestar_livro(minha_biblioteca, "O Pequeno Príncipe")

# Lista os livros disponíveis após o empréstimo
minha_biblioteca.listar_livros_disponiveis()

# Usuário devolve o livro
print("\n--- Ação de devolução ---")
usuario1.devolver_livro(minha_biblioteca, "1984")

# Lista os livros disponíveis após a devolução
minha_biblioteca.listar_livros_disponiveis()


#NESTA ULTIMA QUESTÃO EU USEI O GEMINI DO GOOGLE PARA CONSEGUIR RESOLVER O PROBLEMA, NÃO CONSEGUI FAZER SOZINHO

class ContaBancaria:
    def __init__(self, titular, num_conta, saldo = 0 ): #Método inicializador da classe ContaBancaria
        self.titular = titular
        self.num_conta = num_conta
        self.saldo = saldo
        self.__extrato = {}

    def extrato(self):
        print("***** EXTRATO *****")
        if self.__extrato:
            for i,v in enumerate(self.__extrato):
                print(i, v)

    def depositar(self):                        #Depositar, se o saldo em conta for maior que 10 mil reais a cada novo deposito gaha-se um cash back de 5%
        print("***** DEPOSITAR *****")
        valor_deposito = float(input("Valor do deposito: R$"))
        if self.saldo > 10000:
            self.saldo += valor_deposito + (valor_deposito * 5/100)
            self.__extrato.update({"Deposito" :valor_deposito })
            print(f"Você recebeu 5% do valor depositado, por ter pelo menos 10 mil na conta.")
        else:
            self.saldo += valor_deposito
            print("Deposito realizado com sucesso!")

    def sacar(self):            #Método para sacar o saldo em conta
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
