from flask import Blueprint, request, jsonify, abort
from app.models.seguranca_model import Seguranca
from app.models.localizacao_model import Localizacao
from app.views.seguranca_view import seguranca_to_dict, error_response
from app.extentions import db

seguranca_bp = Blueprint('seguranca_bp', __name__,url_prefix='/seguranca')

@seguranca_bp.route('/', methods=['GET'])
def get_segurancas():
    segurancas = Seguranca.query.all()
    return jsonify([seguranca_to_dict(seguranca) for seguranca in segurancas])

@seguranca_bp.route('/<int:id>', methods=['GET'])
def get_seguranca(id):
    seguranca = Seguranca.query.get_or_404(id)
    return jsonify(seguranca_to_dict(seguranca))

@seguranca_bp.route('/', methods=['POST'])
def create_seguranca():
    data = request.get_json()
    seguranca = Seguranca(
        nome=data['nome'],
        email=data.get('email'),
        telefone=data.get('telefone'),
        localizacao_id=data.get('localizacao_id')
    )
    if seguranca.localizacao_id is None:
        return error_response("Localiazacao não associada", 400)
    localizacao = Localizacao.query.get(seguranca.localizacao_id)
    if localizacao is None:
        return error_response("Lolizacao não localizada",404)
    if seguranca.nome is None:
        return error_response("Campo nome deve ser preenchido", 400)
    db.session.add(seguranca)
    db.session.commit()
    return jsonify(seguranca_to_dict(seguranca)), 201

@seguranca_bp.route('/<int:id>', methods=['PUT'])
def update_seguranca(id):
    seguranca = Seguranca.query.get_or_404(id)
    data = request.get_json()
    seguranca.nome = data['nome'],
    seguranca.email = data.get('email'),
    seguranca.telefone = data.get('telefone'),
    seguranca.localizacao_id = data.get('localizacao_id')
    if seguranca.localizacao_id is None:
        return error_response("Localiazacao não associada", 400)
    localizacao = Localizacao.query.get(seguranca.localizacao_id)
    if localizacao is None:
        return error_response("Lolizacao não localizada", 404)
    if seguranca.nome is None:
        return error_response("Campo nome deve ser preenchido", 400)
    db.session.commit()
    return jsonify(seguranca_to_dict(seguranca)), 200

@seguranca_bp.route('/<int:id>', methods=['DELETE'])
def delete_seguranca(id):
    autor = Seguranca.query.get_or_404(id)
    db.session.delete(autor)
    db.session.commit()
    return '', 204