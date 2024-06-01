from flask import jsonify

from app.services.guia_service import GuiaService
from app.controllers.base_controller import base_controller

guia_service = GuiaService()
guia_controller = base_controller(guia_service)

def get_by_name(nome):
    result = guia_service.fetch_by_name(nome)
    if isinstance(result, dict):
        return jsonify(result)
    return result

