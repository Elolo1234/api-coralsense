from flask import Blueprint, request, jsonify
from services.pesquisa_service import *

pesquisa_bp = Blueprint("pesquisas", __name__)

@pesquisa_bp.route("/pesquisas", methods=["GET"])
def listar():
    return jsonify(listar_pesquisas_json()), 200

@pesquisa_bp.route("/pesquisas", methods=["POST"])
def criar():
    dados = request.json
    return jsonify(adicionar_pesquisa_json(dados)), 201

@pesquisa_bp.route("/pesquisas/<int:id>", methods=["PUT"])
def atualizar(id):
    dados = request.json
    resultado = atualizar_pesquisa_json(id, dados)
    if resultado:
        return jsonify(resultado), 200
    return jsonify({"erro": "Pesquisa não encontrada"}), 404

@pesquisa_bp.route("/pesquisas/<int:id>", methods=["DELETE"])
def deletar(id):
    if deletar_pesquisa_por_id_json(id):
        return jsonify({"mensagem": "Pesquisa deletada com sucesso!"}), 200
    return jsonify({"erro": "Pesquisa não encontrada"}), 404
