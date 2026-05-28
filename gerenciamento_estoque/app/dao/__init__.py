# =========================
# DAO - Sistema de Estoque
# =========================

import mysql.connector


# =========================
# CONEXÃO COM O BANCO
# =========================
class Conexao:
    @staticmethod
    def conectar():
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="gerenciamento_estoque"
        )


# =========================
# DAO CATEGORIAS
# =========================
class CategoriaDAO:

    def inserir(self, nome, descricao):
        conexao = Conexao.conectar()
        cursor = conexao.cursor()

        sql = "INSERT INTO categorias(nome, descricao) VALUES(%s, %s)"
        valores = (nome, descricao)

        cursor.execute(sql, valores)
        conexao.commit()

        print("Categoria cadastrada!")

        cursor.close()
        conexao.close()

    def listar(self):
        conexao = Conexao.conectar()
        cursor = conexao.cursor()

        sql = "SELECT * FROM categorias"
        cursor.execute(sql)

        resultados = cursor.fetchall()

        cursor.close()
        conexao.close()

        return resultados

    def excluir(self, id_categoria):
        conexao = Conexao.conectar()
        cursor = conexao.cursor()

        sql = "DELETE FROM categorias WHERE id_categoria = %s"
        cursor.execute(sql, (id_categoria,))

        conexao.commit()

        cursor.close()
        conexao.close()


# =========================
# DAO FORNECEDORES
# =========================
class FornecedorDAO:

    def inserir(self, razao_social, cnpj, telefone, email, endereco):
        conexao = Conexao.conectar()
        cursor = conexao.cursor()

        sql = """
        INSERT INTO fornecedores
        (razao_social, cnpj, telefone, email, endereco)
        VALUES (%s, %s, %s, %s, %s)
        """

        valores = (razao_social, cnpj, telefone, email, endereco)

        cursor.execute(sql, valores)
        conexao.commit()

        print("Fornecedor cadastrado!")

        cursor.close()
        conexao.close()

    def listar(self):
        conexao = Conexao.conectar()
        cursor = conexao.cursor()

        sql = "SELECT * FROM fornecedores"
        cursor.execute(sql)

        resultados = cursor.fetchall()

        cursor.close()
        conexao.close()

        return resultados


# =========================
# DAO PRODUTOS
# =========================
class ProdutoDAO:

    def inserir(self, nome, descricao, preco,
                quantidade_estoque,
                id_categoria,
                id_fornecedor):

        conexao = Conexao.conectar()
        cursor = conexao.cursor()

        sql = """
        INSERT INTO produtos
        (nome, descricao, preco, quantidade_estoque,
        id_categoria, id_fornecedor)

        VALUES (%s, %s, %s, %s, %s, %s)
        """

        valores = (
            nome,
            descricao,
            preco,
            quantidade_estoque,
            id_categoria,
            id_fornecedor
        )

        cursor.execute(sql, valores)
        conexao.commit()

        print("Produto cadastrado!")

        cursor.close()
        conexao.close()

    def listar(self):
        conexao = Conexao.conectar()
        cursor = conexao.cursor()

        sql = """
        SELECT
            p.id_produto,
            p.nome,
            p.preco,
            p.quantidade_estoque,
            c.nome AS categoria,
            f.razao_social AS fornecedor

        FROM produtos p

        LEFT JOIN categorias c
            ON p.id_categoria = c.id_categoria

        LEFT JOIN fornecedores f
            ON p.id_fornecedor = f.id_fornecedor
        """

        cursor.execute(sql)

        resultados = cursor.fetchall()

        cursor.close()
        conexao.close()

        return resultados

    def atualizar_estoque(self, id_produto, nova_quantidade):
        conexao = Conexao.conectar()
        cursor = conexao.cursor()

        sql = """
        UPDATE produtos
        SET quantidade_estoque = %s
        WHERE id_produto = %s
        """

        valores = (nova_quantidade, id_produto)

        cursor.execute(sql, valores)
        conexao.commit()

        cursor.close()
        conexao.close()

    def excluir(self, id_produto):
        conexao = Conexao.conectar()
        cursor = conexao.cursor()

        sql = "DELETE FROM produtos WHERE id_produto = %s"

        cursor.execute(sql, (id_produto,))
        conexao.commit()

        cursor.close()
        conexao.close()


# =========================
# DAO USUÁRIOS
# =========================
class UsuarioDAO:

    def inserir(self, nome, login, senha, perfil):
        conexao = Conexao.conectar()
        cursor = conexao.cursor()

        sql = """
        INSERT INTO usuarios
        (nome, login, senha, perfil)

        VALUES (%s, %s, %s, %s)
        """

        valores = (nome, login, senha, perfil)

        cursor.execute(sql, valores)
        conexao.commit()

        print("Usuário cadastrado!")

        cursor.close()
        conexao.close()

    def autenticar(self, login, senha):
        conexao = Conexao.conectar()
        cursor = conexao.cursor()

        sql = """
        SELECT * FROM usuarios
        WHERE login = %s AND senha = %s
        """

        valores = (login, senha)

        cursor.execute(sql, valores)

        usuario = cursor.fetchone()

        cursor.close()
        conexao.close()

        return usuario


# =========================
# DAO ENTRADAS ESTOQUE
# =========================
class EntradaEstoqueDAO:

    def registrar(self, id_produto, quantidade):

        conexao = Conexao.conectar()
        cursor = conexao.cursor()

        # registra entrada
        sql = """
        INSERT INTO entradas_estoque
        (id_produto, quantidade)

        VALUES (%s, %s)
        """

        cursor.execute(sql, (id_produto, quantidade))

        # atualiza estoque
        sql_update = """
        UPDATE produtos
        SET quantidade_estoque =
        quantidade_estoque + %s

        WHERE id_produto = %s
        """

        cursor.execute(sql_update, (quantidade, id_produto))

        conexao.commit()

        print("Entrada registrada!")

        cursor.close()
        conexao.close()


# =========================
# DAO SAÍDAS ESTOQUE
# =========================
class SaidaEstoqueDAO:

    def registrar(self, id_produto, quantidade):

        conexao = Conexao.conectar()
        cursor = conexao.cursor()

        # registra saída
        sql = """
        INSERT INTO saidas_estoque
        (id_produto, quantidade)

        VALUES (%s, %s)
        """

        cursor.execute(sql, (id_produto, quantidade))

        # atualiza estoque
        sql_update = """
        UPDATE produtos
        SET quantidade_estoque =
        quantidade_estoque - %s

        WHERE id_produto = %s
        """

        cursor.execute(sql_update, (quantidade, id_produto))

        conexao.commit()

        print("Saída registrada!")

        cursor.close()
        conexao.close()


# =========================
# EXEMPLO DE USO
# =========================

produtoDAO = ProdutoDAO()

produtoDAO.inserir(
    "Notebook Dell",
    "Notebook i5 16GB",
    3500.00,
    10,
    1,
    1
)

produtos = produtoDAO.listar()

for produto in produtos:
    print(produto)