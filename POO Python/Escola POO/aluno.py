class Aluno:
    matricula_atual = 0

    def __init__(self,nome, cpf, email):
        self.matricula = Aluno.gerar_matricula()
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.cursos = []

    @classmethod
    def gerar_matricula(cls):
        cls.matricula_atual += 1
        return cls.matricula_atual

    def matricular(self, curso):
        self.curso.append(curso)

    def imprimir(self):
        print(f'Matricula: {self.matricula}')
        print(f'Nome: {self.nome}')
        print(f'CPF: {self.cpf}')
        print(f'E-mail: {self.email}')
        print(f'Cursos:')
        for curso in self.cursos:
            print(f'- {curso.nome}')

    
aluno1 = Aluno ('Arthur','123,456.789-12', 'arthur@gmail.com')
aluno1.imprimir()
aluno1.gerar_matricula()
        
        