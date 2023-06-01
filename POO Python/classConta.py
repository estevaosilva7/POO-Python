class Conta:
    def __init__(self, numero, tipo):
        self.numero=numero
        self.tipo=tipo

    def saque(self):
        print(f"Solicito um saque da conta: {self.numero} do tipo {self.tipo}!")


saque1 = Conta("777-000", "corrente")
saque2 = Conta("123-456", "poupança")  

saque1.saque()
saque2.saque()