from flask import Blueprint, render_template, request, redirect, url_for, session
from app.dao.usuario_dao import UsuarioDAO

usuario = Blueprint('usuario', __name__)

dao = UsuarioDAO()

# ROTA: LOGIN

@usuario.route('/', methods=['GET', 'POST'])
@usuario.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login_digitado = request.form.get('login')
        senha_digitada = request.form.get('senha')

        # Valida se os campos estão preenchidos
        if not login_digitado or not senha_digitada:
            return render_template('usuario/login.html', erro='Preencha todos os campos.')

        # Chama o DAO para autenticar
        usuario_encontrado = dao.autenticar(login_digitado, senha_digitada)

        if usuario_encontrado:
            session['usuario_id'] = usuario_encontrado[0]
            session['usuario_nome'] = usuario_encontrado[1]
            session['usuario_perfil'] = usuario_encontrado[4]
            return redirect(url_for('usuario.dashboard'))
        else:
            return render_template('usuario/login.html', erro='Login ou senha incorretos.')

    return render_template('usuario/login.html')


# =========================
# ROTA: CADASTRO
# =========================
@usuario.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form.get('nome')
        login_novo = request.form.get('login')
        senha = request.form.get('senha')
        perfil = request.form.get('perfil')

        # Valida se os campos estão preenchidos
        if not nome or not login_novo or not senha or not perfil:
            return render_template('usuario/cadastro.html', erro='Preencha todos os campos.')

        # Chama o DAO para inserir
        dao.inserir(nome, login_novo, senha, perfil)

        return redirect(url_for('usuario.login'))

    return render_template('usuario/cadastro.html')


# =========================
# ROTA: DASHBOARD
# =========================
@usuario.route('/dashboard')
def dashboard():
    if 'usuario_id' not in session:
        return redirect(url_for('usuario.login'))

    return render_template('usuario/dashboard.html')


# =========================
# ROTA: LOGOUT
# =========================
@usuario.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('usuario.login'))