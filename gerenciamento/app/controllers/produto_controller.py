from flask import Blueprint, render_template, request, redirect, url_for
from app.models.produto import Produto
from app.dao.produto_dao import ProdutoDAO
from app.dao.estoque_dao import EstoqueDAO

produto_bp = Blueprint('produto', __name__)
dao = ProdutoDAO()
estoque_dao = EstoqueDAO()

@produto_bp.route('/produtos')
def listar():
    produtos = dao.listar()
    return render_template('index.html', produtos=produtos)

@produto_bp.route('/produtos/cadastrar', methods=['POST'])
def cadastrar():
    nome       = request.form['nome']
    preco      = request.form['preco']
    quantidade = int(request.form['quantidade'])
    localizacao = request.form['localizacao']
    descricao  = request.form.get('descricao') or None

    if not nome or not preco or not quantidade or not localizacao:
        return redirect(url_for('produto.listar'))

    produto = Produto(nome, preco, 0, localizacao, descricao)
    id_produto = dao.inserir(produto)

    if id_produto:
        estoque_dao.registrar_entrada(id_produto, quantidade)

    return redirect(url_for('produto.listar'))
@produto_bp.route('/produtos/excluir/<int:id_produto>', methods=['POST'])
def excluir(id_produto):
    dao.excluir(id_produto)
    return redirect(url_for('produto.listar'))
 
@produto_bp.route('/produtos/editar/<int:id_produto>', methods=['POST'])
def editar(id_produto):
    nome        = request.form['nome']
    preco       = request.form['preco']
    quantidade  = int(request.form['quantidade'])
    localizacao = request.form['localizacao']
 
    produto = Produto(nome, preco, quantidade, localizacao, id_produto=id_produto)
    dao.atualizar(produto)
    return redirect(url_for('produto.listar'))