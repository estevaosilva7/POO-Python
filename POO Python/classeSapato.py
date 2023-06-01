class Sapato():
    def __init__(self, marca , cor):
        self.marca=marca
        self.cor=cor

    def vender(self):
        print(f"Temos na loja hoje o modelo de tênis da marca {self.marca} nas cores {self.cor}!")    


Sapato1=Sapato("Nike", "vermelho")
Sapato2=Sapato("Rainha", "branco")

Sapato1.vender()
Sapato2.vender()