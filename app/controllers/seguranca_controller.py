from flask import jsonify

from app.services.seguranca_service import SegurancaService
from app.controllers.base_controller import base_controller

seguranca_service = SegurancaService()
seguranca_controller = base_controller(seguranca_service)

def get_by_name(nome):
    result = seguranca_service.fetch_by_name(nome)
    if isinstance(result, dict):
        return jsonify(result)
    return result