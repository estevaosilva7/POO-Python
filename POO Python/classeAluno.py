class Aluno():
    def __init__(self,nome,curso,turno):
        self.nome=nome
        self.curso=curso
        self.turno=turno

    def matricula(self):
        print(f"O aluno {self.nome} estuda {self.curso} no turno da {self.turno}!")   


Aluno1=Aluno("João", "Admintração","noite")  
Aluno2=Aluno("Caio", "Economia" ,"tarde")

Aluno1.matricula()
Aluno2.matricula()
