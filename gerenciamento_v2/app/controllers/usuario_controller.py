from flask import Blueprint, render_template, request, redirect, url_for
from app.models.usuario import Usuario
from app.dao.usuario_dao import UsuarioDAO

usuario_bp = Blueprint('usuario', __name__)
dao = UsuarioDAO()

@usuario_bp.route('/')
def cadastro():
    return render_template('usuario/cadastro.html')

@usuario_bp.route('/cadastro', methods=['POST'])
def cadastrar():
    nome  = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']
    perfil = request.form['perfil']

    if not nome or not email or not senha or not perfil:
        return render_template('usuario/cadastro.html', erro='Preencha todos os campos.')

    usuario = Usuario(nome, email, senha, perfil)
    sucesso = dao.inserir(usuario)

    if sucesso:
        return redirect(url_for('usuario.menu'))
    else:
        return render_template('usuario/cadastro.html', erro='Erro ao cadastrar. Tente novamente.')

@usuario_bp.route('/login')
def login():
    return render_template('usuario/login.html')

@usuario_bp.route('/login', methods=['POST'])
def autenticar():
    email = request.form['email']
    senha = request.form['senha']

    usuario = dao.buscar_por_email(email)

    if usuario and usuario['senha'] == senha:
        return redirect(url_for('usuario.menu'))
    else:
        return render_template('usuario/login.html', erro='Email ou senha incorretos.')

@usuario_bp.route('/menu')
def menu():
    return render_template('index.html')
