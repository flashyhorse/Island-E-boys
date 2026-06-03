import bcrypt
from app.dao.db_connection import get_connection

class UsuarioDAO:

    def inserir(self, usuario):
        conn = get_connection()
        try:
            senha_hash = bcrypt.hashpw(
                usuario.senha.encode('utf-8'),
                bcrypt.gensalt()
            ).decode('utf-8')

            cursor = conn.cursor()
            sql = "INSERT INTO usuario (nome, email, senha, perfil) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (usuario.nome, usuario.email, senha_hash, usuario.perfil))
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

    def verificar_senha(self, senha_digitada, senha_hash):
        return bcrypt.checkpw(
            senha_digitada.encode('utf-8'),
            senha_hash.encode('utf-8')
        )
