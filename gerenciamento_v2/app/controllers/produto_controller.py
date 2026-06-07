from flask import Blueprint, render_template, request, redirect, url_for
from app.models.produto import Produto
from app.dao.produto_dao import ProdutoDAO

produto_bp = Blueprint('produto', __name__)
dao = ProdutoDAO()

@produto_bp.route('/produtos')
def listar():
    produtos = dao.listar()
    return render_template('produto/cadastro.html', produtos=produtos)

@produto_bp.route('/produtos/cadastrar', methods=['POST'])
def cadastrar():
    nome = request.form['nome']
    preco = request.form['preco']
    quantidade = request.form['quantidade']
    localizacao = request.form['localizacao']

    if not nome or not preco or not quantidade or not localizacao:
        produtos = dao.listar()
        return render_template('produto/cadastro.html',
                               produtos=produtos,
                               erro='Preencha todos os campos.')

    produto = Produto(nome, preco, quantidade, localizacao)
    sucesso = dao.inserir(produto)

    if sucesso:
        return redirect(url_for('produto.listar'))
    else:
        produtos = dao.listar()
        return render_template('produto/cadastro.html',
                               produtos=produtos,
                               erro='Erro ao cadastrar. Tente novamente.')