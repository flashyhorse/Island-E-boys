from app.dao.db_connection import get_connection

class EstoqueDAO:

    def registrar_entrada(self, id_produto, quantidade):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO entradas_estoque (id_produto, quantidade) VALUES (%s, %s)",
                (id_produto, quantidade)
            )
            cursor.execute(
                "UPDATE produtos SET quantidade_estoque = quantidade_estoque + %s WHERE id_produto = %s",
                (quantidade, id_produto)
            )
            conn.commit()
            return True
        except Exception as e:
            print(f"Erro ao registrar entrada: {e}")
            return False
        finally:
            cursor.close()
            conn.close()

    def registrar_saida(self, id_produto, quantidade):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO saidas_estoque (id_produto, quantidade) VALUES (%s, %s)",
                (id_produto, quantidade)
            )
            cursor.execute(
                "UPDATE produtos SET quantidade_estoque = quantidade_estoque - %s WHERE id_produto = %s",
                (quantidade, id_produto)
            )
            conn.commit()
            return True
        except Exception as e:
            print(f"Erro ao registrar saída: {e}")
            return False
        finally:
            cursor.close()
            conn.close()