from flask import jsonify

from app.services.obrasExposicao_service import ObraExposicaoService
from app.controllers.base_controller import base_controller

obraExposicao_service = ObraExposicaoService()
obraExposicao_controller = base_controller(obraExposicao_service)

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
