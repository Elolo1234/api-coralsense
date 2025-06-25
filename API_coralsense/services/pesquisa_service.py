from models.pesquisa import Pesquisa

def listar_pesquisas():
    pesquisas = Pesquisa.query.all()
    return [p.to_dict() for p in pesquisas]

def criar_pesquisa(dados):
    nova = Pesquisa(**dados)
    db_session.add(nova)
    db_session.commit()
    return nova.to_dict()

def atualizar_pesquisa(titulo, dados):
    pesquisa = Pesquisa.query.get_or_404(titulo)
    for chave, valor in dados.items():
        setattr(pesquisa, chave, valor)
    db_session.commit()
    return pesquisa.to_dict()

def deletar_pesquisa(titulo):
    pesquisa = Pesquisa.query.get_or_404(titulo)
    db_session.delete(pesquisa)
    db_session.commit()
