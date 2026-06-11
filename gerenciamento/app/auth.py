from functools import wraps
from flask import session, redirect, url_for, abort

def login_requerido(f):
    @wraps(f)
    def decorador(*args, **kwargs):
        if 'usuario_id' not in session:
            return redirect(url_for('usuario.login'))
        return f(*args, **kwargs)
    return decorador

def somente_admin(f):
    @wraps(f)
    def decorador(*args, **kwargs):
        if 'usuario_id' not in session:
            return redirect(url_for('usuario.login'))
        if session.get('usuario_perfil') != 'ADMIN':
            abort(403)   # Acesso negado
        return f(*args, **kwargs)
    return decorador

def somente_admin_ou_operador(f):
    @wraps(f)
    def decorador(*args, **kwargs):
        if 'usuario_id' not in session:
            return redirect(url_for('usuario.login'))
        if session.get('usuario_perfil') not in ('ADMIN', 'OPERADOR'):
            abort(403)   # Acesso negado
        return f(*args, **kwargs)
    return decorador