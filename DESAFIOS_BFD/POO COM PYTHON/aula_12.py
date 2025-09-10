class carro:
    def __init__(self, marca, modelo, velocidade = 0, ligado = False):
        self.marca = marca
        self.modelo = modelo
        self.velocidade = velocidade
        self.ligado = ligado

    def ligar_motor(self):
        print("VRUUUUUMMM!!!")
        self.ligado =True
    
    def desligar(self):
        if self.velocidade > 0:
            print("Velocidade maior que 0 não pode desligar.")
        else:
            self.ligado = False

    def acelerar(self):
        if self.ligado:
            if self.velocidade < 50:
                self.velocidade += 10
            else:
                print("Limite de velocidade atingido.")
        else:
            print("Para acelerar o carro você precisa ligar o motor.")
    
    def frear(self):
        if self.ligado and self.velocidade > 0:
            self.velocidade -= 10
        elif self.ligado == False:
            print("O carro esta desligado.")
        elif self.velocidade == 0:
            print("O carro já esta parado.")
    
    def status(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ligado: {self.ligado}")
        print(f"Velocidade atual: {self.velocidade}")

class livro:
    def __init__(self, titulo, autor, pagina):
        self.titulo = titulo
        self.autor = autor
        self.pagina = pagina

    def exibir_dados(self):
        print(f"Titulo: {self.titulo}, Autor: {self.autor}. Página: {self.pagina}")

meu_livro = livro("1984", "Goerg", 15)
meu_livro.exibir_dados()
