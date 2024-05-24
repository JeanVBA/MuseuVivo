from flask import Blueprint, request, jsonify, abort
from datetime import datetime
from app.models.exposicao_model import Exposicao
from app.views.exposicao_view import exposicao_to_dict, error_response
from app.extentions import db

exposicao_bp = Blueprint('exposicao_bp', __name__,url_prefix='/exposicao')

@exposicao_bp.route('/', methods=['GET'])
def get_exposicoes():
    exposicoes = Exposicao.query.all()
    return jsonify([exposicao_to_dict(exposicao) for exposicao in exposicoes])

@exposicao_bp.route('/<int:id>', methods=['GET'])
def get_exposicao(id):
    exposicao = Exposicao.query.get_or_404(id)
    return jsonify(exposicao_to_dict(exposicao))

@exposicao_bp.route('/', methods=['POST'])
def create_exposicao():
    data = request.get_json()
    exposicao = Exposicao(
        titulo=data['titulo'],
        descricao=data.get('descricao'),
        data_inicio=data.get('data_inicio'),
        data_termino=data.get('data_termino')
    )
    if exposicao.titulo is None:
        return error_response("Titulo não pode ser nulo", 400)
    if exposicao.data_termino and datetime.fromisoformat(exposicao.data_termino) < datetime.now():
        return error_response("A data do termino não pode ser antes da data atual", 400)
    db.session.add(exposicao)
    db.session.commit()
    return jsonify(exposicao_to_dict(exposicao)), 201

@exposicao_bp.route('/<int:id>', methods=['PUT'])
def update_exposicao(id):
    exposicao = Exposicao.query.get_or_404(id)
    data = request.get_json()
    exposicao.titulo = data['titulo'],
    exposicao.descricao = data.get('descricao'),
    exposicao.data_inicio = data.get('data_inicio'),
    exposicao.data_termino = data.get('data_termino')
    if exposicao.titulo is None:
        return error_response("Titulo não pode ser nulo", 400)
    if exposicao.data_termino and datetime.fromisoformat(exposicao.data_termino) < datetime.now():
        return error_response("A data do termino não pode ser antes da data atual", 400)
    db.session.commit()
    return jsonify(exposicao_to_dict(exposicao)), 200

@exposicao_bp.route('/<int:id>', methods=['DELETE'])
def delete_exposicao(id):
    exposicao = Exposicao.query.get_or_404(id)
    db.session.delete(exposicao)
    db.session.commit()
    return '', 204