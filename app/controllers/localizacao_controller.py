from flask import Blueprint, request, jsonify, abort
from app.models.localizacao_model import Localizacao
from app.views.localizacao_view import localizacao_to_dict, error_response
from app.extentions import db

localizacao_bp = Blueprint('localizacao_bp', __name__,url_prefix='/localizacao')

@localizacao_bp.route('/', methods=['GET'])
def get_localizacoes():
    localizacoes = Localizacao.query.all()
    return jsonify([localizacao_to_dict(localizacao) for localizacao in localizacoes])

@localizacao_bp.route('/<int:id>', methods=['GET'])
def get_localizacao(id):
    localizacao = Localizacao.query.get_or_404(id)
    return jsonify(localizacao_to_dict(localizacao))

@localizacao_bp.route('/', methods=['POST'])
def create_localizacao():
    data = request.get_json()
    localizacao = Localizacao(
        nome=data['nome']
    )
    if localizacao.nome is None:
        return error_response("Campo nome deve ser preenchido", 400)
    db.session.add(localizacao)
    db.session.commit()
    return jsonify(localizacao_to_dict(localizacao)), 201

@localizacao_bp.route('/<int:id>', methods=['PUT'])
def update_localizacao(id):
    localizacao = Localizacao.query.get_or_404(id)
    data = request.get_json()
    localizacao.nome = data['nome']
    if localizacao.nome is None:
        return error_response("Campo nome deve ser preenchido", 400)
    db.session.commit()
    return jsonify(localizacao_to_dict(localizacao)), 200

@localizacao_bp.route('/<int:id>', methods=['DELETE'])
def delete_localizacao(id):
    localizacao = Localizacao.query.get_or_404(id)
    db.session.delete(localizacao)
    db.session.commit()
    return '', 204