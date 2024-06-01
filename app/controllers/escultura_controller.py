from flask import jsonify

from app.services.escultura_service import EsculturaService
from app.controllers.base_controller import base_controller

escultura_service = EsculturaService()
escultura_controller = base_controller(escultura_service)

def get_by_obra_nome(obra_nome):
    result = escultura_service.fetch_by_obra_nome(obra_nome)
    if isinstance(result, dict):
        return jsonify(result)
    return result