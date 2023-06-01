
class Professor:
    def __init__(self, matricula, nome, cpf, admissao, email, lotacao):
        self.matricula = matricula
        self.nome = nome
        self.cpf = cpf
        self.admissao = admissao
        self.email = email
        self.lotacao = lotacao

    def set_lotacao(self, curso):
        self.lotacao = curso

    def imprimir(self):
        print(f'Matrícula: {self.matricula}')
        print(f'Nome: {self.nome}')
        print(f'CPF: {self.cpf}')
        print(f'Adimissão: {self.admissao}')
        print(f'E-mail: {self.email}')
        print(f'Lotação: {self.lotacao}')


prof1 = Professor ('0202', 'Marcelo', '789.456.123-00','01/01/2022', 'marcelo@gmai.com', 'ADS')
prof1.imprimir()
prof1.set_lotacao('ADS')
 