import json
import os


CAMINHO_PESQUISA_JSON = "dados/pesquisas.json"




def carregar_pesquisas_json():
    try:
        with open(CAMINHO_PESQUISA_JSON, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def salvar_pesquisas_json(lista_pesquisas):
    with open(CAMINHO_PESQUISA_JSON, "w", encoding="utf-8") as f:
        json.dump(lista_pesquisas, f, indent=4, ensure_ascii=False)

def adicionar_pesquisa_json(pesquisa):
    
    pesquisas = carregar_pesquisas_json()
    pesquisa["id"] = len(pesquisas) + 1
    pesquisas.append(pesquisa)
    salvar_pesquisas_json(pesquisas)
    return pesquisa

def listar_pesquisas_json():
   
    return carregar_pesquisas_json()

def buscar_pesquisa_por_id_json(id):
  
    for p in carregar_pesquisas_json():
        if p["id"] == id:
            return p
    return None

def atualizar_pesquisa_json(id, dados_atualizados):
    
    pesquisas = carregar_pesquisas_json()
    for i, p in enumerate(pesquisas):
        if p["id"] == id:
            pesquisas[i].update(dados_atualizados)
            salvar_pesquisas_json(pesquisas)
            return pesquisas[i]
    return None

def deletar_pesquisa_por_id_json(id):
  
    pesquisas = carregar_pesquisas_json()
    nova_lista = [p for p in pesquisas if p["id"] != id]
    if len(nova_lista) < len(pesquisas):
        salvar_pesquisas_json(nova_lista)
        return True
    return False
