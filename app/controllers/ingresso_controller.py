from flask import jsonify, request

from app.services.ingresso_service import IngressoService
from app.controllers.base_controller import base_controller

ingresso_service = IngressoService()
ingresso_controller = base_controller(ingresso_service)

def get_by_args():
    tipo = request.args.get('tipo')
    visitante_nome = request.args.get('visitante')

    items = ingresso_service.fetch_by_args(tipo, visitante_nome)
    return jsonify(items)

