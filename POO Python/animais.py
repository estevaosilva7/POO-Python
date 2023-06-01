class Animal:
    def __init__(self, nome, comprimento, nr_patas, cor, ambiente, velocidade):
        self._nome = nome
        self._comprimento = comprimento
        self._nr_patas = nr_patas
        self._cor = cor
        self._ambiente = ambiente
        self._velocidade = velocidade


class Mamifero(Animal):
    def __init__(self, alimento, nome, comprimento, nr_patas, cor, ambiente, velocidade):
            self._alimento = alimento
            super().__init__(nome, comprimento, nr_patas, cor, ambiente, velocidade)
   
    def dados_Mamifero(self):
        print(f'Alimento: {self._alimento}')
        print(f'Nome: {self._nome}')
        print(f'Comprimento: {self._comprimento}')
        print(f'Número de patas: {self._nr_patas}')
        print(f'Cor: {self._cor}')
        print(f'Ambiente: {self._ambiente}')
        print(f'Velocidade: {self._velocidade}')
       


class Peixe(Animal):
    def __init__(self,caracteristica,nome, comprimento, nr_patas, cor, ambiente, velocidade):
        self._caracteristica = caracteristica
        super().__init__(nome, comprimento, nr_patas, cor, ambiente, velocidade)


    def dados_Peixe(self):
        print(f'Alimento: {self._caracteristica}')
        print(f'Nome: {self._nome}')
        print(f'Comprimento: {self._comprimento}')
        print(f'Número de patas: {self._nr_patas}')
        print(f'Cor: {self._cor}')
        print(f'Ambiente: {self._ambiente}')
        print(f'Velocidade: {self._velocidade}')
       


animal1 = Mamifero('banana', 'macaco', '2m', '4', 'preto', 'selva', '45km')
animal1.dados_Mamifero()
print()
animal2 = Peixe('Agúa doce', 'Sardinha', '4m', '0', 'Azul', 'Aquático', '80km')
animal2.dados_Peixe()


