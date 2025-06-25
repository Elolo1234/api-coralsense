from models.pesquisador import Pesquisador

def listar_pesquisadores():
    pesquisadores = Pesquisador.query.all()
    return [p.to_dict() for p in pesquisadores]

def criar_pesquisador(dados):
    novo = Pesquisador(**dados)
    db_session.add(novo)
    db_session.commit()
    return novo.to_dict()

def atualizar_pesquisador(nome, dados):
    pesquisador = Pesquisador.query.get_or_404(nome)
    for chave, valor in dados.items():
        setattr(pesquisador, chave, valor)
    db_session.commit()
    return pesquisador.to_dict()

def deletar_pesquisador(nome):
    pesquisador = Pesquisador.query.get_or_404(nome)
    db_session.delete(pesquisador)
    db_session.commit()
