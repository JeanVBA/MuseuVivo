from flask import Blueprint, request, jsonify, abort
from app.models.ingresso_model import Ingresso
from app.models.visitante_model import Visitante
from app.models.visitaGuiada_model import VisitaGuiada
from app.views.ingresso_view import ingresso_to_dict, error_response
from app.extentions import db

ingresso_bp = Blueprint('ingresso_bp', __name__,url_prefix='/ingresso')

@ingresso_bp.route('/', methods=['GET'])
def get_ingressos():
    ingressos = Ingresso.query.all()
    return jsonify([ingresso_to_dict(ingresso) for ingresso in ingressos])

@ingresso_bp.route('/<int:id>', methods=['GET'])
def get_ingresso(id):
    ingresso = Ingresso.query.get_or_404(id)
    return jsonify(ingresso_to_dict(ingresso))

@ingresso_bp.route('/', methods=['POST'])
def create_ingresso():
    data = request.get_json()
    ingresso = Ingresso(
        visitante_id=data['visitante_id'],
        tipo=data.get('tipo'),
        data_visita=data.get('data_visita'),
        visita_guiada_id=data.get('visita_guiada_id')
    )
    if ingresso.visitante_id is None:
        return error_response("Visitante não associado", 400)
    visitante = Visitante.query.get(ingresso.visitante_id)
    if visitante is None:
        return error_response("Visitante não localizado", 404)
    if ingresso.tipo not in ['Silver', 'Gold', 'Premium']:
        return error_response("O tipo do ingresso deve ser 'Silver, Gold ou Premium'", 400)
    if ingresso.visita_guiada_id is None:
        return error_response("VisitaGuiada não associada", 400)
    visita_guia = VisitaGuiada.query.get(ingresso.visita_guiada_id)
    if visita_guia is None:
        return error_response("VisitaGuiada não localizada", 404)
    db.session.add(ingresso)
    db.session.commit()
    return jsonify(ingresso_to_dict(ingresso)), 201

@ingresso_bp.route('/<int:id>', methods=['PUT'])
def update_ingresso(id):
    ingresso = Ingresso.query.get_or_404(id)
    data = request.get_json()
    ingresso.visitante_id = data['visitante_id'],
    ingresso.tipo = data.get('tipo'),
    ingresso.data_visita = data.get('data_visita'),
    ingresso.visita_guiada_id = data.get('visita_guiada_id')
    if ingresso.visitante_id is None:
        return error_response("Visitante não associado", 400)
    visitante = Visitante.query.get(ingresso.visitante_id)
    if visitante is None:
        return error_response("Visitante não localizado", 404)
    if ingresso.tipo not in ['Silver', 'Gold', 'Premium']:
        return error_response("O tipo do ingresso deve ser 'Silver, Gold ou Premium'", 400)
    if ingresso.visita_guiada_id is None:
        return error_response("VisitaGuiada não associada", 400)
    visita_guia = VisitaGuiada.query.get(ingresso.visita_guiada_id)
    if visita_guia is None:
        return error_response("VisitaGuiada não localizada", 404)
    db.session.commit()
    return jsonify(ingresso_to_dict(ingresso)), 200

@ingresso_bp.route('/<int:id>', methods=['DELETE'])
def delete_ingresso(id):
    autor = Ingresso.query.get_or_404(id)
    db.session.delete(autor)
    db.session.commit()
    return '', 204