class Config:
    # Flask
    SECRET_KEY = '0416090b2eebed2738990a702d3814e4d2933f8dc3983a5e00b234135fe35f43'
    DEBUG = True

    # MySQL
    DB_HOST = 'localhost'
    DB_USER = 'root'
    DB_PASSWORD = ''
    DB_NAME = 'init_db'
    DB_PORT = 3306

    # Sessão do Usuário
    SESSION_PERMANENT = False

    # Estoque: Regras de Negócio
    ESTOQUE_MINIMO_PADRAO = 10