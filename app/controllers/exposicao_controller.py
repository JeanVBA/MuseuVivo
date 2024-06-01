from flask import jsonify

from app.services.exposicao_service import ExposicaoService
from app.controllers.base_controller import base_controller

exposicao_service = ExposicaoService()
exposicao_controller = base_controller(exposicao_service)

def get_by_title(titulo):
    result = exposicao_service.fetch_by_title(titulo=titulo)
    if isinstance(result, dict):
        return jsonify(result)
    return result