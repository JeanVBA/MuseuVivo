from flask import Blueprint, request, jsonify, abort
from app.models.pintura_model import db, Pintura
from app.models.obra_model import Obra
from app.views.pintura_view import pintura_to_dict, error_response

pintura_bp = Blueprint('pintura_bp', __name__, url_prefix='/pintura')

@pintura_bp.route('/', methods=['GET'])
def get_pinturas():
    pinturas = Pintura.query.all()
    return jsonify([pintura_to_dict(pintura) for pintura in pinturas])

@pintura_bp.route('/<int:id>', methods=['GET'])
def get_pintura(id):
    pintura = Pintura.query.get_or_404(id)
    return jsonify(pintura_to_dict(pintura))

@pintura_bp.route('/', methods=['POST'])
def create_pintura():
    data = request.json
    pintura = Pintura(
        obra_id=data['obra_id'],
        tecnica=data.get('tecnica')
    )
    if pintura.obra_id is None:
        return error_response("Para cadastrar a pintura, é necessario o identificador da obra", 400)
    obra = Obra.query.get(pintura.obra_id)
    if obra is None:
        return error_response("Obra não localizada", 404)
    if obra.tipo != 'Pintura':
        return error_response("Para cadastrar pintura, é necessario que a obra seja do tipo 'Pintura'.", 400)
    if pintura.tecnica is None:
        return error_response("Técnica não pode ser nulo", 400)
    db.session.add(pintura)
    db.session.commit()
    return jsonify(pintura_to_dict(pintura)), 201

@pintura_bp.route('/<int:id>', methods=['PUT'])
def update_pintura(id):
    pintura = Pintura.query.get_or_404(id)
    data = request.json
    pintura.obra_id = data.get('obra_id', pintura.obra_id)
    pintura.tecnica = data.get('tecnica', pintura.tecnica)

    if pintura.obra_id is None:
        return error_response("Para cadastrar a pintura, é necessario o identificador da obra", 400)
    obra = Obra.query.get(pintura.obra_id)
    if obra.tipo != 'Pintura':
        return error_response("Para cadastrar pintura, é necessario que a obra seja do tipo 'Pintura'.", 400)
    if pintura.tecnica is None:
        return error_response("Técnica não pode ser nulo", 404)
    db.session.commit()
    return jsonify(pintura_to_dict(pintura))

@pintura_bp.route('/<int:id>', methods=['DELETE'])
def delete_pintura(id):
    pintura = Pintura.query.get_or_404(id)
    db.session.delete(pintura)
    db.session.commit()
    return '', 204