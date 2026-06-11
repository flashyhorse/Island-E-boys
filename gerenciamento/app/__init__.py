from flask import Flask, render_template
from config import Config

def create_app():
    app = Flask(__name__)
    app.secret_key = Config.SECRET_KEY

    from app.controllers.usuario_controller import usuario_bp
    app.register_blueprint(usuario_bp)

    from app.controllers.produto_controller import produto_bp
    app.register_blueprint(produto_bp)

    @app.errorhandler(403)
    def acesso_negado(e):
        return render_template('403.html'), 403

    return app