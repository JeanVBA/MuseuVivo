from flask import request, jsonify
from app.services.seguranca_service import SegurancaService

seguranca_service = SegurancaService()

def get_segurancas():
    results = seguranca_service.fetch_all()
    return jsonify(results)

def get_seguranca(id):
    result = seguranca_service.fetch_by_id(id)
    if isinstance(result, dict):
        return jsonify(result)
    return result

def create_seguranca():
    data = request.get_json()
    result = seguranca_service.create(data)
    if isinstance(result, dict):
        return jsonify(result), 201
    return result

def update_seguranca(id):
    data = request.get_json()
    result = seguranca_service.update(id, data)
    if isinstance(result, dict):
        return jsonify(result), 200
    return result

def delete_seguranca(id):
    result = seguranca_service.delete(id)
    if result is None:
        return '', 204
    return result