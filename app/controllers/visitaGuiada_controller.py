from flask import Blueprint, request, jsonify, abort
from app.models.visitaGuiada_model import VisitaGuiada
from app.models.guia_model import Guia
from app.views.visitasGuiadas_view import visitaGuiada_to_dict, error_response
from app.extentions import db

visitaGuiada_bp = Blueprint('visitaGuiada_bp', __name__,url_prefix='/visitaGuiada')

@visitaGuiada_bp.route('/', methods=['GET'])
def get_visitasGuiadas():
    visitasGuiadas = VisitaGuiada.query.all()
    return jsonify([visitaGuiada_to_dict(visitaGuiada) for visitaGuiada in visitasGuiadas])

@visitaGuiada_bp.route('/<int:id>', methods=['GET'])
def get_visitaGuiada(id):
    visitaGuiada = VisitaGuiada.query.get_or_404(id)
    return jsonify(visitaGuiada_to_dict(visitaGuiada))

@visitaGuiada_bp.route('/', methods=['POST'])
def create_visitaGuiada():
    data = request.get_json()
    visitaGuiada = VisitaGuiada(
        grupo=data['grupo'],
        data_visita=data.get('data_visita'),
        horario=data.get('horario'),
        guia_responsavel_id=data.get('guia_responsavel_id')
    )
    if visitaGuiada.data_visita is None:
        return error_response("Data da visita deve ser preenchida", 400)
    if visitaGuiada.horario is None:
        return error_response("Horario da visita deve ser preenchida", 400)
    if visitaGuiada.guia_responsavel_id is None:
        return error_response("VisitaGuiada precisa ter associada um guia", 400)
    guia = Guia.query.get(visitaGuiada.guia_responsavel_id)
    if guia is None:
        return error_response("Guia não localizado", 404)
    db.session.add(visitaGuiada)
    db.session.commit()
    return jsonify(visitaGuiada_to_dict(visitaGuiada)), 201

@visitaGuiada_bp.route('/<int:id>', methods=['PUT'])
def update_visitaGuiada(id):
    visitaGuiada = VisitaGuiada.query.get_or_404(id)
    data = request.get_json()
    visitaGuiada.grupo = data['grupo'],
    visitaGuiada.data_visita = data.get('data_visita'),
    visitaGuiada.horario = data.get('horario'),
    visitaGuiada.guia_responsavel_id = data.get('guia_responsavel_id')

    if visitaGuiada.data_visita is None:
        return error_response("Data da visita deve ser preenchida", 400)
    if visitaGuiada.horario is None:
        return error_response("Horario da visita deve ser preenchida", 400)
    if visitaGuiada.guia_responsavel_id is None:
        return error_response("VisitaGuiada precisa ter associada um guia", 400)
    guia = Guia.query.get(visitaGuiada.guia_responsavel_id)
    if guia is None:
        return error_response("Guia não localizado", 404)
    db.session.commit()
    return jsonify(visitaGuiada_to_dict(visitaGuiada)), 200

@visitaGuiada_bp.route('/<int:id>', methods=['DELETE'])
def delete_visitaGuiada(id):
    visitaGuiada = VisitaGuiada.query.get_or_404(id)
    db.session.delete(visitaGuiada)
    db.session.commit()
    return '', 204