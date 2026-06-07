class Produto:
    def __init__(self, nome, preco, quantidade, localizacao, id=None):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.localizacao = localizacao