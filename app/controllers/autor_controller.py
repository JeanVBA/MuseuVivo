from flask import jsonify

from app.controllers.base_controller import base_controller
from app.services.autor_service import AutorService

autor_service = AutorService()
autor_controller = base_controller(autor_service)

def get_by_name(nome):
    result = autor_service.fetch_by_name(nome)
    if isinstance(result, dict):
        return jsonify(result)
    return result
