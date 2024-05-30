from flask import jsonify, request

from app.services.obrasExposicao_service import ObraExposicaoService
from app.controllers.base_controller import base_controller

obraExposicao_service = ObraExposicaoService()
obraExposicao_controller = base_controller(obraExposicao_service)


def update_by_ids(obra_id, exposicao_id):
    data = request.get_json()
    item = obraExposicao_service.update(obra_id, exposicao_id, data)
    if isinstance(item, dict):
        return jsonify(item)
    return item

def delete_by_ids(obra_id, exposicao_id):
    result = obraExposicao_service.delete(obra_id, exposicao_id)
    if result is None:
        return '', 204
    return result

def get_by_obraId(id):
    result = obraExposicao_service.fetch_by_obra_id(id)
    if isinstance(result, dict):
        return jsonify(result)
    return result

def get_by_Exposicaoid(id):
    result = obraExposicao_service.fetch_by_exposicao_id(id)
    if isinstance(result, dict):
        return jsonify(result)
    return result
