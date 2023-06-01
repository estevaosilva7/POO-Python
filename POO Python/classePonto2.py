class Ponto:
    def __init__(self, x, y, cor):
        self.x = x
        self.y = y
        self.cor = cor

    def alterar_cor(self, nova_cor):
        self.cor = nova_cor
    
    def imprimir(self):
        print(f"As coordenadas são {self.x} e {self.y} na cor {self.cor}!")

Ponto1 = Ponto(7,7,"Vermelho")
Ponto2 = Ponto(3,5, "Preta")


Ponto1.alterar_cor("Roxo")
Ponto2.alterar_cor("Verdinho")

Ponto1.imprimir()
Ponto2.imprimir()