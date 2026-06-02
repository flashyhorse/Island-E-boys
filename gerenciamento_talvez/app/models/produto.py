class Produto:
    def __init__(self, nome, preco, quantidade_estoque, localizacao, descricao=None, id_produto=None):
        self.id_produto = id_produto
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.quantidade_estoque = quantidade_estoque
        self.localizacao = localizacao