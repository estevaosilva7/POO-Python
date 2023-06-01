class Ingresso:
    contador_id = 0

    def __init__(self, valor):
        self._id = __class__.gerar_id()
        self._valor = valor
        self._status = 'Disponível'

    @staticmethod
    def gerar_id():
        Ingresso.contador_id += 1
        return Ingresso.contador_id

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor):
        self._valor = valor

    def __str__(self):
        return (f'Código: {self._id}\nValor: {self._valor}\nStatus: {self._status}')
    
class Camarote(Ingresso):
    def __init__(self, valor, adcional):
        self._camarote = valor + adcional
        super().__init__(valor)
        
    def __str__(self):
        return (f'Código: {self._id}\nValor: {self._camarote}\nStatus: {self._status}')


class Show:
    def __init__(self, nome, data, local):
        self._nome = nome
        self._data = data
        self._local = local
        self._lista_pista = []
        self._lista_camarote = []
        self._total_arrecadado = 0

    def gerarIngressos(self, quantidade, valor, tipo=None):
        if tipo == 1:
            adicional = int(input("Informe o valor adicional para o camarote: "))
            for _ in range(quantidade):
                self._lista_camarote.append(valor + adicional)
        else:
            for _ in range(quantidade):
                self._lista_pista.append(valor)

    def venderIngresso(self, quantidade, tipo=None):
        valor_total = 0
        if tipo == 1:
            if len(self._lista_camarote) < quantidade:
                print("Quantidade de ingressos de camarote insuficiente.")
                return
            for _ in range(quantidade):
                valor_total += self._lista_camarote.pop(0)
        else:
            if len(self._lista_pista) < quantidade:
                print("Quantidade de ingressos de pista insuficiente.")
                return
            for _ in range(quantidade):
                valor_total += self._lista_pista.pop(0)

        self._total_arrecadado += valor_total
        return valor_total

    def relatorioVendas(self):
        print(f"Dados do Show:\nArtista: {self._nome}\nData: {self._data}\nLocal: {self._local}\n")
        print("Relatório de Vendas:")
        print("Ingressos de Pista Vendidos:")
        for ingresso_pista in self._lista_pista:
            print(f"Ingresso de Pista - Valor: {ingresso_pista} - Status: Vendido")
        print("\nIngressos de Camarote Vendidos:")
        for ingresso_camarote in self._lista_camarote:
            print(f"Ingresso de Camarote - Valor: {ingresso_camarote} - Status: Vendido")
        print(f"\nTotal arrecadado com a venda de ingressos: {self._total_arrecadado}")

    
    
    
show1=Show('Aviões do forró', '23/06/2022','Arena Aracaju')
show1.gerarIngressos(5,80) #ingresso pista
show1.gerarIngressos(5,80,1) #ingresso camarote
print(show1)
print('Valor a pagar por 2 ingressos pista: R$ ',show1.venderIngresso(2)) # dois ingressos pista
print('Valor a pagar por 1 ingressos VIP: R$ ',show1.venderIngresso(1,1)) # um ingresso VIP
show1.relatorioVendas()
print('Valor a pagar por 2 ingressos VIP: R$ ',show1.venderIngresso(2,1)) # dois ingressos VIP
show1.relatorioVendas()