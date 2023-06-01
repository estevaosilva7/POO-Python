from curso import Curso

class Aluno():

    contador = 0

    def __init__(self, matricula, nome, cpf, email):
        self.matricula = matricula
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.cursos = []

    def matricular(self, curso):
        self.cursos.append(curso)

    def imprimir(self):
        print(f'Aluno: {self.nome}, matrícula: {self.matricula}')
        print(f'CPF: {self.cpf}')
        print(f'E-mail: {self.email}')

    @classmethod
    def gerar_matricula(cls):
        cls.contador += 1
        return cls.contador        

matricula1 = Aluno.gerar_matricula()
aluno1 = Aluno(matricula1, 'Carlos', '123.456.789-01', 'carlos@gmail.com')
curso1 = Curso('CCO', 'Ciência da Computação', 'Curso de graduação em Ciência da Computação')
aluno1.matricular(curso1)