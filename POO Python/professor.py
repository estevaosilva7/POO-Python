from curso import Curso

class Professor:
    
    contador = 0
    
    def __init__(self, matricula, nome, cpf, admissao, email, lotacao):
        self.matricula = matricula
        self.nome = nome
        self.cpf = cpf
        self.admissao = admissao
        self.email = email
        self.lotacao = None

    def set_lotacao(self, curso):
        self.lotacao = curso
        
    def imprimir(self):
        print(f'Matrícula: {self.matricula}')
        print(f'Nome: {self.nome}')
        print(f'CPF: {self.cpf}')
        print(f'Admissão: {self.admissao}')
        print(f'E-mail: {self.email}')   
        print(f'Lotação')
        print(f' Código: {self.lotacao.codigo}')
        print(f'Nome: {self.lotacao.descricao}')
        print(f'Descrição: {self.lotacao.descricao}')
        print(f'Descrição: {self.lotacao.descricao}')
        print(f'Docentes')
        for professor in self.lotacao.docentes:
            print(f' -{professor.nome}')
    
    @classmethod
    def gerar_matricula(cls):
        cls.contador += 1
        return cls.contador


professor1 = Professor('João', '123.456.789-00', 'joao@gmail.com')
curso1 = Curso('CCO', 'Ciência da Computação', 'Curso de graduação em Ciência da Computação', professor1)
curso1.imprimir()