from flask import request, jsonify
from app.services.visitante_service import VisitanteService

visitante_service = VisitanteService()

def get_visitantes():
    visitantes = visitante_service.fetch_all()
    return jsonify(visitantes)

def get_visitante(id):
    result = visitante_service.fetch_by_id(id)
    if isinstance(result, dict):
        return jsonify(result)
    return result

def create_visitante():
    data = request.get_json()
    result = visitante_service.create(data)
    if isinstance(result, dict):
        return jsonify(result), 201
    return result

def update_visitante(id):
    data = request.get_json()
    result = visitante_service.update(id, data)
    if isinstance(result, dict):
        return jsonify(result), 200
    return result

def delete_visitante(id):
    result = visitante_service.delete(id)
    if result is None:
        return '', 204
    return result