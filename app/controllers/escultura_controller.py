from flask import Blueprint, request, jsonify, abort
from app.models.escultura_model import db, Escultura
from app.models.obra_model import Obra
from app.views.escultura_view import escultura_to_dict, error_response

escultura_bp = Blueprint('escultura_bp', __name__, url_prefix='/escultura')

@escultura_bp.route('/', methods=['GET'])
def get_esculturas():
    esculturas = Escultura.query.all()
    return jsonify([escultura_to_dict(escultura) for escultura in esculturas])

@escultura_bp.route('/<int:id>', methods=['GET'])
def get_escultura(id):
    escultura = Escultura.query.get_or_404(id)
    return jsonify(escultura_to_dict(escultura))

@escultura_bp.route('/', methods=['POST'])
def create_escultura():
    data = request.json
    escultura = Escultura(
        obra_id=data['obra_id'],
        material=data.get('material'),
        peso=data.get('peso')
    )
    if escultura.obra_id is None:
        return error_response("Para cadastrar a escultura, é necessario o identificador da obra", 400)
    obra = Obra.query.get(escultura.obra_id)
    if obra.tipo != 'Pintura':
        return error_response("Para cadastrar escultura, é necessario que a obra seja do tipo 'Escultura'.", 400)
    if escultura.tecnica is None:
        return error_response("Material não pode ser nulo", 400)
    db.session.add(escultura)
    db.session.commit()
    return jsonify(escultura_to_dict(escultura)), 201

@escultura_bp.route('/<int:id>', methods=['PUT'])
def update_escultura(id):
    escultura = Escultura.query.get_or_404(id)
    data = request.json
    escultura.obra_id = data.get('obra_id', escultura.obra_id)
    escultura.material = data.get('material', escultura.material)
    escultura.peso = data.get('peso', escultura.peso)

    if escultura.obra_id is None:
        return error_response("Para cadastrar a escultura, é necessario o identificador da obra", 400)
    obra = Obra.query.get(escultura.obra_id)
    if obra.tipo != 'Pintura':
        return error_response("Para cadastrar escultura, é necessario que a obra seja do tipo 'Escultura'.", 400)
    if escultura.tecnica is None:
        return error_response("Material não pode ser nulo", 400)
    db.session.commit()
    return jsonify(escultura_to_dict(escultura))

@escultura_bp.route('/<int:id>', methods=['DELETE'])
def delete_escultura(id):
    escultura = Escultura.query.get_or_404(id)
    db.session.delete(escultura)
    db.session.commit()
    return '', 204