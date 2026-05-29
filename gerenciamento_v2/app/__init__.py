from flask import Flask
from config import Config

def create_app():
    app = Flask(__name__)
    app.secret_key = Config.SECRET_KEY

    from app.controllers.usuario_controller import usuario_bp
    app.register_blueprint(usuario_bp)

    return app
