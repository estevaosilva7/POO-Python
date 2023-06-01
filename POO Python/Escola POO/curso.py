from professor import Professor

class Curso:
    gerar_codigo = 0

    def __init__(self, nome, descricao, coordenador = None):
        self.codigo = Curso.gerar_novo_codigo()
        self.nome = nome
        self.descricao = descricao 
        self.coordenador = coordenador
        self.docentes = []

    @classmethod
    def gerar_novo_codigo(cls):
        cls.gerar_codigo += 1
        return cls.gerar_codigo

    def definir_coordenador(self, coordenador):
        self.coordenador = coordenador

    def add_docente(self, professor):
        self.docentes.append(professor)

    def imprimir(self):
        print(f'Código: {self.codigo}')
        print(f'Nome: {self.nome}')
        print(f'Descrição: {self.descricao}')
        print(f'Coordenador: {self.coordenador.nome}')
        print('Docentes: ')
        for professor in self.docentes:
            print(f'- {professor.nome}')

prof1 = Professor ('0202', 'Marcelo', '789.456.123-00','01/01/2022', 'marcelo@gmai.com', 'ADS')
cuso1 = Curso ('ADS', 'Tecnólogo')
cuso1.definir_coordenador(prof1)
cuso1.add_docente(prof1)
cuso1.imprimir()



        
