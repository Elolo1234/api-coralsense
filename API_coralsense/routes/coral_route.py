from flask import Blueprint, request, jsonify
from services.corais_services import *

coral_bp = Blueprint("corais", __name__)

@coral_bp.route("/corais", methods=["GET"])
def listar():
    lista = listar_corais()
    return jsonify(lista), 200

@coral_bp.route("/corais", methods=["POST"])
def criar():
    dados = request.json
    novo_coral = criar_coral(dados)
    return jsonify(novo_coral), 201

@coral_bp.route("/corais/<string:especie>", methods=["PUT"])
def atualizar(especie):
    dados = request.json
    coral_atualizado = atualizar_coral(especie, dados)
    return jsonify(coral_atualizado), 200

@coral_bp.route("/corais/<string:especie>", methods=["DELETE"])
def deletar(especie):
    deletar_coral(especie)
    return jsonify({"mensagem": "Coral deletado com sucesso!"}), 200
