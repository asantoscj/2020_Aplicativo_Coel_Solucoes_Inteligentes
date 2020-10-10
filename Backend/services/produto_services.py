from infra.produto.produto_dao import \
    listar as dao_listar, \
    consultar as dao_consultar, \
    cadastrar as dao_cadastrar, \
    remover as dao_remover, \
    alterar as dao_alterar

from model.produto import Produto


def listar():
    return [produto.__dict__() for produto in dao_listar()]


def localizar(id):
    produto = dao_consultar(id)
    if produto is None:
        return None
    return produto.__dict__()


def criar(produto_dados):
    produto = Produto.criar(produto_dados)
    return dao_cadastrar(produto)


def remover(id):
    dados_produto = localizar(id)
    if dados_produto is None:
        return 0
    dao_remover(Produto.criar(dados_produto))
    return 1


def atualizar(id_produto, alimentacao, caracteristica, categoria_venda,
              certificado, codigo_pedido, descricao_completa, descricao_reduzida,
              fabricante, funcao, id_categoria, modelo, montagem, status,
              tag, id_parametros,
              id_equivalencia, id_historico, id_ligacoes):
    produto = Produto.criar({"id_produto": id_produto, "alimentacao": alimentacao, "caracteristica": caracteristica,
                             "categoria_venda": categoria_venda, "certificado": certificado, "codigo_pedido": codigo_pedido,
                             "descricao_completa": descricao_completa, "descricao_reduzida": descricao_reduzida,
                             "fabricante": fabricante, "funcao": funcao, "id_categoria": id_categoria, "modelo": modelo,
                             "montagem": montagem, "status": status, "tag": tag, "id_parametros": id_parametros,
                             "id_equivalencia": id_equivalencia, "id_historico": id_historico, "id_ligacoes": id_ligacoes})
    dao_alterar(produto)
    return localizar(id)
