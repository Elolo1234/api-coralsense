class Pesquisador:
    def __init__(self, nome, instituicao, especialidade, email):
        self.nome = nome
        self.instituicao = instituicao
        self.especialidade = especialidade
        self.email = email

    def to_dict(self):
        return {
            "nome": self.nome,
            "instituicao": self.instituicao,
            "especialidade": self.especialidade,
            "email": self.email
        }
