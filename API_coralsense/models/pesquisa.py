class Pesquisa:
    def __init__(self, titulo, objetivo, ano, local, coral_relacionado):
        self.titulo = titulo
        self.objetivo = objetivo
        self.ano = ano
        self.local = local
        self.coral_relacionado = coral_relacionado

    def to_dict(self):
        return {
            "titulo": self.titulo,
            "objetivo": self.objetivo,
            "ano": self.ano,
            "local": self.local,
            "coral_relacionado": self.coral_relacionado
        }
