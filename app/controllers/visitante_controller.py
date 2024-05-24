from flask import Blueprint, request, jsonify, abort
from app.models.visitante_model import Visitante
from app.views.visitante_view import visitante_to_dict, error_response
from app.extentions import db


visitante_bp = Blueprint('visitante_bp', __name__,url_prefix='/visitante')

@visitante_bp.route('/', methods=['GET'])
def get_visitantes():
    visitantes = Visitante.query.all()
    return jsonify([visitante_to_dict(visitante) for visitante in visitantes])

@visitante_bp.route('/<int:id>', methods=['GET'])
def get_visitante(id):
    autor = Visitante.query.get_or_404(id)
    return jsonify(visitante_to_dict(autor))

@visitante_bp.route('/', methods=['POST'])
def create_visitante():
    data = request.get_json()
    visitante = Visitante(
        nome=data['nome'],
        email=data.get('email'),
        telefone=data.get('telefone')
    )
    if visitante.nome is None:
        return error_response("Campo nome deve ser preenchido", 400)
    db.session.add(visitante)
    db.session.commit()
    return jsonify(visitante_to_dict(visitante)), 201

@visitante_bp.route('/<int:id>', methods=['PUT'])
def update_visitante(id):
    visitante = Visitante.query.get_or_404(id)
    data = request.get_json()
    visitante.nome = data['nome']
    visitante.email = data.get('email')
    visitante.telefone = data.get('telefone')
    if visitante.nome is None:
        return error_response("Campo nome deve ser preenchido", 400)
    db.session.commit()
    return jsonify(visitante_to_dict(visitante)), 200

@visitante_bp.route('/<int:id>', methods=['DELETE'])
def delete_visitante(id):
    visitante = Visitante.query.get_or_404(id)
    db.session.delete(visitante)
    db.session.commit()
    return '', 204