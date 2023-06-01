class Produto:
    def __init__(self, id_produto, nome_produto, descricao, valor_unitario, unidade_medida):
        self._id_produto= id_produto
        self._nome_produto = nome_produto
        self._descricao = descricao
        self._valor_unitario = valor_unitario
        self._unidade_medida = unidade_medida
    
    @property
    def id_produto(self):
        return self._id_produto
    
    @id_produto.setter
    def id_produto(self, id_produto):
        self._id_produto = id_produto

    @property
    def nome_produto(self):
        return self._nome_produto
    
    @nome_produto.setter
    def nome_produto(self, nome_produto):
        self._nome_produto = nome_produto
    
    @property
    def descricao(self):
        return self._descricao
    
    @descricao.setter
    def descricao(self, descricao):
        self._descricao = descricao

    @property
    def valor_unitario(self):
        return self._valor_unitario
    
    @valor_unitario.setter
    def valor_unitario(self, valor_unitario):
        self._valor_unitario = valor_unitario

    @property
    def unidade_medida(self):
        return self._unidade_medida
    
    @unidade_medida.setter
    def unidade_medida(self, unidade_medida):
        self._unidade_medida = unidade_medida

class Fornecedor:
    def __init__(self, id_fornecedor, nome_fornecedor):
        self._id_fornecedor = id_fornecedor
        self._nome_fornecedor = nome_fornecedor

    @property
    def id_fornecedor(self):
        return self._id_fornecedor
    
    @id_fornecedor.setter
    def id_fornecedor(self, id_fornecedor):
        self._id_fornecedor = id_fornecedor

    @property
    def nome_fornecedor(self):
        return self._nome_fornecedor

    @nome_fornecedor.setter
    def nome_fornecedor(self, nome_fornecedor):
        self._nome_fornecedor = nome_fornecedor

class Cotacao:
    def __init__(self, id_cotacao, produto, quantidade, data, nome_solicitante, fornecedor, valor_total):
        self._id_cotacao = id_cotacao
        self._produto = produto
        self._quantidade = quantidade
        self._data = data
        self._nome_solicitante = nome_solicitante
        self._fornecedor = fornecedor
        self._valor_total = produto.valor_unitario * quantidade

    @property
    def id_cotacao(self):
        return self._id_cotacao
    
    @id_cotacao.setter
    def id_cotacao(self, id_cotacao):
        self._id_cotacao = id_cotacao

    @property
    def produto(self):
        return self._produto
    
    @produto.setter
    def produto(self, produto):
        self._produto = produto

    @property
    def quantidade(self):
        return self._quantidade
    
    @quantidade.setter
    def quantidade(self, quantidade):
        self._quantidade = quantidade

    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self, data):
        self._data = data

    @property
    def nome_solicitante(self):
        return self._nome_solicitante
    
    @nome_solicitante.setter
    def nome_solicitante(self, nome_solicitante):
        self._nome_solicitante = nome_solicitante

    @property
    def fornecedor(self):
        return self._fornecedor
    
    @fornecedor.setter
    def fornecedor(self, fornecedor):
        self._fornecedor = fornecedor

    @property
    def valor_total(self):
        return self._valor_total
    
    @valor_total.setter
    def valor_total(self, valor_total):
        self._valor_total = valor_total
    def __str__(self):
        return f"Cotação {self.id} - {self.produto.nome} ({self.produto.unidade_medida}): {self.quantidade} " \
               f"Unidades  {self.produto.valor_unitario:.2f} cada, fornecedor {self.fornecedor.nome} - " \
               f"Total: R${self.valor_total:.2f}"

class Orcamento:
    def __init__(self, nome_obra, descricao_reforma):
        self._nome_obra = nome_obra
        self._descricao_reforma = descricao_reforma
        self._cotacos_realizadas = []

    def cadastrar_cotacao(self, cotacao):
        self._cotacoes.append(cotacao)

    def cotacao_menor_valor(self):
        if not self._cotacoes:
            return None
        return min(self._cotacoes, key=lambda c: c.valor_total)
    
    def buscar_cotacao_fornecedor(self, fornecedor):
        return [c for c in self.__cotacoes if c.fornecedor == fornecedor]
    
    def listar_cotacoes(self):
        for c in self.__cotacoes:
            print(f"Cotação {c.id}: {c.produto.nome} - Quantidade: {c.quantidade} - Fornecedor: {c.fornecedor.nome} - Valor Total: R$ {c.valor_total:.2f}")
    
    def listar_cotacoes_por_faixa_preco(self, valor_minimo, valor_maximo):
        for c in self.__cotacoes:
            if valor_minimo <= c.valor_total <= valor_maximo:
                print(f"Cotação {c.id}: {c.produto.nome} - Quantidade: {c.quantidade} - Fornecedor: {c.fornecedor.nome} - Valor Total: R$ {c.valor_total}:.2f")


produto1 = Produto(id_produto=1, nome_produto="Martelo", descricao="Ferramenta utilizada para bater em pregos", valor_unitario=20.0, unidade_medida="Unidade")
print()

fornecedor1 = Fornecedor(id_fornecedor=1, nome_fornecedor="Fornecedor 1")
print()

cotacao1 = Cotacao(id_cotacao=1, produto=produto1, quantidade=10, data="2022-01-01", nome_solicitante="João", fornecedor=fornecedor1, valor_total=200.0)
print()

orcamento = Orcamento(nome_obra="Reforma da cozinha", descricao_reforma="Reforma completa da cozinha")
print()

