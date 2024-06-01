from flask import jsonify

from app.services.visitante_service import VisitanteService
from app.controllers.base_controller import base_controller

visitante_service = VisitanteService()
visitante_controller = base_controller(visitante_service)

def get_by_name(nome):
    result = visitante_service.fetch_by_name(nome)
    if isinstance(result, dict):
        return jsonify(result)
    return result