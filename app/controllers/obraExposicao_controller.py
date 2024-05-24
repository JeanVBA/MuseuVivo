from flask import Blueprint, request, jsonify, abort
from app.models.obraExposicao_model import ObraExposicao
from app.models.obra_model import Obra
from app.models.exposicao_model import Exposicao
from app.views.obraExpocicao_view import obraExposicao_to_dict, error_response, obrasExposicao_to_dict
from app.extentions import db

obraExposicao_bp = Blueprint('obraExposicao_bp', __name__,url_prefix='/obraExposicao')

@obraExposicao_bp.route('/', methods=['GET'])
def get_obrasExposicoes():
    obrasExposicoes = ObraExposicao.query.all()
    return jsonify([obraExposicao_to_dict(obraExposicao) for obraExposicao in obrasExposicoes])

@obraExposicao_bp.route('/<int:id>', methods=['GET'])
def get_obraExposicao(id):
    obraExposicao = ObraExposicao.query.get_or_404(id)
    return jsonify(obraExposicao_to_dict(obraExposicao))

@obraExposicao_bp.route('/exposicao/<int:id>', methods=['GET'])
def get_obrasExposicao(id):
    obrasExposicao = ObraExposicao.query.get_or_404(id)
    return jsonify(obrasExposicao_to_dict(obrasExposicao))


@obraExposicao_bp.route('/', methods=['POST'])
def create_obraExposicao():
    data = request.get_json()
    obraExposicao = ObraExposicao(
        obra_id=data.get('obra_id'),
        exposicao_id=data.get('exposicao_id')
    )
    if obraExposicao.obra_id is None:
        return error_response("É necessario associar uma obra", 400)
    obra = Obra.query.get(obraExposicao.obra_id)
    if obra is None:
        return error_response("Obra não localizada", 404)
    if obraExposicao.exposicao_id is None:
        return error_response("É necessario associar uma exposicao",400)
    exposicao = Exposicao.query.get(obraExposicao.exposicao_id)
    if exposicao is None:
        return error_response("Exposicao não localizada",404)
    db.session.add(obraExposicao)
    db.session.commit()
    return jsonify(obraExposicao_to_dict(obraExposicao)), 201

@obraExposicao_bp.route('/<int:id>', methods=['PUT'])
def update_obraExposicao(id):
    obraExposicao = ObraExposicao.query.get_or_404(id)
    data = request.get_json()
    obraExposicao.obra_id = data.get('obra_id'),
    obraExposicao.exposicao_id = data.get('exposicao_id')
    if obraExposicao.obra_id is None:
        return error_response("É necessario associar uma obra", 400)
    obra = Obra.query.get(obraExposicao.obra_id)
    if obra is None:
        return error_response("Obra não localizada", 404)
    if obraExposicao.exposicao_id is None:
        return error_response("É necessario associar uma exposicao",400)
    exposicao = Exposicao.query.get(obraExposicao.exposicao_id)
    if exposicao is None:
        return error_response("Exposicao não localizada",404)
    db.session.commit()
    return jsonify(obraExposicao_to_dict(obraExposicao)), 200

@obraExposicao_bp.route('/<int:id>', methods=['DELETE'])
def delete_obraExposicao(id):
    obraExposicao = ObraExposicao.query.get_or_404(id)
    db.session.delete(obraExposicao)
    db.session.commit()
    return '', 204