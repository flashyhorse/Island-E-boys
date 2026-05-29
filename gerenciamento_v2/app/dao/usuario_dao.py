from app.dao.db_connection import get_connection

class UsuarioDAO:

    def inserir(self, usuario):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            sql = "INSERT INTO usuario (nome, email, senha, perfil) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (usuario.nome, usuario.email, usuario.senha, usuario.perfil))
            conn.commit()
            return True
        except Exception as e:
            print(f"Erro ao inserir usuário: {e}")
            return False
        finally:
            cursor.close()
            conn.close()

    def buscar_por_email(self, email):
        conn = get_connection()
        try:
            cursor = conn.cursor(dictionary=True)
            sql = "SELECT * FROM usuario WHERE email = %s"
            cursor.execute(sql, (email,))
            return cursor.fetchone()
        except Exception as e:
            print(f"Erro ao buscar usuário: {e}")
            return None
        finally:
            cursor.close()
            conn.close()
