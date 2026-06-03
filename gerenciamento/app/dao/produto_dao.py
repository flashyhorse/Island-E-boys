from app.dao.db_connection import get_connection

class ProdutoDAO:

    def inserir(self, produto):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            sql = """INSERT INTO produtos (nome, descricao, preco, quantidade_estoque, localizacao)
                     VALUES (%s, %s, %s, %s, %s)"""
            cursor.execute(sql, (produto.nome, produto.descricao, produto.preco,
                                 produto.quantidade_estoque, produto.localizacao))
            id_produto = cursor.lastrowid
            conn.commit()
            return id_produto
        except Exception as e:
            print(f"Erro ao inserir produto: {e}")
            return None
        finally:
            cursor.close()
            conn.close()

    def listar(self):
        conn = get_connection()
        try:
            cursor = conn.cursor(dictionary=True)
            sql = """
                SELECT
                    p.id_produto,
                    p.nome,
                    p.descricao,
                    p.preco,
                    p.quantidade_estoque,
                    p.localizacao,
                    MAX(e.data_entrada) AS data_entrada,
                    MAX(s.data_saida)   AS data_saida
                FROM produtos p
                LEFT JOIN entradas_estoque e ON e.id_produto = p.id_produto
                LEFT JOIN saidas_estoque   s ON s.id_produto = p.id_produto
                GROUP BY p.id_produto
                ORDER BY p.id_produto DESC
            """
            cursor.execute(sql)
            return cursor.fetchall()
        except Exception as e:
            print(f"Erro ao listar produtos: {e}")
            return []
        finally:
            cursor.close()
            conn.close()