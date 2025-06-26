from flask import Blueprint, request, jsonify
from services.coral_service import *

coral_bp = Blueprint("corais", __name__)

@coral_bp.route("/corais", methods=["GET"])
def listar():
    return jsonify(listar_corais_json()), 200

@coral_bp.route("/corais", methods=["POST"])
def criar():
    dados = request.json
    novo = adicionar_coral_json(dados)
    return jsonify(novo), 201

@coral_bp.route("/corais/<int:id>", methods=["PUT"])
def atualizar(id):
    dados = request.json
    coral = buscar_coral_por_id_json(id)
    if coral:
        coral.update(dados)
        corais = listar_corais_json()
        for i in range(len(corais)):
            if corais[i]["id"] == id:
                corais[i] = coral
        from services.coral_services import salvar_corais_json
        salvar_corais_json(corais)
        return jsonify(coral), 200
    return jsonify({"erro": "Coral não encontrado"}), 404

@coral_bp.route("/corais/<int:id>", methods=["DELETE"])
def deletar(id):
    if deletar_coral_por_id_json(id):
        return jsonify({"mensagem": "Coral deletado com sucesso!"}), 200
    return jsonify({"erro": "Coral não encontrado"}), 404