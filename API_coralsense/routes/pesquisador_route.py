from flask import Blueprint, request, jsonify
from services.pesquisador_service import *

pesquisador_bp = Blueprint("pesquisadores", __name__)

@pesquisador_bp.route("/pesquisadores", methods=["GET"])
def listar():
    return jsonify(listar_pesquisadores()), 200

@pesquisador_bp.route("/pesquisadores", methods=["POST"])
def criar():
    dados = request.json
    return jsonify(criar_pesquisador(dados)), 201

@pesquisador_bp.route("/pesquisadores/<string:nome>", methods=["PUT"])
def atualizar(nome):
    dados = request.json
    return jsonify(atualizar_pesquisador(nome, dados)), 200

@pesquisador_bp.route("/pesquisadores/<string:nome>", methods=["DELETE"])
def deletar(nome):
    deletar_pesquisador(nome)
    return jsonify({"mensagem": "Pesquisador deletado com sucesso!"}), 200
