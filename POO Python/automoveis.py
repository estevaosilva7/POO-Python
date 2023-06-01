class Motor:
    def __init__(self, num_cilindro = 0, potencia = 0):
        self._num_cilindro = num_cilindro
        self._potencia = potencia

    @property
    def num_cilindro(self):
        return self._num_cilindro
        
    @num_cilindro.setter
    def num_cilindro(self, value):
        self._num_cilindro = value

    @property
    def potencia(self):
        return self._potencia
        
    @potencia.setter
    def potencia(self, value):
        self._potencia = value

    def __str__(self):
        return (f'Número de cilindros: {self._num_cilindro} \nPotência: {self._potencia}')
    
class Veiculo:
    def __init__(self, peso=0, velocidade_maxima=0, preco=0):
        self._peso = peso
        self._velocidade_maxima = velocidade_maxima
        self._preco = preco

    @property
    def peso(self):
        return self._peso
        
    @peso.setter
    def peso(self, value):
        self._peso = value

    @property
    def velocidade_maxima(self):
        return self._velocidade_maxima
        
    @velocidade_maxima.setter
    def velocidade_maxima(self, value):
        self._velocidade_maxima = value

    @property
    def preco(self):
        return self._preco 
        
    @preco.setter
    def preco(self, value):
        self._preco = value

    def __str__(self):
        return (f'Peso: {self._peso}Kg\nVelocidade Máxima: {self._velocidade_maxima}Km\nPreço: {self._preco}R$')


class CarroPasseio(Motor, Veiculo):
    def __init__(self,num_cilindro = 0, potencia = 0, peso=0, velocidade_maxima=0, preco=0, cor = str, modelo = str):
        Motor.__init__(self, num_cilindro, potencia)
        Veiculo.__init__(self, peso, velocidade_maxima, preco)
        self._cor = cor
        self._modelo = modelo

    @property
    def cor(self):
        return self._cor
    
    @cor.setter
    def cor(self, value):
        self._cor = value

    @property
    def modelo(self):
        return self._modelo
    
    @modelo.setter
    def modelo(self, value):
        self._modelo = value

    def __str__(self):
        return (f'{Motor.__str__(self)}\n{Veiculo.__str__(self)}\nCor: {self._cor}\nModelo: {self._modelo}')
    

class Caminhao(Motor, Veiculo):
    def __init__(self, num_cilindro=0, potencia=0, peso=0, velocidade_maxima=0, preco=0, toneladas=0,altura_maxima=0, comprimento=0):
        Motor.__init__(self, num_cilindro, potencia)
        Veiculo.__init__(self, peso, velocidade_maxima, preco)
        self._toneladas = toneladas
        self._altura_maxima = altura_maxima
        self._comprimento = comprimento

    @property
    def toneladas(self):
        return self._toneladas
    
    @toneladas.setter
    def toneladas(self, value):
        self._toneladas = value

    @property
    def altura_maxima(self):
        return self._altura_maxima
    
    @altura_maxima.setter
    def altura_maxima(self, value):
        self._altura_maxima = value

    @property
    def comprimento(self):
        return self._comprimento
    
    @comprimento.setter
    def comprimento(self, value):
        self._comprimento = value

    def __str__(self):
        return (f'{Motor.__str__(self)}\n{Veiculo.__str__(self)}\nToneladas: {self._toneladas}Kg\nAltura Maáxima: {self._altura_maxima}m\nComprimento: {self._comprimento}m')



    
motor1 = Motor()
motor1.num_cilindro = 4
motor1.potencia = 200
print(motor1)

print()

veiculo1 = Veiculo(350, 120, 1000)
print(veiculo1)

print()

carro1 = CarroPasseio(4, 250, 450, 10000, 500, 'Vermelho', 'Volvo')
print(carro1)

print()

caminhao1 = Caminhao(8, 400, 5000, 120, 100000, 10, 3, 10)
print(caminhao1)
    

    


            