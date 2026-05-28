from flask import Flask
from config import Config

def create_app(config=Config):
    app = Flask(__name__)
    app.config.from_object(config)

    # Registrar controllers aqui quando estiverem prontos
    # from app.controllers.usuario_controller import usuario
    # app.register_blueprint(usuario)

    return app