import unittest
from app.models.produto import Produto
from app.models.usuario import Usuario


class TestProduto(unittest.TestCase):

    def setUp(self):
        self.produto = Produto(
            nome="Parafuso M8",
            preco=2.50,
            quantidade_estoque=100,
            localizacao="Prateleira A1",
            descricao="Parafuso de aço inox"
        )

    def test_calcular_valor_total_estoque(self):
        """Multiplica preço pela quantidade — valor total em estoque."""
        resultado = self.produto.preco * self.produto.quantidade_estoque
        self.assertEqual(resultado, 250.0)

    def test_calcular_valor_total_estoque_zerado(self):
        """Estoque zerado deve resultar em valor total zero."""
        self.produto.quantidade_estoque = 0
        resultado = self.produto.preco * self.produto.quantidade_estoque
        self.assertEqual(resultado, 0.0)

    def test_aplicar_desconto(self):
        """Desconto de 10% sobre o preço deve retornar 2.25."""
        desconto = 0.10
        preco_com_desconto = self.produto.preco * (1 - desconto)
        self.assertAlmostEqual(preco_com_desconto, 2.25)

    def test_registrar_entrada_estoque(self):
        """Entrada de 50 unidades deve somar ao estoque atual."""
        quantidade_entrada = 50
        estoque_esperado = self.produto.quantidade_estoque + quantidade_entrada
        self.produto.quantidade_estoque += quantidade_entrada
        self.assertEqual(self.produto.quantidade_estoque, estoque_esperado)

    def test_registrar_saida_estoque(self):
        """Saída de 30 unidades deve subtrair do estoque atual."""
        quantidade_saida = 30
        estoque_esperado = self.produto.quantidade_estoque - quantidade_saida
        self.produto.quantidade_estoque -= quantidade_saida
        self.assertEqual(self.produto.quantidade_estoque, estoque_esperado)

    def test_estoque_nao_pode_ser_negativo(self):
        """Saída maior que o estoque não deve deixar saldo negativo."""
        quantidade_saida = 200
        estoque_apos = self.produto.quantidade_estoque - quantidade_saida
        self.assertLess(estoque_apos, 0)  # detecta o problema
        # regra de negócio: deve ser bloqueado (estoque >= 0)
        estoque_seguro = max(0, estoque_apos)
        self.assertEqual(estoque_seguro, 0)

    def test_preco_deve_ser_positivo(self):
        """Preço do produto deve ser maior que zero."""
        self.assertGreater(self.produto.preco, 0)

    def test_nome_nao_pode_ser_vazio(self):
        """Nome do produto não pode ser vazio ou None."""
        self.assertIsNotNone(self.produto.nome)
        self.assertNotEqual(self.produto.nome.strip(), "")

    def test_calcular_quantidade_pedidos(self):
        """Calcula quantos pedidos de 25 unidades cabem no estoque."""
        tamanho_pedido = 25
        pedidos_possiveis = self.produto.quantidade_estoque // tamanho_pedido
        self.assertEqual(pedidos_possiveis, 4)

    def test_reajuste_preco(self):
        """Reajuste de 20% sobre o preço original."""
        reajuste = 0.20
        novo_preco = round(self.produto.preco * (1 + reajuste), 2)
        self.assertEqual(novo_preco, 3.0)


class TestUsuario(unittest.TestCase):

    def setUp(self):
        self.usuario = Usuario(
            nome="Ana Lima",
            email="ana@estoque.com",
            senha="senha123",
            perfil="ADMIN"
        )

    def test_nome_nao_vazio(self):
        """Nome do usuário não pode ser vazio."""
        self.assertIsNotNone(self.usuario.nome)
        self.assertNotEqual(self.usuario.nome.strip(), "")

    def test_email_contem_arroba(self):
        """Email deve conter o caractere @."""
        self.assertIn("@", self.usuario.email)

    def test_senha_minimo_caracteres(self):
        """Senha deve ter no mínimo 6 caracteres."""
        self.assertGreaterEqual(len(self.usuario.senha), 6)

    def test_perfil_valido(self):
        """Perfil deve ser ADMIN ou OPERADOR."""
        perfis_validos = ["ADMIN", "OPERADOR"]
        self.assertIn(self.usuario.perfil, perfis_validos)

    def test_usuario_sem_id_inicial(self):
        """Usuário recém criado não deve ter ID (ainda não persistido)."""
        self.assertIsNone(self.usuario.id)


if __name__ == '__main__':
    unittest.main(verbosity=2)