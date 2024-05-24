from flask import Blueprint, request, jsonify, abort
from app.models.guia_model import Guia
from app.views.guia_view import guia_to_dict, error_response
from app.extentions import db


guia_bp = Blueprint('guia_bp', __name__, url_prefix='/guia')

@guia_bp.route('/', methods=['GET'])
def get_guias():
    guias = Guia.query.all()
    return jsonify([guia_to_dict(guia) for guia in guias])

@guia_bp.route('/<int:id>', methods=['GET'])
def get_guia(id):
    autor = Guia.query.get_or_404(id)
    return jsonify(guia_to_dict(autor))

@guia_bp.route('/', methods=['POST'])
def create_guia():
    data = request.get_json()
    guia = Guia(
        nome=data['nome'],
        email=data.get('email'),
        telefone=data.get('telefone')
    )
    if guia.nome is None:
        return error_response("Campo nome deve ser preenchido", 400)
    db.session.add(guia)
    db.session.commit()
    return jsonify(guia_to_dict(guia)), 201

@guia_bp.route('/<int:id>', methods=['PUT'])
def update_guia(id):
    guia = Guia.query.get_or_404(id)
    data = request.get_json()
    guia.nome = data['nome']
    guia.email = data.get('email')
    guia.telefone = data.get('telefone')
    if guia.nome is None:
        return error_response("Campo nome deve ser preenchido", 400)
    db.session.commit()
    return jsonify(guia_to_dict(guia)), 200

@guia_bp.route('/<int:id>', methods=['DELETE'])
def delete_guia(id):
    guia = Guia.query.get_or_404(id)
    db.session.delete(guia)
    db.session.commit()
    return '', 204