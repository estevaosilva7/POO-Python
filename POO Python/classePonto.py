class Ponto:
    def __init__(self, x,y):
        self.x=x
        self.y=y

    def __str__(self):
        return f"({self.x}, {self.y})"



ponto1= Ponto(7,8)
ponto2= Ponto(1,2)

print("Coordenadas do ponto 1:", ponto1)
print("Coordenadas do ponto 2:", ponto2)