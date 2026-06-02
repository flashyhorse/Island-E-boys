import mysql.connector
from config import Config

def get_connection():
    try:
        conn = mysql.connector.connect(
            host=Config.HOST,
            user=Config.USUARIO,
            password=Config.SENHA,
            database=Config.BANCO
        )
        return conn
    except mysql.connector.Error as e:
        print(f"Erro ao conectar ao banco: {e}")
        return None
