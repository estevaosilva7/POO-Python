class Curso:
    
    contador = 0
    
    def __init__(self, codigo, nome, descricao):
        self.codigo = codigo
        self.nome = nome
        self.descricao = descricao
        self.coordenador = None
        self.docentes = []
        self.id = Curso.gerar_codigo()
        
    @classmethod
    def gerar_codigo(cls):
        cls.contador += 1
        return cls.contador
    
    def definir_coordenador(self, coordenador):
        self.coordenador = coordenador

    def adicionar_docente(self, professor):
        self.docentes.append(professor)

    def imprimir(self):
        print(f'Código: {self.codigo}')
        print(f'Nome: {self.nome}')
        print(f'Descrição: {self.descricao}')
        if self.coordenador:
            print(f'Coordenador: {self.coordenador.nome}')
        else:
            print('Coordenador não definido')
        print(f'Docentes:')
        for professor in self.docentes:
            print(f'- {professor.nome}')


curso1 = Curso('CCO', 'Ciência da Computação', 'Curso de graduação em Ciência da Computação')
curso1.definir_coordenador('André')
curso1.adicionar_docentes('Luiz, Livía, Arthur')
curso1.imprimir()

