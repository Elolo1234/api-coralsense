from flask import Blueprint, request, jsonify
from services.pesquisa_service import *

pesquisa_bp = Blueprint("pesquisas", __name__)

@pesquisa_bp.route("/pesquisas", methods=["GET"])
def listar():
    return jsonify(listar_pesquisas()), 200

@pesquisa_bp.route("/pesquisas", methods=["POST"])
def criar():
    dados = request.json
    return jsonify(criar_pesquisa(dados)), 201

@pesquisa_bp.route("/pesquisas/<string:titulo>", methods=["PUT"])
def atualizar(titulo):
    dados = request.json
    return jsonify(atualizar_pesquisa(titulo, dados)), 200

@pesquisa_bp.route("/pesquisas/<string:titulo>", methods=["DELETE"])
def deletar(titulo):
    deletar_pesquisa(titulo)
    return jsonify({"mensagem": "Pesquisa deletada com sucesso!"}), 200
