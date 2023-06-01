class Professor():
    def __init__(self, nome, materia):
        self.nome=nome
        self.materia=materia

    def aula(self):
        print(f"O professor {self.nome} vai dar aula de {self.materia} na faculdade!")

Professor1=Professor("Augusto", "Redes")
Professor2=Professor('Ana', "Banco de Dados")   

Professor1.aula()
Professor2.aula()