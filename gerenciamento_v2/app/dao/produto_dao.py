from app.dao.db_connection import get_connection

class ProdutoDAO:

    def inserir(self, produto):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            sql = """INSERT INTO produtos (nome, preco, quantidade, localizacao)
                     VALUES (%s, %s, %s, %s)"""
            cursor.execute(sql, (produto.nome, produto.preco,
                                 produto.quantidade, produto.localizacao))
            conn.commit()
            return True
        except Exception as e:
            print(f"Erro ao inserir produto: {e}")
            return False
        finally:
            cursor.close()
            conn.close()

    def listar(self):
        conn = get_connection()
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM produtos ORDER BY id DESC")
            return cursor.fetchall()
        except Exception as e:
            print(f"Erro ao listar produtos: {e}")
            return []
        finally:
            cursor.close()
            conn.close()