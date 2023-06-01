class Vaca:
    def __init__(self, registro = None, raca = None, cor = None, tamanho = None, idade = None, peso = None):
        self.registro = registro
        self.raca = raca
        self.cor = cor
        self.tamanho = tamanho
        self.idade = idade
        self.peso = peso
    
    #O nome da vaca foi especificado
    def comer(self, alimento, quantidade):
        self.peso+= 0.05*quantidade
        print(f'A vaca {self.registro} comeu', str(quantidade),'Kg de', alimento,'.')
 
    #Coloquei para aparecer o nome da vaca pelo registro quando o metódo funcionar.
    def ruminar(self):
        print(f'Vaca {self.registro} estar ruminando. ')
    
    # Tinha o número "1" aqui no código do slide e tirei porque ficou estranho no prints, também coloquei para aparecer o nome da vaca.
    def produzir_leite(self):
        leite = self.peso * 0.02
        print(f"A vaca {self.registro} produziu ", str(leite), "de leite!")
        return leite
    
    #O nome da vaca foi especificado
    def caminhar(self, distancia):
        print(f"A vaca {self.registro} caminhou",str(distancia),"metros")

    def imprimir(self):
        print("Registro: ", self.registro)
        print("Raça: ", self.raca)
        print("Cor: ", self.cor)
        print("Tamanho: ", self.tamanho)
        print("Idade: ", self.idade)
        print("Peso: ", self.peso)

Mimosa = Vaca ("Mimosa", "Holandesa",  "preta e benca", "1,40 m", "2 anos", 700)
Docinho = Vaca ("Docinho", "Jersey", "preta", "1,6 m", "2 anos", 800)
print()

Mimosa.comer('Ovo', 500)
Docinho.comer('Capim', 700)
print()

Mimosa.ruminar()
Docinho.ruminar()
print()

Mimosa.produzir_leite()
Docinho.produzir_leite()
print()

Mimosa.caminhar(500)
Docinho.caminhar(700)
print()

Mimosa.imprimir()
print()
Docinho.imprimir()
print()