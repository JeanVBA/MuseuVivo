from flask import Blueprint, request, jsonify, abort
from app.models.exposicao_model import Exposicao
from app.views.exposicao_view import exposicao_to_dict
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
    db.session.commit()
    return jsonify(exposicao_to_dict(exposicao)), 200