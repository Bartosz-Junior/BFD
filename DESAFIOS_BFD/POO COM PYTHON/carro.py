class carros:
    def __init__(self, modelo, ano, ligado=False):
        self.modelo = modelo
        self.ano = ano
        self.ligado = ligado

    def ligar(self):
        print("VRUUUUUM!")
        self.ligado = True

    def status(self):
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")
        print(f"Ligado: {self.ligado}")

uno = carros("Fiat Uno", 2000)
uno.ligar()
uno.status()
