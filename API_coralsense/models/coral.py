class Coral:
    def __init__(self, especie, nome_popular, extincao, indice_temperatura, indice_poluicao):
        self.especie = especie
        self.nome_popular = nome_popular
        self.extincao = extincao
        self.indice_temperatura = indice_temperatura
        self.indice_poluicao = indice_poluicao

    def to_dict(self):
        return{
            "especie" : self.especie,
            "nome_popular" : self.nome_popular,
            "extincao" : self.extincao,
            "indice_temperatura" : self.indice_temperatura,
            "indice_poluicao" : self.indice_poluicao
        }