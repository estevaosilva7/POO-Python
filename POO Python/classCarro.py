class Carro:
    def __init__(self, modelo, cor):
        self.modelo=modelo
        self.cor=cor

    def acelerar(self):
        print(f"O carro {self.modelo} {self.cor} foi o que mais acelerou na corrida!")

carro1 = Carro("Mercedes", "branco")    
carro2 = Carro("Ford", "preto") 

carro1.acelerar()
carro2.acelerar()

