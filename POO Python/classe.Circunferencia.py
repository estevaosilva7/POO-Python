class Circunferencia:
    def __init__(self, x, y, raio, cor_linha, cor_preenchimento):
        self.x = x
        self.y = y
        self.raio = raio
        self.cor_linha = cor_linha
        self.cor_preenchimento = cor_preenchimento

    #A área de um círculo é pi vezes o raio elevado ao quadrado (A = π r²)
    def area(self):
        area = 3.14* (self.raio * self.raio)
        print(f"Área da circunferência: {area}")

    # C = 2 * π * r.
    def perimetro(self):
       perimetro = 2*self.raio* 3.14
       print(f'Perímetro da circunferência: {perimetro}')

    def imprimir(self):
        print("Centro:", self.x, "e", self.y)
        print("Raio:", self.raio)
        print("Cor da linha:", self.cor_linha)
        print("Cor do preenchimento:", self.cor_preenchimento)


Ponto1 = Circunferencia(7, 2, 2, "Amarelo", "Rosa")

Ponto1.area()
Ponto1.perimetro()
print()
Ponto1.imprimir()