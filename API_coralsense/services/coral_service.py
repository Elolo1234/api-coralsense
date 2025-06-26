from models.coral import Coral

def listar_corais():
    corais = Coral.query.all()
    return [c.to_dict() for c in corais]

def criar_coral(dados):
    novo = Coral(**dados)
    db_session.add(novo)
    db_session.commit()
    return novo.to_dict()

def atualizar_coral(especie, dados):
    coral = Coral.query.get_or_404(especie)
    for chave, valor in dados.items():
        setattr(coral, chave, valor)
    db_session.commit()
    return coral.to_dict()

def deletar_coral(especie):
    coral = Coral.query.get_or_404(especie)
    db_session.delete(coral)
    db_session.commit()
