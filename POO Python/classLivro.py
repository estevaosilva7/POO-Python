class Livro:
    def __init__(self,genero, formato):
        self.genero=genero
        self.formato=formato

    def ler(self):
        print(f"Vamos ler um livro do gênero {self.genero} disponível no formato {self.formato}!")   


leitura1 = Livro("romance", "on-line")
leitura2 = Livro("fábula", "fisíco")

leitura1.ler()
leitura2.ler()